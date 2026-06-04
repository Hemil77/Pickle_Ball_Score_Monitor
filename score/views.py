from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

def homepage(request) :
    return HttpResponse("Hello Django")

def pickleball(request) :
    return render(request, 'home.html')

