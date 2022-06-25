from django.contrib import admin
from .models import Profiles


@admin.register(Profiles)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "favorite_city")
