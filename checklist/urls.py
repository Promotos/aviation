from django.urls import path

from . import views


app_name = "checklist"


urlpatterns = [
    path("", views.index, name="index"),
    path("club/<int:club_id>/", views.club_index, name="club_index")
]
