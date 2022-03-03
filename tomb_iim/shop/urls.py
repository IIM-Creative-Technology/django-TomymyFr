from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('details/<int:article_id>/', views.details, name='details'),
    path('message/', views.message, name='message'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
]