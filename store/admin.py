from django.contrib import admin

from .models import Product, Variation

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'stock', 'is_available', 'category', 'created_at', 'updated_at']
    prepopulated_fields = {'slug':('product_name', )}
    readonly_fields = ['created_at', 'updated_at']
    search_fields = ('product_name', 'category')
    ordering = ('-created_at',)
    filter_horizontal = ()
    list_filter = ()

@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ['variation_choice', 'variation_value', 'is_active']
    list_editable = ('is_active', )