from django.db import models

# Create your models here.
class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()  # Capacity in terms of available space

    def __str__(self):
        return self.name

class WarehouseLocation(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='locations')
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()  # Capacity in terms of available space for this location

    def __str__(self):
        return f"{self.warehouse.name} - {self.location}"

class DeliveryVehicle(models.Model):
    vehicle_number = models.CharField(max_length=20)
    capacity = models.FloatField()  # Capacity in terms of volume

    def __str__(self):
        return self.vehicle_number

class CoverageArea(models.Model):
    warehouse = models.OneToOneField(Warehouse, on_delete=models.CASCADE, related_name='coverage_area')
    area = models.TextField()  # Description of the coverage area (e.g., geographical regions served)

    def __str__(self):
        return f"Coverage Area for {self.warehouse.name}"