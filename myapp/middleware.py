from django.urls import reverse
from django.shortcuts import redirect

class  RedirectAuthenticatedUserMiddleware:

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            paths_to_redirect = [reverse('blog:login'),reverse('blog:register')]
            if request.path in paths_to_redirect:
                return redirect('blog:index')
            
        response = self.get_response(request)
        return response

class RestrictUnauthorizedUserMiddleware:

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            restricted_paths = [reverse('blog:dashboard')]
            if request.path in restricted_paths:
                return redirect('blog:login')
            
        response = self.get_response(request)
        return response