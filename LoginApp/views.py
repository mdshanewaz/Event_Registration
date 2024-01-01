from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

# Authentications
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from LoginApp.decorators import unauthenticated_user

# Messagaes 
from django.contrib import messages

# Forms and Models
from LoginApp.models import ProfileModel, User
from LoginApp.forms import ProfileForm, SignupForm

# Create your views here.

@unauthenticated_user
def signupView(request):
    title = 'SIGNUP'
    form = SignupForm
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!")
            return HttpResponseRedirect(reverse('LoginApp:login'))
    return render(request, 'LoginApp/signup.html', context={'title':title, 'form':form})

@unauthenticated_user
def loginView(request):
    title = 'LOGIN'
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('EventApp:home'))
    return render(request, 'LoginApp/login.html', context={'title': title, 'form':form})


@login_required
def logoutView(request):
    logout(request)
    messages.warning(request, "You are logged out!")
    return HttpResponseRedirect(reverse('LoginApp:login'))

@login_required
def profile_view(request):
    title = 'PROFILE'
    profile = ProfileModel.objects.get(user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes are saved to Profile!")
            form = ProfileForm(instance=profile)
    return render(request, 'LoginApp/profile.html', context={'title':title, 'form':form})