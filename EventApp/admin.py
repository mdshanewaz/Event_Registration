from django.contrib import admin
from EventApp.models import EventModel, RegistrationModel

# Register your models here.

admin.site.register(EventModel)
admin.site.register(RegistrationModel)

