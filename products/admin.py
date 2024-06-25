from django.contrib import admin

from .models import (
    ProductImage,
    Product, 
    Color, 
    Size, 
    Material, 
    WashInstruction, 
    ProductType, 
    Area, 
    ProductInventory, 
    ProductImage
)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', 'image_url', 'alt_text')

class ProductInventoryInline(admin.TabularInline):
    model = ProductInventory
    extra = 1

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'alt_text', 'has_image', 'has_url')
    list_filter = ('product',)
    search_fields = ('product__name', 'alt_text')

    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True

    def has_url(self, obj):
        return bool(obj.image_url)
    has_url.boolean = True

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'price', 'on_sale', 'date_added')
    list_filter = ('on_sale', 'product_type', 'areas')
    search_fields = ('name', 'sku', 'description')
    inlines = [ProductImageInline, ProductInventoryInline]

admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Material)
admin.site.register(WashInstruction)
admin.site.register(ProductType)
admin.site.register(Area)
admin.site.register(ProductInventory)