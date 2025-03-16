# middleware.py
from django.urls import *
from django.shortcuts import *

from django.utils import timezone
from django.conf import settings
from django.contrib.auth import logout

class SessionTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            last_activity = request.session.get('last_activity')
            now = timezone.now()
            if last_activity:
                elapsed_time = (now - last_activity).total_seconds()
                if elapsed_time > settings.SESSION_COOKIE_AGE:
                    logout(request)
                    return redirect(reverse('login'))  # Redirect to your login page
            request.session['last_activity'] = now
        response = self.get_response(request)
        return response
