from django import forms
from tkinter import Widget
from EventApp.models import EventModel, RegistrationModel

# Forms Stat here
class EventForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = '__all__'
        exclude = ('user', 'created_date', 'member', 'slots')

        widgets = {
            'event_date' : forms.DateInput(attrs={'type': 'date'}),
            'event_time' : forms.TimeInput(attrs={'type': 'time'}),
        }

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegistrationModel
        fields = []             # No fields are included

class EventSearchForm(forms.Form):
    title = forms.CharField(label='Title', max_length=500, required=False)


