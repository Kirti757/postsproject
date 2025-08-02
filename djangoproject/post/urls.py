from django.urls import path

app_name='post'

from post import views
urlpatterns = [
    path('', views.posts_list, name='posts_list'),


    path('new-post/', views.post_new, name='post_new'),
    path('<slug:slug>', views.posts_page, name='posts_page'),
    


    
]
