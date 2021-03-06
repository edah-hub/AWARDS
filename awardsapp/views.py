from __future__ import unicode_literals

from telnetlib import AUTHENTICATION
from .email import send_welcome_email
from django.shortcuts import render, redirect, get_object_or_404
from .models import Image,Location,tags, Profile, Review, NewsLetterRecipients, Like, Project
from django.http  import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import NewImageForm, PostForm, RegistrationsForm, UpdatebioForm, ReviewForm, NewProjectForm
from .email import send_welcome_email
from .forms import NewsLetterForm
from rest_framework import generics
from rest_framework.response import Response
from .serializers import ProjectSerializer, ProfileSerializer
from rest_framework import status
from awardsapp.serializers import *
from .permissions import IsAdminOrReadOnly
from django.shortcuts import render
from .models import Profile,Project
from django import forms
from rest_framework.views import APIView
from django.contrib import messages
from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout



# Create your views here.


def index(request):
    all_project=Project.objects.all()
    
    return render(request,'index.html',{'all_project':all_project})

def signin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have successfuly loged in")
            return redirect ("/")
    return render(request,'registration/login.html')

def register(request):
    if request.method == "POST":
        form = RegistrationsForm(request.POST)
        
        
        username=request.POST["username"]
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        if password1 !=password2:
            messages.error(request,'Password do not match')
            return render('/register')
        new_user=User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password1,
        ) 
        new_user.save() 
        return render (request,'registration/login.html')
    return render(request,'registration/registration_form.html')

def profile(request):
    user=request.user
    my_profile=Profile.objects.get(user=user)
    return render(request,"profile.html",{'my_profile':my_profile,"user":user})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user

    if request.method == 'POST':
        form = UpdatebioForm(request.POST, request.FILES, instance=current_user.profile)
        print(form.is_valid())
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')

    else:
        form = UpdatebioForm()
    return render(request, 'registration/edit_profile.html', {"form": form})

# def signout(request):
#     logout(request)
#     if request.method=="POST":
#         messages.success(request,"You have logged out, we will be glad to have you back again")
#         return redirect ("login")
    
def logout(request):
    if request.method=="POST":
        logout(request)
        return redirect('login')

# @login_required(login_url='/accounts/login/')
# def addpost(request):
#     if request.method=="POST":
#         form = PostForm(request.POST,request.FILES)
#         if form.is_valid():
#             post= form.save(commit=False)
#             post.user=request.user
#             post.save()
#             return redirect('home')

#     else:
#         form=PostForm()
#     try:
#         posts=Project.objects.all() 
#         posts=posts[::-1] 
#     except Project.DoesNotExist:
#         posts=None
#     return render(request,'registration/new_post.html',{"form":form,"posts":posts}) 

@login_required(login_url='/accounts/login/')
def postproject(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user=request.user
            project.save()
        return redirect('home')
    else:
        form = PostForm()
    context = {
        'form':form,
    }
    return render(request, 'registration/new_post.html', context)


@login_required(login_url='/accounts/login/')
def home_projects (request):
    # Display all projects here:

    if request.GET.get('search_term'):
        projects = Project.search_project(request.GET.get('search_term'))

    else:
        projects = Project.objects.all()

    form = NewsLetterForm

    if request.method == 'POST':
        form = NewsLetterForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)

            HttpResponseRedirect('home_projects')

    return render(request, 'index.html', {'projects':projects, 'letterForm':form})

def project(request, id):

    try:
        project = Project.objects.get(pk = id)

    except DoesNotExist:
        raise Http404()

    current_user = request.user
    comments = Review.get_comment(Review, id)
    latest_review_list=Review.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            design_rating = form.cleaned_data['design_rating']
            content_rating = form.cleaned_data['content_rating']
            usability_rating = form.cleaned_data['usability_rating']
            comment = form.cleaned_data['comment']
            review = Review()
            review.project = project
            review.user = current_user
            review.comment = comment
            review.design_rating = design_rating
            review.content_rating = content_rating
            review.usability_rating = usability_rating
            review.save()

    else:
        form = ReviewForm()

        # return HttpResponseRedirect(reverse('image', args=(image.id,)))

    return render(request, 'image.html', {"project": project,
                                          'form':form,
                                          'comments':comments,
                                          'latest_review_list':latest_review_list})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('homePage')

    else:
        form = NewImageForm()
    return render(request, 'registration/new_image.html', {"form": form})


