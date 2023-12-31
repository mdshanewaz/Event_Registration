from django import forms
from tkinter import Widget
from EventApp.models import EventModel

# Forms Stat here
class EventForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = '__all__'
        exclude = ('user', 'created_date')

        widgets = {
            'event_date' : forms.DateInput(attrs={'type': 'date'}),
            'event_time' : forms.TimeInput(attrs={'type': 'time'}),
        }
