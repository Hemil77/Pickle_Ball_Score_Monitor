from django.urls import path
from . import views

urlpatterns =[
    path("", views.vatsal),
    path("home", views.energy),
    path("mullo", views.om),
    path("pickleball", views.pickleball),
    path("energy", views.energy),
    path("vatsal", views.vatsal),
    
]