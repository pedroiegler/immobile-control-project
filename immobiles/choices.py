from django.utils.translation import gettext_lazy as _
from django.db import models

class TypeImmobile(models.TextChoices):
    APARTMENT = 'APARTAMENTO', 'APARTAMENTO'
    KITNET = 'KITNET', 'KITNET'
    HOUSE = 'CASA', 'CASA'