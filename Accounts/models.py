from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date
import os
import uuid

class MyUser(AbstractUser):
    first_name = models.CharField(max_length=100, null=True,blank=True)
    last_name = models.CharField(max_length=100, null=True,blank=True)
    is_user = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='profile_pics/', null=True,blank=True)
    dob = models.CharField(max_length=100, null=True,blank=True)
    bio = models.TextField( null=True,blank=True)
    server_id = models.CharField(max_length=10, null=True,blank=True, unique=True)
    doj = models.DateField(default=date.today)

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)


class Forgotpassword(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
# Create your models here.
