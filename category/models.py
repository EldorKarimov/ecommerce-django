from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    description = models.TextField()
    cat_image = models.ImageField(upload_to='media/photo/categories')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name