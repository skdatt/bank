from django.db import models


class Customer(models.Model):
    name=models.CharField(max_length=20)
    Age=models.IntegerField()

class Address(models.Model):
    City=models.CharField(max_length=30)
    Pin=models.IntegerField()
    Cust=models.OneToOneField(Customer,on_delete=models.PROTECT)
