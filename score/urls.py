from django.urls import path
from . import views

urlpatterns =[
    path("", views.pickleball),
    path("home", views.pickleball),    
]
