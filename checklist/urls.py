from django.urls import path

from . import views


app_name = "checklist"


urlpatterns = [
    path("", views.index, name="index"),
    #path("airplane/<int:airplane_id>/", views.airplane_detail, name="airplane_detail")
]
