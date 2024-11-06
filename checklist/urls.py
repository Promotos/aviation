from django.urls import path

from . import views


app_name = "checklist"


urlpatterns = [
    path("", views.index, name="index"),
    path("club/<int:club_id>/", views.club_index, name="club_index"),
    path("club/<int:club_id>/airplane/<int:airplane_id>", views.airplane_index, name="airplane_index"),
    path("club/<int:club_id>/airplane/<int:airplane_id>/checklist/<int:checklist_id>", views.checklist_detail, name="checklist_detail")
]
