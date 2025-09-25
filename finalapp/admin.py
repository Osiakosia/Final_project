from django.contrib import admin

# Register your models here.
from .models import Order, OrderLine, Car,Service ,CarModel

admin.site.register(Order)
admin.site.register(OrderLine)
admin.site.register(Car)
admin.site.register(Service)
admin.site.register(CarModel)

