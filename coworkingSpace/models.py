from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class CoworkingSpace(models.Model):
    nama = models.CharField(max_length=200)
    alamat = models.CharField(max_length=200)
    harga = models.CharField(max_length=100)
    kapasitas = models.CharField(max_length=5, default='1')
    detail = models.TextField(null=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='static/spaces/')
    favorit = models.ManyToManyField(User, related_name='favorit', blank=True)

    def get_absolute_url(self):
        return reverse('coworkingSpace:single', args = [self.slug])

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.nama