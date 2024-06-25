# products/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

class Color(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class WashInstruction(models.Model):
    instruction = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.instruction

class ProductType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=50, unique=True)
    num_of_reviews = models.PositiveIntegerField(default=0)
    ave_of_reviews = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        default=0.0
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    colors = models.ManyToManyField(Color, through='ProductInventory')
    sizes = models.ManyToManyField(Size, through='ProductInventory')
    description = models.TextField()
    materials = models.ManyToManyField(Material)
    wash_instructions = models.ManyToManyField(WashInstruction)
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT)
    areas = models.ManyToManyField(Area)
    on_sale = models.BooleanField(default=False)
    sale_amount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    date_added = models.DateTimeField(auto_now_add=True)
    weight = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

class ProductInventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ['product', 'color', 'size']

    def __str__(self):
        return f"{self.product.name} - {self.color.name} - {self.size.name}"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    alt_text = models.CharField(max_length=200)

    def clean(self):
        if not self.image and not self.image_url:
            raise ValidationError("Either an image file or an image URL must be provided.")
        if self.image and self.image_url:
            raise ValidationError("Please provide either an image file or an image URL, not both.")

    def __str__(self):
        return f"Image for {self.product.name}"