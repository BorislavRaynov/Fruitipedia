from django.db import models
from django.core.validators import MinLengthValidator
from .validators import check_name_starts_with_letter

# Create your models here.
class Profile(models.Model):

    first_name = models.CharField(
        max_length=25,
        validators=[MinLengthValidator(2), check_name_starts_with_letter],
        null=False,
        blank=False
    )

    last_name = models.CharField(
        max_length=35,
        validators=[MinLengthValidator(1), check_name_starts_with_letter],
        null=False,
        blank=False
    )

    email = models.EmailField(
        max_length=40,
        null=False,
        blank=False
    )

    password = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(8)],
        null=False,
        blank=False
    )

    picture = models.URLField(
        null=True,
        blank=True
    )

    age = models.IntegerField(
        default=18,
        null=True,
        blank=True
    )
