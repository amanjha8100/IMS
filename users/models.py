from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
# Create your models here.

class Profile(models.Model):
    staff = OneToOneField(User, on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=300,null=True)
    phone = models.PositiveBigIntegerField(null=True)
    image = models.ImageField(default="avatar.jpg",upload_to="Profile_Images")

    def __str__(self):
        return f'{self.staff.username} - Profile'