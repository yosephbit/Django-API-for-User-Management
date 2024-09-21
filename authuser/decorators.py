from rest_framework.response import Response
from rest_framework import status
from functools import wraps
from django.http import JsonResponse
from django.shortcuts import render

def role_required(role, return_template=False):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.role == role:
                return view_func(request, *args, **kwargs)
            else:
                if return_template:
                    return render(request, 'others/unauthorized.html', status=status.HTTP_403_FORBIDDEN)
                return JsonResponse({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
        return wrapper
    return decorator