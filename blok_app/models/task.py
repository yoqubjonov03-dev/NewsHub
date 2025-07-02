from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Task(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title






