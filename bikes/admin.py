from django.contrib import admin
from .models import Manufacturer, BikeType, Bike

admin.site.register(Manufacturer)
admin.site.register(BikeType)
admin.site.register(Bike)

# Register your models here.
