from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import getTasks, create_task, task_detail

urlpatterns = [
    path('tasks/', getTasks, name='getTasks'),
    path('tasks/create/', create_task, name='create_task'),
    path('tasks/<int:pk>', task_detail, name='task_detail')
]