from django.db import models
import os
import string
import random
# Create your models here.
from django.db import models
from Accounts.models import MyUser


def unique_ids():
    length = 10
    while True:
        unique_id = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        return unique_id

class Movies(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    unique_id = models.CharField(max_length=10, unique=True, default=unique_ids)
    title = models.CharField(max_length=100,default='Movie')
    file = models.FileField(upload_to='movies/', blank=True, null=True)
    image= models.ImageField(upload_to='dynamic/file/music/thumbnails',blank=True, null=True)
    def delete(self, *args, **kwargs):
        # Delete the file when the Music object is deleted
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title

class Music(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, default=None)
    unique_id = models.CharField(max_length=10, unique=True, default=unique_ids)
    title = models.CharField(max_length=100,default='Music')
    file = models.FileField(upload_to='music/', blank=True, null=True, )
    image= models.ImageField(upload_to='music/thumbnails',blank=True, null=True)
    def delete(self, *args, **kwargs):
        if self.file:
            if os.path.isfile(self.file.path) :
                os.remove(self.file.path)
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title

class Photos(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default='Photo')
    unique_id = models.CharField(max_length=10, unique=True, default=unique_ids)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='photos/', blank=True, null=True)
    def delete(self, *args, **kwargs):
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        super().delete(*args, **kwargs)
    def __str__(self):
        return self.title

class Videos(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    unique_id = models.CharField(max_length=10, unique=True, default=unique_ids)
    title = models.CharField(max_length=100, default='Video')
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='videos/', blank=True, null=True)
    def delete(self, *args, **kwargs):
        if self.file:
            if os.path.isfile(self.file.path):
                os.remove(self.file.path)
        super().delete(*args, **kwargs)
    def __str__(self):
        return self.title
