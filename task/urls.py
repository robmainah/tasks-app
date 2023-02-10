from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='home'),
    path('new-task', views.CreateTaskView.as_view(), name='new-task'),
]
