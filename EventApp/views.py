from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def profile_view(request):
    return HttpResponse("Assalamu Alaikum")