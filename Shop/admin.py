from django.contrib import admin
from .models import User, Product, Cart, CartItem, Order, OrderItem, DailyData

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'is_buyer', 'is_seller', 'revenue']
    search_fields = ['username', 'email']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    search_fields = ['name']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    search_fields = ['user__username']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'cart', 'product', 'quantity']
    search_fields = ['cart__user__username', 'product__name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_at']
    search_fields = ['user__username']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'product', 'quantity']
    search_fields = ['order__user__username', 'product__name']

@admin.register(DailyData)
class DailyDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'revenue']
    search_fields = ['date']

