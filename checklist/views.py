from django.http import HttpResponse

from checklist.models import Airplane


def index(request):
    return HttpResponse("Hello, world. You're at the checklist index...")


def airplane_detail(request, airplane_id: int):
    try:
        ap = Airplane.objects.get(id=airplane_id)
        return HttpResponse(f"Details for Airplane {ap}")
    except Airplane.DoesNotExist:
        return HttpResponse(f"Airplane {airplane_id} does not exist")
