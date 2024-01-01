from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView, TemplateView
from EventApp.models import EventModel, RegistrationModel
from EventApp.forms import EventForm, RegistrationForm

# Create your views here.

@login_required
def home_view(request):
    title = 'HOME'
    events = EventModel.objects.all()
    return render(request, 'EventApp/home.html', context={'title':title, 'events':events})

@login_required
def event_create_view(request):
    title = 'CREATE EVENT'
    form = EventForm()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('EventApp:dashboard'))
    return render(request, 'EventApp/create_event.html', context={'title':title, 'form':form})

@login_required
def event_page_view(request, pk):
    event = get_object_or_404(EventModel, pk=pk)
    title = event.title

    try:
        registration = RegistrationModel.objects.get(user=request.user, event=event)
    except RegistrationModel.DoesNotExist:
        registration = None
    
    form = RegistrationForm()

    enroll1 = False
    enroll2 = False
    
    if event.user == request.user:
        enroll1 = True
    elif RegistrationModel.objects.filter(user=request.user, event=event).exists():
        enroll2 = True
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                registrationEvent = form.save(commit=False)
                registrationEvent.user = request.user
                registrationEvent.event = event
                registrationEvent.save()
                event.slots -= 1
                event.save()
                return redirect('EventApp:home')
    
    context= {
        'title':title, 
        'event':event, 
        'registration':registration, 
        'form':form, 
        'enroll1':enroll1,
        'enroll2':enroll2,
    }
        
    return render(request, 'EventApp/event.html', context=context)

@login_required
def dashboard_view(request):
    title = 'DASHBOARD'
    events = EventModel.objects.filter(user=request.user)
    schedules = RegistrationModel.objects.filter(user=request.user)
    return render(request, 'EventApp/dashboard.html', context={'title':title, 'schedules':schedules, 'events':events})

class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = RegistrationModel
    template_name = 'EventApp/event_delete.html'
    title = 'UNREGISTER'
    success_url = reverse_lazy('EventApp:dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.title
        return context
