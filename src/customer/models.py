from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Parent(models.Model):
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Child(models.Model):
    name = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Images(models.Model):
    image = models.ImageField(upload_to='images/')

