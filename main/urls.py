from django.urls import path
from .views import ListTask, DetailTask, CreateTask, UpdateTask, DeleteTask

urlpatterns = [
    path('', ListTask.as_view(), name='index'),
    path('task/<int:pk>', DetailTask.as_view(), name='task'),
    path('create/', CreateTask.as_view(), name='create'),
    path('edit/<int:pk>', UpdateTask.as_view(), name='edit'),
    path('delete/<int:pk>', DeleteTask.as_view(), name='delete')
]
