# Generated by Django 4.2.1 on 2023-08-09 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noteApi', '0002_note_image_note_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='image',
        ),
    ]