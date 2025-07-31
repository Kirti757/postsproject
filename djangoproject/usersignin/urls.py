from django.urls import path
from usersignin import views
app_name='usersignin'
urlpatterns = [
    path('register/', views.register_view, name='register'),


    

 
]
