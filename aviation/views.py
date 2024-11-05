from django.shortcuts import render
from django.http import HttpRequest

from checklist.models import Club


def index(request: HttpRequest):
    clubs = []
    
    if request.user.is_authenticated:
        clubs = Club.objects.filter(users__in=[request.user])
        
    return render(request, "index.html", {"clubs": clubs})
