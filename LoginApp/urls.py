from django.urls import path
from LoginApp import views


app_name = 'LoginApp'

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('signup/', views.signupView, name='signup'),
    path('logout/', views.logoutView, name='logout'),
]