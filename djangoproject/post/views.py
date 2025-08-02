from django.shortcuts import render,redirect
from .models import Post
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms


def posts_list(request):
    posts=Post.objects.all().order_by('-date')
    return render(request,'posts/posts_list.html',{'posts':posts})

def posts_page(request,slug):
    post=Post.objects.get(slug=slug) 
    return render(request,'posts/posts_page.html',{'post':post})


#decorator
@login_required(login_url="/usersignin/login/") # checks users are login or logout if not then redirect to login page
def post_new(request):
    if request.method=="POST":
        form =forms.CreatePost(request.POST,request.FILES)
        if form.is_valid():
            newpost=form.save(commit=False)
            newpost.author=request.user
            newpost.save()
            return redirect('post:posts_list')
    else:
        form=forms.CreatePost()
    return render(request,'posts/post_new.html',{'form':form})