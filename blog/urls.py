"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from functools import partial
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.Home,name="home"),
    path("signup/",views.signup,name='signup'),
    path("login/",views.user_login,name='login'),
    path("logout/",views.user_logout,name='logout'),
    path("pass1/",views.pass1,name='pass1'),
    path("pass2/",views.pass2,name='pass2'),
    path("profile/",views.profile,name='profile'),
    path("Post/",views.Post,name="Post"),
    path("read/",views.Read,name="read"),
    
    path("update/<int:id>",views.Update,name="update"),
    path("delete/<int:id>",views.Delete,name="delete"),

]
urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
