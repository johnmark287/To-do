from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=50)
    completed = models.BooleanField()
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)