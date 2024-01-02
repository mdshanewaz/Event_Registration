from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView, TemplateView
from EventApp.models import EventModel, RegistrationModel
from EventApp.forms import EventForm, RegistrationForm, EventSearchForm

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
    slots_value = event.slots
    title = event.title

    try:
        registration = RegistrationModel.objects.get(user=request.user, event=event)
    except RegistrationModel.DoesNotExist:
        registration = None
    
    form = RegistrationForm()

    enroll1 = False
    enroll2 = False
    enroll3 = False
    
    if event.user == request.user:
        enroll1 = True
    elif RegistrationModel.objects.filter(user=request.user, event=event).exists():
        enroll2 = True
    elif slots_value == 0:
        enroll3 = True
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
        'enroll3':enroll3,
    }
        
    return render(request, 'EventApp/event.html', context=context)

@login_required
def dashboard_view(request):
    title = 'DASHBOARD'
    events = EventModel.objects.filter(user=request.user)
    schedules = RegistrationModel.objects.filter(user=request.user)
    return render(request, 'EventApp/dashboard.html', context={'title':title, 'schedules':schedules, 'events':events})

# class EventDeleteView(LoginRequiredMixin, DeleteView):
#     model = RegistrationModel
#     template_name = 'EventApp/event_delete.html'
#     
#     success_url = reverse_lazy('EventApp:dashboard')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = self.title
#         return context
    
#     def delete(self, request, *args, **kwargs):
#         # Get the RegistrationModel instance to be deleted
#         registration_instance = self.get_object()
#         event_instance = registration_instance.event

#         # Increment the slots attribute
#         event_instance.slots += 1
#         event_instance.save()

#         # Proceed with the deletion
#         return super().delete(request, *args, **kwargs)

@login_required
def unregister_view(request, pk):
    title = 'UNREGISTER'

    unreg = False

    registration_instance = get_object_or_404(RegistrationModel, pk=pk)
    event_instance = registration_instance.event

    registration_instance.delete()

    event_instance.slots += 1
    event_instance.save()

    unreg = True

    if unreg == True:
        return HttpResponseRedirect(reverse('EventApp:dashboard'))

    context = {
        'title' : title,
        'object' : registration_instance,
    }

    # return render(request, 'EventApp/event_delete.html', context=context)

@login_required
def search_view(request):
    form = EventSearchForm(request.GET)

    if form.is_valid():
        title_query = form.cleaned_data.get('title')
        # Perform the search based on the title
        events = EventModel.objects.filter(title__icontains=title_query)
    else:
        # If the form is not valid, return all events
        events = EventModel.objects.all()

    context = {
        'form': form, 
        'events': events,
        'title': 'SEARCH',
    }
    
    return render(request, 'EventApp/search.html', context=context) 



