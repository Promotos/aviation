from django.db import models
from django.contrib.auth.models import User


class Club(models.Model):
    name = models.CharField(max_length=50, help_text="Der Name des Vereins.")
    users = models.ManyToManyField(User, help_text="Mitglieder des Vereins.")
    homepage = models.CharField(max_length=100, help_text="Webseite des Vereins.", blank=True)
    description = models.TextField(max_length=500, help_text="Beschreibung des Vereins.", blank=True)

    def __str__(self) -> str:
        return f"{self.name}"


class Airplane(models.Model):
    clubs = models.ManyToManyField(Club, help_text="Zu welchem Verein dieses Flugzeug gehört.")
    name = models.CharField(max_length=50, help_text="Der Name des Flugzeugs.")
    callsign = models.CharField(max_length=8, help_text="Das Flugzeug Callsign.")

    def __str__(self) -> str:
        return f"{self.name} ({self.callsign})"


class Checklist(models.Model):
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, help_text="Für welches Flugzeug diese Checkliste gilt.")
    name = models.CharField(max_length=50, help_text="Name der Checkliste.")

    def __str__(self) -> str:
        return f"{self.name} ({self.airplane})"


class ChecklistItemGroup(models.Model):
    name = models.CharField(max_length=100, help_text="Name der Gruppe.")

    def __str__(self) -> str:
        return f"{self.name}"


class ChecklistItem(models.Model):
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE, help_text="Zu welcher Checkliste dieser Eintrag gehört.")
    order = models.IntegerField(default=0, help_text="Legt die Reihenfolge fest.")
    group = models.ForeignKey(ChecklistItemGroup, on_delete=models.CASCADE, help_text="Gruppe des Eintrags.")
    name = models.CharField(max_length=100, help_text="Name des Eintrags. Bsp. 'Rettungsgerät gesichert.'")
    description = models.TextField(max_length=500, help_text="Beschreibung des Eintrags.", blank=True)
    hint = models.TextField(max_length=500, help_text="Hilfestellung für diesen Eintrag", blank=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.checklist})"
