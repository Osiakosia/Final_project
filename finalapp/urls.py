from django.urls import path
from . import views
from .views import CustomLogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path("test/", views.test_alerts, name="test_alerts"),
    path("", views.CustomerListView.as_view(), name="home"),
    path("signup/", views.signup, name="signup"),
    path("accounts/logout/", CustomLogoutView.as_view(next_page="index"), name="logout"),

    # Customers
    path("customers/", views.CustomerListView.as_view(), name="customer_list"),
    path("customers/<int:pk>/", views.CustomerDetailView.as_view(), name="customer_detail"),
    path("customers/add/", views.CustomerCreateView.as_view(), name="customer_create"),
    path("customers/<int:pk>/edit/", views.CustomerUpdateView.as_view(), name="customer_update"),
    path("customers/<int:pk>/delete/", views.CustomerDeleteView.as_view(), name="customer_delete"),

    # Cars
    path("cars/", views.CarListView.as_view(), name="car_list"),
    path("cars/<int:pk>/", views.CarDetailView.as_view(), name="car_detail"),
    path("cars/add/", views.CarCreateView.as_view(), name="car_create"),
    path("cars/<int:pk>/edit/", views.CarUpdateView.as_view(), name="car_update"),
    path("cars/<int:pk>/delete/", views.CarDeleteView.as_view(), name="car_delete"),

    # Services
    path("services/", views.ServiceRecordListView.as_view(), name="service_list"),
    path("services/<int:pk>/", views.ServiceRecordDetailView.as_view(), name="service_detail"),
    path("services/add/", views.ServiceRecordCreateView.as_view(), name="service_create"),
    path("services/<int:pk>/edit/", views.ServiceRecordUpdateView.as_view(), name="service_update"),
    path("services/<int:pk>/delete/", views.ServiceRecordDeleteView.as_view(), name="service_delete"),

    # Parts
    path("parts/", views.PartListView.as_view(), name="part_list"),
    path("parts/<int:pk>/", views.PartDetailView.as_view(), name="part_detail"),
    path("parts/add/", views.PartCreateView.as_view(), name="part_create"),
    path("parts/<int:pk>/edit/", views.PartUpdateView.as_view(), name="part_update"),
    path("parts/<int:pk>/delete/", views.PartDeleteView.as_view(), name="part_delete"),

    #  Password
    # Dashboard / index
    path("", views.index, name="index"),

    # ✅ Registration
    path("signup/", views.signup, name="signup"),

    # ✅ Authentication
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="index"), name="logout"),

    # ✅ Password change
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name="registration/password_change.html"), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(template_name="registration/password_change_done.html"), name="password_change_done"),

    # ✅ Password reset
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name="password_reset_complete"),
]
