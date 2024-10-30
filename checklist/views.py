from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the checklist index...")


def airplane_detail(request, airplane_id: int):
    return HttpResponse(f"Details for Airplane {airplane_id}")
