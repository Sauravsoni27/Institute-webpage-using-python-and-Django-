
from django.contrib import admin
from django.urls import path
from first import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('register/', views.register),
    path('about/', views.about),
    path('contact/', views.contact),
    path('service/', views.service),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('myadmin/', views.adminhome),
    # path('user/', views.userhome),
]
