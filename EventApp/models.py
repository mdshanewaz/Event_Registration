from django.db import models
from django.conf import settings
from LoginApp.models import User

# Create your models here.
class EventModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='event')
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=2000)
    created_date = models.DateTimeField(auto_now_add=True)
    event_date = models.DateField(blank=True, null=True)
    event_time = models.TimeField(blank=True,null=True)
    location = models.CharField(max_length=100)
    slots = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f'{self.title}, {self.event_time}'

class RegistrationModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.event}'