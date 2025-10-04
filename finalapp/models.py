from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

class Customer(models.Model):
    """Represents a car owner (customer of the auto service)."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

from django.db import models

class ServiceRecord(models.Model):
    """Represents a maintenance or repair entry for a car."""
    car = models.ForeignKey("Car", on_delete=models.CASCADE, related_name="service_records")

    SERVICE_TYPE_CHOICES = [
        ("maintenance", "Maintenance"),
        ("repair", "Repair"),
        ("inspection", "Inspection"),
        ("other", "Other"),
    ]

    service_type = models.CharField(max_length=20, choices=SERVICE_TYPE_CHOICES)
    description = models.TextField(help_text="Detailed description of work performed")
    mileage_at_service = models.PositiveIntegerField(blank=True, null=True)
    service_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Staff member who performed the service (optional if you have users/employees)
    mechanic = models.ForeignKey(
        "auth.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="services_performed"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_service_type_display()} on {self.service_date} for {self.car}"

from django.db import models


class Part(models.Model):
    """Represents a part available in the inventory."""
    name = models.CharField(max_length=100)
    part_number = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    quantity_in_stock = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.part_number})"


class ServicePart(models.Model):
    """Junction table: which parts were used in a service record."""
    service_record = models.ForeignKey("ServiceRecord", on_delete=models.CASCADE, related_name="used_parts")
    part = models.ForeignKey("Part", on_delete=models.CASCADE, related_name="service_usages")
    quantity_used = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity_used} x {self.part.name} for {self.service_record}"


from django.db import models


class CarMake(models.Model):
    """Represents a car manufacturer (e.g., Toyota, Ford, BMW)."""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    """Represents a specific model under a manufacturer (e.g., Camry, Focus, X5)."""
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name="models")
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ("make", "name")

    def __str__(self):
        return f"{self.make.name} {self.name}"


class Car(models.Model):
    """Represents a customer's car in the auto service system."""
    owner = models.ForeignKey("Customer", on_delete=models.CASCADE, related_name="cars")
    model = models.ForeignKey(CarModel, on_delete=models.PROTECT, related_name="cars")
    year = models.PositiveIntegerField()
    vin = models.CharField(max_length=17, unique=True, help_text="Vehicle Identification Number")
    license_plate = models.CharField(max_length=15, unique=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    mileage = models.PositiveIntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # New field for pictures
    picture = models.ImageField(upload_to="car_pictures/", blank=True, null=True)

    def __str__(self):
        return f"{self.model} ({self.license_plate})"

