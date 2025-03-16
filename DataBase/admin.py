from django.contrib import admin
from .models import *
from Accounts.models import *
from django.contrib.auth.models import AbstractUser

import os

class MusicAdmin(admin.ModelAdmin):
    list_display = ['title', 'userss']

    def userss(self, obj):
        return obj.user.username if obj.user else None

    userss.short_description = 'Username'

    
    def delete_model(self, request, obj):
        # Delete the associated file when the Music object is deleted from admin
        if obj.file:
            if os.path.isfile(obj.file.path):
                os.remove(obj.file.path)
        obj.delete()

admin.site.register(Music, MusicAdmin)
admin.site.register(Movies)
admin.site.register(Videos)
admin.site.register(Photos)