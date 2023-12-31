from django.urls import path
from EventApp import views


app_name = 'EventApp'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create_event/', views.event_view, name='create_event'),
]