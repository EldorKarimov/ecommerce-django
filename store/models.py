from django.db import models
from category.models import Category

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='media/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_choice='color', is_active=True)
    
    def sizes(self):
        return super(VariationManager, self).filter(variation_choice='size', is_active=True)

variation_choices = (
    ('color', 'color'),
    ('size', 'size')
)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    variation_choice = models.CharField(max_length=100, choices=variation_choices)
    variation_value = models.CharField(max_length=20)

    objects = VariationManager()

    def __str__(self):
        return self.product.product_name