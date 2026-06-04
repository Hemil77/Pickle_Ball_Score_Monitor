from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

def homepage(request) :
    return HttpResponse("Hello Django")

def pickleball(request) :
    return render(request, 'home.html')

def om(request) :
    return render(request, 'om.html')

def energy(request) :
    return render(request, 'energy.html')

def vatsal(request) :
    return render(request, 'vatsal.html')
