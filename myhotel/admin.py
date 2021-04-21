from django.contrib import admin
from .models import *

class RoomAdmin(admin.ModelAdmin):
    list_display = ["id", "number", "category", "beds", "capacity"]
    ordering = ["-id"]

class BookingAdmin(admin.ModelAdmin):
    # list_display = ["id", "number", "category", "beds", "capacity"]
    list_display = ["id", "booker", "room", "check_in", "check_out"]
    ordering = ["-id"]

admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)
