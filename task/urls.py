from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='home'),
    path('new-task', views.CreateTaskView.as_view(), name='new-task'),
    path('task/<int:pk>', views.TaskDetailView.as_view(), name='task-detail'),
    path('task/<int:pk>/update', views.TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete', views.TaskDeleteView.as_view(), name='task-delete'),
]
