from django.contrib import admin

from .models import Club, Airplane, Checklist, ChecklistItem, ChecklistItemGroup

admin.site.register(Club)
admin.site.register(Airplane)
admin.site.register(Checklist)


class ChecklistItemAdmin(admin.ModelAdmin):
    list_display = ["order", "group", "name"]
    list_filter = ["group"]


admin.site.register(ChecklistItem, ChecklistItemAdmin)
admin.site.register(ChecklistItemGroup)
