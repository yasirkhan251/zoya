# Generated by Django 5.0.4 on 2024-05-12 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DataBase', '0003_music_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='music',
            name='description',
        ),
    ]
