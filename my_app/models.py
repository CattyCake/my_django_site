from django.db import models

# Create your models here.

class Delivery_number(models.Model):
    order_number = models.CharField(null=True, max_length=200, help_text="Введите номер заказа")
    def __str__(self):
        return self.order_number

class Order(models.Model):
    order_name = models.CharField(null=True, max_length=200, help_text="Введите адресс доставки")
    courier = models.ForeignKey('Courier', on_delete=models.SET_NULL, null=True)
    order_number = models.ForeignKey('Delivery_number', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.order_name

class Courier(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name,)
