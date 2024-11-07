from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from checklist.models import Club, Airplane, Checklist, ChecklistItem


@login_required
def index(request: HttpRequest):
    clubs = []

    if request.user.is_authenticated:
        clubs = Club.objects.filter(users__in=[request.user])

    return render(request, "checklist_index.html", {"clubs": clubs})


@login_required
def club_index(request: HttpRequest, club_id: int):
    club = Club.objects.get(id=club_id)
    airplanes = Airplane.objects.filter(clubs__in=[club_id])
    return render(request, "club_index.html", {"club": club, "airplanes": airplanes})


@login_required
def airplane_index(request: HttpRequest, club_id: int, airplane_id: int):
    club = Club.objects.get(id=club_id)
    airplane = Airplane.objects.get(id=airplane_id)
    checklists = Checklist.objects.filter(airplane=airplane)
    return render(request, "airplane_index.html", {"club": club, "airplane": airplane, "checklists": checklists})


@login_required
def checklist_detail(request: HttpRequest, club_id: int, airplane_id: int, checklist_id: int):
    club = Club.objects.get(id=club_id)
    airplane = Airplane.objects.get(id=airplane_id)
    checklist = Checklist.objects.get(id=checklist_id)
    first_item = ChecklistItem.objects.filter(checklist=checklist).order_by("order").first()
    return render(request, "checklist_detail.html", 
                  {"club": club, "airplane": airplane, "checklist": checklist, "first_item": first_item})

@login_required
def checklist_walk(request: HttpRequest, club_id: int, airplane_id: int, checklist_id: int, item_id: int):
    club = Club.objects.get(id=club_id)
    airplane = Airplane.objects.get(id=airplane_id)
    checklist = Checklist.objects.get(id=checklist_id)
    current_item = ChecklistItem.objects.get(id=item_id)
    index = ChecklistItem.objects.order_by("order").filter(checklist=checklist, order__lte=current_item.order).count()
    count = ChecklistItem.objects.filter(checklist=checklist).count()
    last_item = ChecklistItem.objects.order_by("order").filter(checklist=checklist, order__lt=current_item.order).last()
    next_item = ChecklistItem.objects.order_by("order").filter(checklist=checklist, order__gt=current_item.order).first()
    return render(request, "checklist_walk.html",
                  {"club": club, "airplane": airplane, "checklist": checklist, "current_item": current_item,
                   "last_item": last_item, "next_item": next_item, "index": index, "count": count})
