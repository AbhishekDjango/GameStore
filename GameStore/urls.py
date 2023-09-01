"""
URL configuration for GameStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from App import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.Logout,name='logout'),
    path('verify/',views.VerifyOTP,name='verify'),
    path('notverify/',views.NotVerify,name='notverify'),
    path('',views.IndexPage,name='index'),
    path('home/',views.HomePage,name='home'),
    path('store/',views.StorePage,name='store'),
    path('BlockDude/',views.BlockDude,name='blockdude'),
    path('UnrulyTower/',views.UnrulyTower,name='game2'),
    path('StickHero/',views.StickHero,name='game3'),
    path('Mario/',views.Mario,name='game1'),
    path('FlappyBird/',views.Flappybird,name='game4'),
]
