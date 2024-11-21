from django.db import models
from django.http import Http404
from django.contrib.auth.models import User


class Club(models.Model):
    name = models.CharField(max_length=50, help_text="Der Name des Vereins.")
    users = models.ManyToManyField(User, help_text="Mitglieder des Vereins.")
    homepage = models.CharField(max_length=100, help_text="Webseite des Vereins.", blank=True)
    contact = models.CharField(max_length=100, help_text="Kontaktinformationen des Vereins.", blank=True)
    description = models.TextField(max_length=500, help_text="Beschreibung des Vereins.", blank=True)

    def get(user: User, club_id: int):
        clubs = Club.objects.filter(users__in=[user], id=club_id)
        if clubs.count() == 0:
            raise Http404(f"Club {club_id} not found for user {user.username}")
        elif clubs.count() > 1:
            raise ValueError(f"Club not unique. Got {clubs.count()}")
        else:
            return clubs.first()         

    def __str__(self) -> str:
        return f"{self.name}"


class Airplane(models.Model):
    clubs = models.ManyToManyField(Club, help_text="Zu welchem Verein dieses Flugzeug gehört.")
    name = models.CharField(max_length=50, help_text="Der Name des Flugzeugs.")
    callsign = models.CharField(max_length=8, help_text="Das Flugzeug Callsign.")
    picture_url = models.CharField(max_length=100, help_text="Bild von dem Flugzeug.", blank=True)
    description = models.TextField(max_length=500, help_text="Beschreibung des Flugzeugs.", blank=True)

    def get(club: Club, airplane_id: int):
        airplanes = Airplane.objects.filter(clubs__in=[club], id=airplane_id)
        if airplanes.count() == 0:
            raise Http404(f"Airplane {airplane_id} not found for club {club}")
        elif airplanes.count() > 1:
            raise ValueError(f"Airplane not unique. Got {airplanes.count()}")
        else:
            return airplanes.first()

    def __str__(self) -> str:
        return f"{self.name} ({self.callsign})"


class Checklist(models.Model):
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, help_text="Für welches Flugzeug diese Checkliste gilt.")
    name = models.CharField(max_length=50, help_text="Name der Checkliste.")
    description = models.TextField(max_length=500, help_text="Beschreibung der Checkliste.", blank=True)

    def get(airplane: Airplane, checklist_id: int):
        checklists = Checklist.objects.filter(airplane=airplane, id=checklist_id)
        if checklists.count() == 0:
            raise Http404(f"Checklist {checklist_id} not found for airplane {airplane}")
        elif checklists.count() > 1:
            raise ValueError(f"Checklist not unique. Got {checklists.count()}")
        else:
            return checklists.first()

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

    def get(checklist: Checklist, checklist_item_id: int):
        checklist_items = ChecklistItem.objects.filter(checklist=checklist, id=checklist_item_id)
        if checklist_items.count() == 0:
            raise Http404(f"Checklist item {checklist_item_id} not found for checklist {checklist}")
        elif checklist_items.count() > 1:
            raise ValueError(f"Checklist not unique. Got {checklist_items.count()}")
        else:
            return checklist_items.first()

    def __str__(self) -> str:
        return f"{self.name} ({self.checklist})"
