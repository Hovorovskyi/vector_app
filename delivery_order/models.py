from django.db import models
from user.models import User
from menu.models import MenuItem
from djmoney.models.fields import MoneyField


class DeliveryOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem)
    total_price = MoneyField(decimal_places=2, default=0, default_currency='UAH', max_digits=10)
    delivery_address = models.CharField(max_length=255)
