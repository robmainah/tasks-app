from django.urls import path
from django.contrib.auth import views as aut_views
from . import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('register', views.register, name='register'),
    path('login', aut_views.LoginView.as_view(
        template_name='user/login.html'), name='login'),
    path('logout', aut_views.LogoutView.as_view(), name='logout'),
    path('reset-password', aut_views.PasswordResetView.as_view(
        template_name='user/reset-password.html'), name='reset-password'),
    path('password_reset_confirm/<uidb64>/<token>', aut_views.PasswordResetConfirmView.as_view(
        template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_done', aut_views.PasswordResetView.as_view(
        template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_complete', aut_views.PasswordResetCompleteView.as_view(
        template_name='user/password_reset_complete.html'), name='password_reset_complete'),
]
