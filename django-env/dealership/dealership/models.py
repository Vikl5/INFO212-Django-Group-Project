from unittest.util import _MAX_LENGTH
from django.db import models

class Car(models.Model):
    make = models.CharField(max_length = 50)
    carmodel = models.CharField(max_length = 50)
    year = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    status = models.CharField(max_length = 50)
    

    def __str__(self):
        return self.make + '' + self.carmodel + '' + self.year + '' + self.location + '' + self.status
        
class Customer(models.Model):
    name = models.CharField(max_length = 200)
    age = models.CharField(max_length = 20)
    address = models.CharField(max_length = 200)

    def __str__(self):
        return self.name + '' + self.age + '' + self.address
