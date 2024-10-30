from django.db import models


class Airplane(models.Model):
    name = models.CharField(max_length=50, help_text="The model name of the aircraft.")
    callsign = models.CharField(max_length=8, help_text="The aircraft callsign.")

    def __str__(self) -> str:
        return f"{self.name} ({self.callsign})"


class Checklist(models.Model):
    airplain = models.ForeignKey(Airplane, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name} ({self.airplain})"


class ChecklistItem(models.Model):
    checklist = models.ForeignKey(Checklist, on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    hint = models.TextField(max_length=500)

    def __str__(self) -> str:
        return f"{self.name} ({self.checklist})"
