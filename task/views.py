from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Task

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    ordering = 'updated_at'


class CreateTaskView(CreateView):
    model = Task
    fields = ['title', 'content']
