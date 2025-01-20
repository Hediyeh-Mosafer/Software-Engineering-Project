from django.urls import path
from .views import register
from django.contrib.auth import views as auth_views
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login')),
    path('register/', register, name='register'),
    path('login/', views.custom_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

]
