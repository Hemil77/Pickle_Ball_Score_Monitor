from django.urls import path
from . import views

urlpatterns =[
    path("", views.vatsal),
    path("home", views.energy),    
]
