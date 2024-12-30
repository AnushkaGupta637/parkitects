# parking_app/forms.py
from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'address']

class BookingForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    car_plate_number = forms.CharField(label='Car Plate Number', max_length=20)
    phone_number = forms.CharField(label='Phone Number', max_length=15)
    entry_time = forms.TimeField(label='Entry Time')