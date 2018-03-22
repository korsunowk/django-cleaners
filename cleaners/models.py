from django.db import models

from towns.models import Town


class Cleaner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    quality_score = models.DecimalField(max_digits=5, decimal_places=2)
    towns = models.ManyToManyField(Town, related_name='towns')
