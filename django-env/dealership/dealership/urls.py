"""dealership URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import cancel_order_car, delete_customer, delete_employee, get_cars, get_customers, get_employee, order_car, save_car, save_customer, save_employee, update_car, delete_car, update_customer, update_employee

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', get_cars),
    path('save_car/', save_car),
    path('update_car/<int:id>', update_car),
    path('delete_car/<int:id>', delete_car),
    path('customers/', get_customers),
    path('save_customer/', save_customer),
    path('update_customer/<int:id>', update_customer),
    path('delete_customer/<int:id>', delete_customer),
    path('employees/', get_employee),
    path('save_employee/', save_employee),
    path('update_employee/<int:id>', update_employee),
    path('delete_employee/<int:id>', delete_employee),
    path('order_car/<int:customer_id>/<int:car_id>', order_car),
    path('cancel_order_car/<int:customer_id>/<int:car_id>', cancel_order_car),
]
