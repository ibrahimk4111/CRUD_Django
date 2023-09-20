from django.db import models

class dbNote(models.Model):
    body = models.TextField()
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
