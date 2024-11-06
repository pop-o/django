from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)
    # return HttpResponse("<h1>Welcome to home page of blog</h1>")

def about(request):
    return render(request,'blog/about.html',{'title':'About Page'})
    # return HttpResponse('<h1>About Page</h1>')