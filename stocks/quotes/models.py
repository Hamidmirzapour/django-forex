from django.db import models
from django.db.models import fields


class Portfolio(models.Model):
    base_currency = fields.CharField(max_length=10)
    quote_currency = fields.CharField(max_length=10)

    def __str__(self) -> str:
        return self.base_currency + '/' + self.quote_currency