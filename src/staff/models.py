from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    class Meta:
        _db = "customers"

class Parent(models.Model):
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Child(models.Model):
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)