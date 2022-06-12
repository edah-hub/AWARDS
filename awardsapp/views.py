from django.shortcuts import render
from .models import Profile,Project
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .models import Profile,Project
from .forms import NewImageForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    all_project=Project.objects.all()
    
    return render(request,'index.html',{'all_project':all_project})

def signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have successfuly loged in")
            return redirect ("/")
    return render(request,'login.html')

def register(request):
    if request.method == "POST":
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
        return render (request,'login.html')
    return render(request,'register.html')

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
        return redirect('homePage')

    else:
        form = UpdatebioForm()
    return render(request, 'registration/edit_profile.html', {"form": form})

def signout(request):
    logout(request)
    messages.success(request,"You have logged out, we will be glad to have you back again")
    return redirect ("login")

@login_required(login_url='/accounts/login/')
def addpost(request):
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post= form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('/')

    else:
        form=PostForm()
    try:
        posts=Post.objects.all() 
        posts=posts[::-1] 
    except Post.DoesNotExist:
        posts=None
    return render(request,'newpost.html',{"form":form,"posts":posts}) 

@login_required(login_url='/accounts/login/')
def postproject(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user=request.user
            project.save()
        return redirect('/')
    else:
        form = PostForm()
    context = {
        'form':form,
    }
    return render(request, 'newpost.html', context)


