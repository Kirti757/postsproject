from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm   # <-- new form
from django.contrib.auth.views import PasswordResetCompleteView
from django.urls import reverse_lazy
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("post:posts_list")
    else:
        form = CustomUserCreationForm()
    return render(request, "usersignin/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("post:posts_list")
    else:
        form = AuthenticationForm()
    return render(request, "usersignin/login.html", {"form": form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("post:posts_list")
    return redirect("usersignin:login")

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    def get(self, request, *args, **kwargs):
        messages.success(request, "Your password has been reset successfully. Please log in below.")
        return redirect(reverse_lazy("usersignin:login"))