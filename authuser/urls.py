from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_lists, name='user-list'),
    path('users.html', views.user_lists_template, name='user-list-template'),
    path('profile/', views.profile, name='profile'),
]