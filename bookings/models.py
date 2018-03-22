from django.db import models

from customers.models import Customer
from cleaners.models import Cleaner


class Booking(models.Model):
    customer = models.ForeignKey(Customer)
    cleaner = models.ForeignKey(Cleaner)
    date = models.DateTimeField()
