"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# add include to include our urls.py (that' inside blog folder) to main urls file
from django.urls import path, include
# import auth_views from django
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # local: go to 127.0.0.1:8000/accounts/login
    # online: mydjangosite.com/accounts/login
    path('accounts/login/', auth_views.LoginView.as_view(template_name="registration/login.html"), name='login'),

    # local: go to 127.0.0.1:8000/accounts/logout
    # online: mydjangosite.com/accounts/logout
    path('accounts/logout/', view=auth_views.LogoutView.as_view(), name='logout'),

    # add urls file (that' inside blog folder)
    path('', include('blog.urls')),
]
