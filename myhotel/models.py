from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    ROOM_CATEGORIES = [
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    ]
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()

    def check_availability(self, check_in, check_out):
        avail_list = []
        booking_list = self.booking_set.all()
        for booking in booking_list:
            if booking.check_in > check_out or booking.check_out < check_in:
                avail_list.append(True)
            else:
                avail_list.append(False)
        return all(avail_list) #returns True if all items in list are True

           

    def __str__(self):
        return f"room {self.number}|{self.category}|{self.beds} beds|{self.capacity} persons"

class Booking(models.Model):
    booker = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()

    def __str__(self):
        return f"{self.booker} booked {self.room} from {self.check_in} upto {self.check_out}"
