from django.core import validators
from django.db import models


# Create your models here.


class AppUser(models.Model):
    MIN_LEN_USERNAME = 2

    username = models.CharField(
        unique=True,
        max_length=30,
        validators=(
            validators.MinLengthValidator(MIN_LEN_USERNAME),
        )
    )

    email = models.EmailField(
        unique=True,
    )



