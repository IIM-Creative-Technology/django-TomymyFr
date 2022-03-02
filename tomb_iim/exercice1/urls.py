from django.urls import path
from . import views

app_name = 'exercice1'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('details/<int:question_id>/', views.details, name='details'),
    path('delete/<int:question_id>/', views.delete, name='delete'),
    path('update/<int:question_id>/', views.update, name='update'),
]