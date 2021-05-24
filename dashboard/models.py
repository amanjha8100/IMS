from django.db import models
from django.contrib.auth.models import User


# Create your models here.
cat_choices = (
    ("Stationary","Stationary"),
    ("Electronics","Electronics"),
    ("Food","Food"),
)

class Product(models.Model):
    name = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=100, choices=cat_choices,null=True)
    quantity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Product'
        ordering = ['category']

    def __str__(self):
        return f'{self.name}-{self.category}-{self.quantity}'

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    staff = models.ForeignKey(User,models.CASCADE,null=True)
    date = models.DateTimeField(auto_now_add=True)
    oquantity = models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural = 'Order'

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'