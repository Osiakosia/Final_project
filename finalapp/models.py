
# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from PIL import Image
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField
import pytz
description = HTMLField()

utc = pytz.UTC


class Order(models.Model):
    date = models.DateField(
        verbose_name=_("Date"),
        auto_now_add=True,
        help_text="Order creation date")
    car = models.ForeignKey(
        verbose_name="Car",
        to="Car",
        on_delete=models.SET_NULL,
        null=True,
        related_name="orders",
    )

    ORDER_STATUS = (
        ("0", "New"),
        ("1", "Declined"),
        ("2", "Accepted"),
        ("3", "Waiting"),
        ("4", "In progress"),
        ("5", "Completed"),
    )

    status = models.CharField(
        verbose_name=_("Status"),
        max_length=1,
        choices=ORDER_STATUS,
        default="0",
        help_text="Order status",
    )

    deadline = models.DateTimeField(
        verbose_name=_("Deadline"),
        help_text="Order finish date & time")

    user = models.ForeignKey(
        to=User,
        verbose_name=_("User"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return (
            f"{self.date} {self.status} {self.deadline}"
        )

        class Meta:
            verbose_name = _("Order")
            verbose_name_plural = _("Orders")
            ordering = ["-id"]

class OrderLine(models.Model):
    order = models.ForeignKey(
        verbose_name="Order",
        to="Order",
        on_delete=models.CASCADE
    )
    service = models.ForeignKey(
        verbose_name="Service",
        to="Service",
        on_delete=models.SET_NULL,
        null=True
    )
    quantity = models.IntegerField(verbose_name=_("Quantity"), default=1)

    def __str__(self):
        return (
            f"{self.order} {self.service} {self.quantity}"
        )

        @property
        def total_price(self):
            total_price = 0
            for line in self.lines.all():
                total_price += line.price
            return total_price

        @property
        def is_overdue(self):
            return self.deadline and self.deadline.replace(
                tzinfo=utc
            ) < datetime.today().replace(tzinfo=utc)

        class Meta:
            verbose_name = _("Order line")
            verbose_name_plural = _("Order lines")


class Car(models.Model):
    license_plate_no = models.CharField(
        verbose_name=_("License plate No"),
        max_length=16, null=True, blank=True)
    vin_code = models.CharField(
        verbose_name=_("VIN code")
        , max_length=17)
    client_name = models.CharField(
        verbose_name=_("Client name"),
        max_length=128)
    car_model = models.ForeignKey(
        verbose_name="Model",
        to="CarModel",
        on_delete=models.SET_NULL,
        null=True,
        related_name="cars",
    )
    client_name = models.CharField(
        verbose_name=_("Client's name"),
        max_length=64)
    observations = HTMLField()
    photo = models.ImageField(
        upload_to="car_photos/", default="car_photos/no_photo.png"
    )


    def __str__(self):
        return (
            f"{self.license_plate_no} {self.vin_code}, {self.client_name}, {self.car_model}, "
        )

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'



class Service(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=128)
    price = models.DecimalField(
        verbose_name=_("Price"),
        max_digits=8, decimal_places=2)
    description = models.TextField(
        verbose_name=_("Description"),
        max_length=2048)

    def __str__(self):
        return (
        f"{self.name} {self.price} {self.description}"
        )

        class Meta:
            verbose_name = 'Service'
            verbose_name_plural = 'Services'
            ordering = ["id"]

class CarModel(models.Model):
    make = models.CharField(
        verbose_name=_("Make"),
        max_length=64,
    )
    model = models.CharField(
        verbose_name=_("Model"),
        max_length=64,
    )
    year = models.PositiveIntegerField(
        "Year", help_text="Year of manufacture")
    engine_type = models.CharField(
        "Engine type",
        max_length=64,
    )

    FUEL_CHOICES = (
        ("G", "Gasoline"),
        ("D", "Diesel"),
        ("L", "LPG"),
        ("H", "Hybrid"),
        ("E", "Electric"),
    )

    fuel_type = models.CharField(
        "Fuel",
        max_length=1,
        choices=FUEL_CHOICES,
        blank=True,
        help_text="Type of engine power",
    )

    description = models.TextField("Description", max_length=2048)

    def __str__(self):
        return (
            f"{self.make} {self.model}, {self.year}, {self.engine_type}, "
            f"{self.fuel_type}"
    )

    class Profile(models.Model):
        user = models.OneToOneField(
            to=User, verbose_name=_("User"), on_delete=models.CASCADE
        )
        picture = models.ImageField(
            verbose_name=_("Picture"),
            upload_to="profile_pics",
            default="profile_pics/default.png",
        )

        def __str__(self):
            profile = _("profile")
            return f"{self.user.username} {profile}"

        class Meta:
            verbose_name = _("Profile")
            verbose_name_plural = _("Profiles")

        def save(self, *args, **kwargs):
            super().save(*args, **kwargs)
            img = Image.open(self.picture.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.picture.path)