@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')

    else:
        form = NewProjectForm()
    return render(request, 'registration/new_post.html', {"form": form})

# Viewing a single picture

def user_list(request):
    user_list = User.objects.all()
    context = {'user_list': user_list}
    return render(request, 'user_list.html', context)


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user

    if request.method == 'POST':
        form = UpdatebioForm(request.POST, request.FILES, instance=current_user.profile)
        print(form.is_valid())
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')

    else:
        form = UpdatebioForm()
    return render(request, 'registration/edit_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def individual_profile_page(request, username=None):
    if not username:
        username = request.user.username
    # images by user id
    images = Image.objects.filter(user_id=username)

    return render (request, 'registration/user_image_list.html', {'images':images, 'username': username})

def search_projects(request):

    # search for a user by their username
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_projects(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "projects": searched_projects})

    else:
        message = "You haven't searched for any person"
        return render(request, 'search.html', {"message": message})

# Search for an image
def search_image(request):

        # search for an image by the description of the image
        if 'image' in request.GET and request.GET["image"]:
            search_term = request.GET.get("image")
            searched_images = Image.search_image(search_term)
            message = f"{search_term}"

            return render(request, 'search.html', {"message": message, "pictures": searched_images})

        else:
            message = "You haven't searched for any image"
            return render(request, 'search.html', {"message": message})
        
        
    

# def search_users(request):
#
#     # search for a user by their username
#     if 'user' in request.GET and request.GET["user"]:
#         search_term = request.GET.get("user")
#         searched_users = Profile.search_users(search_term)
#         message = f"{search_term}"
#
#         return render(request, 'search.html', {"message": message, "profiles": searched_users})
#
#     else:
#         message = "You haven't searched for any person"
#         return render(request, 'search.html', {"message": message})
#
# def user_review_list(request, username=None):
#     if not username:
#         username = request.user.username
#     latest_review_list = Review.objects.filter(user_id=username).order_by('-comment')
#     context = {'latest_review_list':latest_review_list, 'username':username}
#     return render(request, 'user_review_list.html', context)

@login_required(login_url='/accounts/login/')
def individual_profile_page(request, username):
    print(username)
    if not username:
        username = request.user.username
    # images by user id
    images = Image.objects.filter(user_id=username)
    user = request.user
    profile = Profile.objects.get(user=user)
    userf = User.objects.get(pk=username)
    latest_review_list = Review.objects.filter(user_id=username).filter(user_id=username)
    context = {'latest_review_list': latest_review_list}
    if userf:
        print('user found')
        profile = Profile.objects.get(user=userf)
    else:
        print('No suchuser')
    return render (request, 'registration/user_image_list.html', context, {'images':images,
                                                                  'profile':profile,
                                                                  'user':user,
                                                                  'username': username})
def review_list(request):
    latest_review_list = Review.objects.all()
    context = {'latest_review_list':latest_review_list}
    return render(request, 'review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'review_detail.html', {'review': review})


def project_list(request):
    project_list = Project.objects.order_by('-title')
    context = {'project_list':project_list}
    return render(request, 'project_list.html', context)


# AJAX functionality

def newsletter(request):
    name = request.POST.get('your_name')
    email= request.POST.get('email')

    recipient= NewsLetterRecipients(name= name, email =email)
    recipient.save()
    send_welcome_email(name, email)
    data= {'success': 'You have been successfully added to the newsletter mailing list'}
    return JsonResponse(data)

# Project Serializer

class ProjectList(APIView):
    def get(self, request, format = None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many = True)
        return Response(serializers.data)


    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status= status.HTTP_201_CREATED)

        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)


class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project)
        return Response(serializers.data)


    def put(self, request, pk, format = None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)

        else:
            return Response(serializers.errors,
                            status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Profile Serializer

class ProfileList(APIView):
    def get(self, request, format = None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many = True)
        return Response(serializers.data)


    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        permission_classes = (IsAdminOrReadOnly,)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status= status.HTTP_201_CREATED)

        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)


class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)


    def put(self, request, pk, format = None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)

        else:
            return Response(serializers.errors,
                            status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


