from django.shortcuts import render, HttpResponse
from .models import *
from datetime import timedelta
from django.utils import timezone
from django.views.generic import ListView, FormView, View, DetailView
from .forms import *
from django.urls import reverse

# def roomDetailView(request, category):
#     room_list = Room.objects.filter(category=category)

#     context = {"room": room_list, "room_category": category}
#     # print("Context:", context)
#     # return HttpResponse(category)
#     return render(request, 'myhotel/room_detail_view.html', context)

class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form = AvailabilityForm()
        room_list = Room.objects.filter(category=category)
        if len(room_list)>0:
            room = room_list[0]
            for item in room.ROOM_CATEGORIES:
                if item[0] == category:
                    room_category = item[1]
            context = {
                "room_category": room_category,
                "form": form,
            }
            return render(request, 'myhotel/room_detail_view.html', context)
        else:
            return HttpResponse("Category does not exist")
        

    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        room_list = Room.objects.filter(category=category)
        filled_form = AvailabilityForm(request.POST)
        if filled_form.is_valid():
            data = filled_form.cleaned_data
        available_rooms = []
        for room in room_list:
            if room.check_availability(data["check_in"], data["check_out"]):
                available_rooms.append(room)
        if available_rooms[0]:
            room = available_rooms[0]
            booking = Booking.objects.create(
                booker = self.request.user,
                room = room,
                check_in = data["check_in"],
                check_out = data["check_out"]
            )
            return HttpResponse(booking)
        else:
            return HttpResponse("No availability for this category")


def roomListView(request):
    room = Room.objects.first()
    room_list = []
    for item in room.ROOM_CATEGORIES:
        room_url = reverse("RoomDetailView", kwargs={'category': item[0]})
        room_cat = item[1]
        room_list.append((room_cat, room_url))
    context = {"room_list": room_list, }
    return render(request, 'myhotel/room_list_view.html', context)

class BookingList(ListView):
    model = Booking

class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'myhotel/availability_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data["room_category"])
        available_rooms = []
        for room in room_list:
            if room.check_availability(data["check_in"], data["check_out"]):
                available_rooms.append(room)
        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                booker = self.request.user,
                room = room,
                check_in = data["check_in"],
                check_out = data["check_out"]
            )
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse("No availability for this category")

# def form_valid(self, form):
#         data = form.cleaned_data
#         room_list = Room.objects.filter(category=data["room_category"])
#         available_rooms = []
#         for room in room_list:
#             if room.check_availability(data["check_in"], data["check_out"]):
#                 booking = Booking.objects.create(
#                 booker = self.request.user,
#                 room = room,
#                 check_in = data["check_in"],
#                 check_out = data["check_out"]
#                 )
#         if booking:
#             print("Booking:", booking)
#             booking.save()
#             return HttpResponse(booking)
#         else:
#             return HttpResponse("No availability for this category")


def index(request):
    breq = Room.objects.get(number=101)
    booking = breq.booking_set.first()
    check_in = timezone.now() + timedelta(days=1)
    check_out = timezone.now() + timedelta(days=2)
    print("Check-in", booking.check_in)
    print("Check-out", booking.check_out)

    available = breq.check_availability(check_in, check_out)
    context = {"breq": breq, "checkin": check_in, "available": available}

    return render(request, 'myhotel/room_list_view.html', context)




