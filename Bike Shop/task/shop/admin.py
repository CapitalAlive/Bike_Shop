from django.contrib import admin
from . import models
# Register your models here.

for model in [models.Frame, models.Seat, models.Tire, models.Basket, models.Bike, models.Order]:
    admin.site.register(model)
