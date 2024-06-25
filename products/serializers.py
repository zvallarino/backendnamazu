from rest_framework import serializers
from .models import Product, ProductImage, ProductInventory

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image', 'image_url', 'alt_text']

class ProductInventorySerializer(serializers.ModelSerializer):
    color = serializers.StringRelatedField()
    size = serializers.StringRelatedField()

    class Meta:
        model = ProductInventory
        fields = ['color', 'size', 'quantity']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    inventory = ProductInventorySerializer(source='productinventory_set', many=True, read_only=True)
    colors = serializers.StringRelatedField(many=True)
    sizes = serializers.StringRelatedField(many=True)
    materials = serializers.StringRelatedField(many=True)
    wash_instructions = serializers.StringRelatedField(many=True)
    product_type = serializers.StringRelatedField()
    areas = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product
        fields = '__all__'

