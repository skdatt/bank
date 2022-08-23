from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40,unique=True)
    dob = models.DateField()
    address = models.TextField(max_length=256)
    photo = models.FileField(upload_to='photos/')
    age = models.IntegerField()
    contact = models.BigIntegerField()

    class Meta:
        db_table = 'Customer_Master'