# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# class ParkingSlot(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     location = models.CharField(max_length=100)
#     datetime_booked = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

class Slot(models.Model):
    slot_number = models.IntegerField(unique=True,default=0)
    booked = models.BooleanField(default=False)


