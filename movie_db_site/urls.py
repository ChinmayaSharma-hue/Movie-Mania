"""movie_db_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from pages.views import (
    home,
    movies,
    movieProfile,
    signupPage,
    loginPage,
    logoutPage,
)
from django.urls import include, re_path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("accounts/", include("accounts.urls")),
    path("home", home),
    path("signup/", csrf_exempt(signupPage), name="signup"),
    path("login/", csrf_exempt(loginPage), name="login"),
    path("logout/", csrf_exempt(logoutPage), name="logout"),
    path("check/", movieProfile),
    path("api/", include("api.urls")),
    path("check/<movie_id>", movieProfile),
    path("movies/<category>", movies),
]
