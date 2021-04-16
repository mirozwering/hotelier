from django.contrib import admin
from .models import *

class RoomAdmin(admin.ModelAdmin):
    list_display = ["id", "number", "category", "beds", "capacity"]
    ordering = ["-id"]

admin.site.register(Room, RoomAdmin)
