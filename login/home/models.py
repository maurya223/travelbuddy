from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# User registration model
class Register(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username



class Contact(models.Model):
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

class TravelOption(models.Model):
    TRAVEL_TYPES = [
        ('Flight', 'Flight'),
        ('Train', 'Train'),
        ('Bus', 'Bus'),
    ]

    travel_id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10, choices=TRAVEL_TYPES)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.type} {self.source} → {self.destination} on {self.date_time}"
class Booking(models.Model):
    user = models.ForeignKey("Register", on_delete=models.CASCADE)   # ✅ linked to Register
    transport_type = models.CharField(max_length=100)
    from_station = models.CharField(max_length=100)
    to_station = models.CharField(max_length=100)
    journey_date = models.DateField()
    seats = models.IntegerField()
    status = models.CharField(max_length=20)


   



