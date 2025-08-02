"""
URL configuration for djangoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

# from django.urls import path,include,re_path
from django.urls import path,include #replace this line by above line (while deploying)

from django.conf.urls.static import static

#from django.view.static import serve
from django.conf import settings #replace this line by above comment (while deploying)



urlpatterns = [
    path('admin/', admin.site.urls),
    path("usersignin/", include("usersignin.urls")), 
    path('about/',include('djangoappone.urls')),
    path('posts/',include('post.urls',namespace="post")),
    path('',include('djangoappone.urls')),
    
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


#from django.view.static import serve(add this line)
# comment down this line------------>from django.conf import settings
# replace this line from django.urls import path,include ----->with----------->from django.urls import path,include,re_path

