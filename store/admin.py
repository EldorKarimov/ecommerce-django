from django.contrib import admin

from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'stock', 'is_available', 'category', 'created_at', 'updated_at']
    prepopulated_fields = {'slug':('product_name', )}
    readonly_fields = ['created_at', 'updated_at']
    search_fields = ('product_name', 'category')
    ordering = ('-created_at',)
    filter_horizontal = ()
    list_filter = ()