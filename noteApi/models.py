from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100, default='')
    body = models.TextField()
    updated = models.DateField(auto_now=True)
    created = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images', default='')
    