from django.shortcuts import render
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class ListTask(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'main/index.html'


class DetailTask(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'main/task.html'


class CreateTask(CreateView):
    model = Task
    context_object_name = 'task'
    template_name = 'main/create.html'
    fields = '__all__'
    success_url = reverse_lazy('index')


class UpdateTask(UpdateView):
    model = Task
    context_object_name = 'task'
    template_name = 'main/create.html'
    fields = '__all__'
    success_url = reverse_lazy('index')


class DeleteTask(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('index')
