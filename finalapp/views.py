
# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import  Part
from .models import Customer, Car, ServiceRecord
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LogoutView
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomerForm

# ----------------------------
# Custom Signup
# ----------------------------
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-login after signup
            messages.success(request, f"✅ Welcome, {user.first_name or user.username}! Your account has been created.")
            return redirect("index")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})


def index(request):
    recent_services = (
        ServiceRecord.objects.select_related("car")
        .order_by("-service_date")[:5]
    )
    context = {
        "customer_count": Customer.objects.count(),
        "car_count": Car.objects.count(),
        "service_count": ServiceRecord.objects.count(),
        "part_count": Part.objects.count(),
        "recent_services": recent_services,
    }
    return render(request, "index.html", context)


def test_alerts(request):
    messages.success(request, "✅ Success! Your action worked.")
    messages.error(request, "❌ Error! Something went wrong.")
    messages.warning(request, "⚠️ Warning! Be careful.")
    messages.info(request, "ℹ️ Info: This is just a test message.")
    return redirect("index")

# ----------------------------
# Custom Login View
# ----------------------------
class CustomLoginView(LoginView):
    template_name = "registration/login.html"

    def form_valid(self, form):
        user = form.get_user()
        messages.success(self.request, f"✅ Welcome back, {user.first_name or user.username}!")
        return super().form_valid(form)



# ----------------------------
# Custom Logout View
# ----------------------------
class CustomLogoutView(LogoutView):
    next_page = "index"

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "✅ You have been logged out successfully.")
        return super().dispatch(request, *args, **kwargs)

# --- Customers ---
class CustomerListView(ListView):
    model = Customer
    template_name = "customers/customer_list.html"
    context_object_name = "customers"   # ✅ important: use same name as template


class CustomerDetailView(DetailView):
    model = Customer
    template_name = "customers/customer_detail.html"


class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customer_form.html"
    success_url = reverse_lazy("customer_list")


class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
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
    fields = ["car", "description", "service_date", "cost"]
    template_name = "services/service_form.html"
    success_url = reverse_lazy("index")  # ✅ Redirect to dashboard after create

    def form_valid(self, form):
        messages.success(self.request, "✅ Service record created successfully!")
        return super().form_valid(form)


class ServiceRecordUpdateView(UpdateView):
    model = ServiceRecord
    fields = ["car", "description", "service_date", "cost"]
    template_name = "services/service_form.html"
    success_url = reverse_lazy("index")  # ✅ Redirect back to dashboard
    def form_valid(self, form):
        messages.success(self.request, "✅ Service record updated successfully!")
        return super().form_valid(form)


class ServiceRecordDeleteView(DeleteView):
    model = ServiceRecord
    template_name = "services/service_confirm_delete.html"
    success_url = reverse_lazy("index")  # ✅ Redirect to dashboard
    def delete(self, request, *args, **kwargs):
        messages.success(request, "🗑️ Service record deleted successfully!")
        return super().delete(request, *args, **kwargs)


# --- Parts ---
class PartListView(LoginRequiredMixin,ListView):
    model = Part
    template_name = "parts/part_list.html"
    context_object_name = "parts"  # 👈 matches your template


class PartDetailView(DetailView):
    model = Part
    template_name = "parts/part_detail.html"
    context_object_name = "part"

# Optional: where to redirect if not logged in
    login_url = "/accounts/login/"  # or your custom login route
    redirect_field_name = "next"

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



