from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from coworkingSpace.models import CoworkingSpace


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coworking_space = models.ForeignKey(CoworkingSpace, on_delete=models.CASCADE)
    ticket_amount = models.IntegerField(default=0)
    payment_status = models.BooleanField(default=False)
    booking_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('booking:single', args = [self.id])

    def __str__(self):
        return self.id
