from django.contrib import admin
from .models import Client, Car, Sale


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'name',
                    'middle_name', 'phone_number', 'date_of_birth']
    list_filter = ['last_name']
    ordering = ['last_name']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['model', 'year', 'color', 'mileage',
                    'volume', 'body_type', 'drive_unit',
                    'gearbox', 'fuel_type', 'price', 'image']
    list_filter = ['model', 'year', 'body_type', 'drive_unit',
                   'gearbox', 'fuel_type']
    search_fields = ['model']
    ordering = ['model', 'price', 'year']


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ['client', 'car', 'created_at']
    list_filter = ['client', 'created_at']
    ordering = ['created_at']
