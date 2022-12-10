from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

from coworkingSpace.models import CoworkingSpace


class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coworking_space = models.ForeignKey(CoworkingSpace, on_delete=models.CASCADE)
    verification_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id
