from django.contrib import admin
from .models import dbNote

# Register your models here.
@admin.register(dbNote)
class noteAdmin(admin.ModelAdmin):
    list_display = ('id', 'body')

