from django.shortcuts import render

# Create your views here.


def home(request):
    all_post=Post.objects.all()
    
    return render('index.html',{'all_post':all_post})
