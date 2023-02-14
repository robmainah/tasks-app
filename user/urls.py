from django.urls import path
from django.contrib.auth import views as aut_views
from . import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('register', views.register, name='register'),
    path('login', aut_views.LoginView.as_view(template_name='user/login.html'), 
        name='login'),
    path('logout', aut_views.LogoutView.as_view(), name='logout'),
]
