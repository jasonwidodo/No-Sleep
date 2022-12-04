from django.contrib import admin
from .models import CoworkingSpace

@admin.register(CoworkingSpace)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nama',),}
    readonly_fields=('created_at', 'last_updated')