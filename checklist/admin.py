from django.contrib import admin

from .models import Airplane, Checklist, ChecklistItem

admin.site.register(Airplane)
admin.site.register(Checklist)
admin.site.register(ChecklistItem)
