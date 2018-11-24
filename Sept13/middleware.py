from django.conf import settings
from django.shortcuts import redirect, reverse
from django.contrib.auth import logout
import re

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_fun, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')
        # if not request.user.is_authenticated:
        #     if True:
        #         return redirect(settings.LOGIN_URL)
        if path == reverse("logout").lstrip('/'):
            logout(request)
        url = any(url.match(path) for url in EXEMPT_URLS)
        if request.user.is_authenticated and url:
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif request.user.is_authenticated or url:
            return None
        else:
            return redirect(settings.LOGIN_URL)
