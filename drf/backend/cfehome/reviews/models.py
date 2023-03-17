from django.db import models
from products.models import Product
from users.models import UserModel


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
        ordering = ['-created_at']

    def __str__(self) -> str:
        return f"{self.rating} stars - {self.product.name} - {self.user.username}"
