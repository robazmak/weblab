
from __future__ import unicode_literals

from django.db import models


class Savings (models.Model):
    capital = models.DecimalField(max_digits=10,decimal_places=2)
    years = models.DecimalField(max_digits=10,decimal_places=2)
    interest = models.DecimalField(max_digits=10,decimal_places=2)
    final_capital = models.DecimalField(max_digits=10,decimal_places=2)

