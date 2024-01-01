from django.urls import path
from EventApp import views


app_name = 'EventApp'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create_event/', views.event_create_view, name='create_event'),
    path('event_page/<pk>/', views.event_page_view, name='event_page'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('delete/<pk>/', views.EventDeleteView.as_view(), name='delete'),
]