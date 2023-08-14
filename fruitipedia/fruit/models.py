from django.db import models
from django.core.validators import MinLengthValidator
from .validators import check_name_only_letters

# Create your models here.
class Fruit(models.Model):

    name = models.CharField(
        max_length=30,
        validators=[MinLengthValidator(2), check_name_only_letters],
        blank=False,
        null=False
    )

    image = models.URLField(
        blank=False,
        null=False
    )

    description = models.TextField(
        blank=False,
        null=False
    )

    nutrition = models.TextField(
        blank=True,
        null=True
    )
