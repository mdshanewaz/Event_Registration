from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView, TemplateView
from EventApp.models import EventModel
from EventApp.forms import EventForm

# Create your views here.

@login_required
def home_view(request):
    title = 'Dashboard'
    return render(request, 'EventApp/dash.html', context={'title':title})

@login_required
def event_view(request):
    title = 'CREATE EVENT'
    form = EventForm
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('LoginApp:profile'))
    return render(request, 'EventApp/create_event.html', context={'title':title, 'form':form})

