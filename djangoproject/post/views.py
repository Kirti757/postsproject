from django.shortcuts import render
from .models import Post
# Create your views here.
from django.http import HttpResponse

def posts_list(request):
    posts=Post.objects.all().order_by('-date')

    return render(request,'posts/posts_list.html',{'posts':posts})

def posts_page(request,slug):
    post=Post.objects.get(slug=slug) 
    return render(request,'posts/posts_page.html',{'post':post})
