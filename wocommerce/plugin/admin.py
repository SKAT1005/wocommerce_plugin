from django.contrib import admin

from .models import Order, API, Type_API


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['date', 'status']

@admin.register(API)
class APIAdmin(admin.ModelAdmin):
    list_display = ['type']

@admin.register(Type_API)
class TypeAPIAdmin(admin.ModelAdmin):
    list_display = ['name']