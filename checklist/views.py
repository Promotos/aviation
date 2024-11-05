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


#@login_required
#def airplane_detail(request, airplane_id: int):
#    try:
#        ap = Airplane.objects.get(id=airplane_id)
#        return HttpResponse(f"Details for Airplane {ap}")
#    except Airplane.DoesNotExist:
#        return HttpResponse(f"Airplane {airplane_id} does not exist")
