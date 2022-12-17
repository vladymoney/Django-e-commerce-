from django.core.validators import MinLengthValidator
from django.db import models

from ecomerce.accounts.models import AppUser
from ecomerce.shop.validators import validate_file_size


# Create your models here.

class Photo(models.Model):
    photo = models.URLField()
    description = models.TextField(
        max_length=300, validators=(MinLengthValidator(10),), blank=True, null=True
    ),
    name = models.CharField(max_length=50)
    old_price = models.FloatField()
    price = models.FloatField()
    date_of_publication = models.DateField(auto_now=True)

class Product(models.Model):
    name = models.CharField(max_length=255),
    image = models.ImageField(upload_to='products /'),
    price = models.FloatField(),




