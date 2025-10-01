from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Customer, CarMake, CarModel, Car, ServiceRecord, Part, ServicePart


@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["name"]


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ["name", "make"]
    list_filter = ["make"]
    search_fields = ["name", "make__name"]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["license_plate", "model", "year", "owner", "vin"]
    list_filter = ["model__make", "year", "color"]
    search_fields = ["license_plate", "vin", "owner__first_name", "owner__last_name"]
    autocomplete_fields = ["owner", "model"]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone", "email"]
    search_fields = ["first_name", "last_name", "phone", "email"]


class ServicePartInline(admin.TabularInline):
    model = ServicePart
    extra = 1


@admin.register(ServiceRecord)
class ServiceRecordAdmin(admin.ModelAdmin):
    list_display = ["car", "service_type", "service_date", "mileage_at_service", "cost"]
    list_filter = ["service_type", "service_date"]
    search_fields = ["car__license_plate", "description"]
    autocomplete_fields = ["car", "mechanic"]
    inlines = [ServicePartInline]


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ["name", "part_number", "quantity_in_stock", "unit_price"]
    search_fields = ["name", "part_number"]
    list_editable = ["quantity_in_stock", "unit_price"]

