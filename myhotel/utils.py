from .models import Room, Booking
from django.urls import reverse

def get_room_cat_url_list():
    room = Room.objects.first()
    room_list = []
    for item in room.ROOM_CATEGORIES:
        room_url = reverse("RoomDetailView", kwargs={'category': item[0]})
        room_cat = item[1]
        room_list.append((room_cat, room_url))
    return room_list

def get_room_category_human_format(category):
    # room_list = Room.objects.filter(category=category)
    # if len(room_list)>0:
    room = Room.objects.first()
    for item in room.ROOM_CATEGORIES:
        if item[0] == category:
            room_category = item[1]
            return room_category


def get_available_rooms(category, check_in, check_out):
    room_list = Room.objects.filter(category=category)

    available_rooms = []
    for room in room_list:
        if room.check_availability(check_in, check_out):
            available_rooms.append(room)

    if len(available_rooms) > 0:
        return available_rooms

def book_room(request, room, check_in, check_out):
    booking = Booking.objects.create(
            booker = request.user,
            room = room,
            check_in = check_in,
            check_out = check_out
        )
    return booking