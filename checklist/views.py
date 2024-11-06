from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from checklist.models import Club


@login_required
def index(request: HttpRequest):
    clubs = []

    if request.user.is_authenticated:
        clubs = Club.objects.filter(users__in=[request.user])

    return render(request, "checklist_index.html", {"clubs": clubs})


@login_required
def club_index(request, club_id: int):
    return render(request, "club_index.html")
