# main/admin.py

from django.contrib import admin
from .models import Category, Product, About, Order, Contact


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'min_quantity')
    list_filter = ('category',)
    search_fields = ('name', 'description')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'total_price', 'customer_name', 'customer_phone', 'customer_address', 'payment_status')
    list_filter = ('payment_status', 'product')
    search_fields = ('customer_name', 'customer_phone', 'product__name')

admin.site.register(Order, OrderAdmin)

admin.site.register(About)
# Enregistrer les modèles dans l'interface admin
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'created_at')
    search_fields = ('name', 'email', 'phone_number')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
