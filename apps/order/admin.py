from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.

class TabularOrderItem(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [TabularOrderItem]