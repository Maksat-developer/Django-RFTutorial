from django.db import models
from users.models import UserModel

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120)

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField()

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

    def __str__(self) -> str:
        return self.name


