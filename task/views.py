from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Task

class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'
    ordering = '-updated_at'
    paginate_by = 2


class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'content']
    success_url = '/'


class TaskDetailView(DetailView):
    model = Task


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'content']

    def get_success_url(self, **kwargs):
        return reverse_lazy('task-detail', args=(self.object.id,))


class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/'
