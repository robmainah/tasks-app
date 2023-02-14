from django.db import models
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=191, null=True, default=None)
    content = models.TextField(null=True, default=None)
    updated_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
