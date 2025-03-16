from django.urls import path
from .views import *
urlpatterns = [
    path('',credentials, name='credentials'),
    path('login/',logins,name='login'),
    path('signup/',signup,name='signup'),
    
    
   
]
