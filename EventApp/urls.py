from django.urls import path
from EventApp import views


app_name = 'EventApp'

urlpatterns = [
    path('', views.profile_view, name='profile'),
]