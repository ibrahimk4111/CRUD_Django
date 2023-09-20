from django.db import models

# Create your models here.
class Note(models.Model):
    body = models.TextField()
    is_complete = models.BooleanField()
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    