from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['user', 'coworking_space', 'ticket_amount']

class VerifyForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['payment_status']

class CancelForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['booking_status']