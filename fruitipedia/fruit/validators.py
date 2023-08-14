from django.core.exceptions import ValidationError


def check_name_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Fruit name should contain only letters!')
