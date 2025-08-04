# usersignin/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "usersignin"

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # Password reset flow
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="usersignin/password_reset.html",
            email_template_name="usersignin/password_reset_email.html",
            success_url="/usersignin/password_reset_done/"   # 👈 redirect works
        ),
        name="password_reset"
    ),
    path(
        "password_reset_done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="usersignin/password_reset_done.html"
        ),
        name="password_reset_done"
    ),
    path(
        "reset/<uidb64>/<token>/",    # 👈 MUST include <uidb64> and <token>
        auth_views.PasswordResetConfirmView.as_view(
            template_name="usersignin/password_reset_confirm.html",
            success_url="/usersignin/reset/done/"
        ),
        name="password_reset_confirm"
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="usersignin/password_reset_complete.html"
        ),
        name="password_reset_complete"
    ),
]
