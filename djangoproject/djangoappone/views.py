from django.shortcuts import render

def home(request):
    return render(request, 'djangoappone/home.html')

def about(request):
    return render(request, 'djangoappone/about.html')



