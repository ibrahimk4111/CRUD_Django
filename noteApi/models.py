from django.db import models

# Create your models here.
class Note(models.Model):
    body = models.TextField()
    isDone = models.BooleanField(default=False)
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    