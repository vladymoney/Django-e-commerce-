from django.core.validators import MinLengthValidator
from django.db import models

from ecomerce.accounts.models import AppUser
from ecomerce.shop.validators import validate_file_size


# Create your models here.

class Photo(models.Model):
    photo = models.ImageField(upload_to="images", validators=(validate_file_size,))
    description = models.TextField(
        max_length=300, validators=(MinLengthValidator(10),), blank=True, null=True
    )
    location = models.CharField(max_length=30, blank=True, null=True)
    price = models.IntegerField
    date_of_publication = models.DateField(auto_now=True)

class Product(models.Model):
    name = models.CharField(max_length=255),
    image = models.ImageField(upload_to='products /'),
    price = models.FloatField(),




