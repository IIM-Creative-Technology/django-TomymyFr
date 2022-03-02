from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('details/<int:article_id>/', views.details, name='details'),
    path('message/', views.message, name='message'),
]