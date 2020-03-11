from django.contrib import admin
from .models import  CarType, CarBrand, Color, Car
admin.site.register(CarType)
admin.site.register(CarBrand)
admin.site.register(Color)
admin.site.register(Car)