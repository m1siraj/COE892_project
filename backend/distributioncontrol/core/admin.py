from django.contrib import admin
from .models import Warehouse, WarehouseLocation, DeliveryVehicle, CoverageArea

# Register your models here.

admin.site.register(Warehouse)
admin.site.register(WarehouseLocation)
admin.site.register(DeliveryVehicle)
admin.site.register(CoverageArea)