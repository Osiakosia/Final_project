from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import  Part
from django.shortcuts import render
from .models import Customer, Car, ServiceRecord

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.contrib import messages


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log user in after signup
            return redirect("index")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def index(request):
    context = {
        "customer_count": Customer.objects.count(),
        "car_count": Car.objects.count(),
        "service_count": ServiceRecord.objects.count(),
        "recent_services": ServiceRecord.objects.select_related("car").order_by("-service_date")[:5],
    }
    return render(request, "index.html", context)



class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been logged out successfully.")
        return super().dispatch(request, *args, **kwargs)


# --- Customers ---
class CustomerListView(ListView):
    model = Customer
    template_name = "customers/customer_list.html"


class CustomerDetailView(DetailView):
    model = Customer
    template_name = "customers/customer_detail.html"


class CustomerCreateView(CreateView):
    model = Customer
    fields = ["first_name", "last_name", "phone", "email"]
    template_name = "customers/customer_form.html"
    success_url = reverse_lazy("customer_list")


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ["first_name", "last_name", "phone", "email"]
    template_name = "customers/customer_form.html"
    success_url = reverse_lazy("customer_list")


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("customer_list")


# --- Cars ---
class CarListView(ListView):
    model = Car
    template_name = "cars/car_list.html"


class CarDetailView(DetailView):
    model = Car
    template_name = "cars/car_detail.html"


class CarCreateView(CreateView):
    model = Car
    fields = ["owner", "model", "year", "vin", "license_plate", "color", "mileage"]
    template_name = "cars/car_form.html"
    success_url = reverse_lazy("car_list")


class CarUpdateView(UpdateView):
    model = Car
    fields = ["owner", "model", "year", "vin", "license_plate", "color", "mileage"]
    template_name = "cars/car_form.html"
    success_url = reverse_lazy("car_list")


class CarDeleteView(DeleteView):
    model = Car
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("car_list")


# --- Service Records ---
class ServiceRecordListView(ListView):
    model = ServiceRecord
    template_name = "services/service_list.html"


class ServiceRecordDetailView(DetailView):
    model = ServiceRecord
    template_name = "services/service_detail.html"


class ServiceRecordCreateView(CreateView):
    model = ServiceRecord
    fields = ["car", "service_type", "description", "mileage_at_service",
              "service_date", "cost", "mechanic"]
    template_name = "services/service_form.html"
    success_url = reverse_lazy("service_list")


class ServiceRecordUpdateView(UpdateView):
    model = ServiceRecord
    fields = ["car", "service_type", "description", "mileage_at_service",
              "service_date", "cost", "mechanic"]
    template_name = "services/service_form.html"
    success_url = reverse_lazy("service_list")


class ServiceRecordDeleteView(DeleteView):
    model = ServiceRecord
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("service_list")


# --- Parts ---
class PartListView(ListView):
    model = Part
    template_name = "parts/part_list.html"


class PartDetailView(DetailView):
    model = Part
    template_name = "parts/part_detail.html"


class PartCreateView(CreateView):
    model = Part
    fields = ["name", "part_number", "description", "quantity_in_stock", "unit_price"]
    template_name = "parts/part_form.html"
    success_url = reverse_lazy("part_list")


class PartUpdateView(UpdateView):
    model = Part
    fields = ["name", "part_number", "description", "quantity_in_stock", "unit_price"]
    template_name = "parts/part_form.html"
    success_url = reverse_lazy("part_list")


class PartDeleteView(DeleteView):
    model = Part
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("part_list")
