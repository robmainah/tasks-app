from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='home'),
    path('new-task', views.CreateTaskView.as_view(), name='new-task'),
    path('task/<int:pk>', views.TaskDetailView.as_view(), name='task-detail'),
]
