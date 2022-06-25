from django.contrib import admin
from .models import Letting, Address

# Register your models here.


@admin.register(Letting)
class LettingAdmin(admin.ModelAdmin):
    list_display = ("title", "address")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("number", "street", "city", "state", "zip_code", "country_iso_code")


# Register your models here.
