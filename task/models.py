from django.db import models
from django.utils import timezone
from django.shortcuts import redirect

class Task(models.Model):
    title = models.CharField(max_length=191, null=True, default=None)
    content = models.TextField(null=True, default=None)
    updated_at = models.DateTimeField(default=timezone.now)

    # def get_absolute_url(self):
    #     return redirect('home')

    def __str__(self):
        return self.title
