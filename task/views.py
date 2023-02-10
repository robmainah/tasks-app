from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Task

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    ordering = '-updated_at'


class CreateTaskView(CreateView):
    model = Task
    fields = ['title', 'content']
    success_url = '/'

class TaskDetailView(DetailView):
    model = Task
