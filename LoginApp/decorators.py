from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth, Group

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('EventApp:profile')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

# def allowed_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             group = None
#             if request.user.groups.exists():
#                 group = request.user.groups.all()[0].name
#             if group in allowed_roles:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return HttpResponse('You are no authorized to view this page')
#         return wrapper_func
#     return decorator