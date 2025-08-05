from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CustomPasswordResetCompleteView
from django.urls import reverse_lazy

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
            success_url=reverse_lazy("usersignin:password_reset_done"),   # ✅ FIX
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
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="usersignin/password_reset_confirm.html",
            success_url=reverse_lazy("usersignin:password_reset_complete"),  # ✅ FIX
        ),
        name="password_reset_confirm"
    ),
    path(
        "reset/done/",
        CustomPasswordResetCompleteView.as_view(),
        name="password_reset_complete"
    ),
]
