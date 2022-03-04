from django.urls import path
from . import views

app_name = 'reseau'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('create/', views.create, name='create'),
    path('details/<int:pk>/', views.details_post, name='details_post'),
    path('message/', views.message, name='message'),
    path('like/<int:pk>/', views.like_post, name='like_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),

]