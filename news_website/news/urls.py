from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', home, name='home'),
    path('', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),
]
