from django.db import models
import random
import string
from enum import Enum

# Create your models here.

# unique shipment code generator function 
def code_generator():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))


# shipment model
class Shipment(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Progress', 'Progress'),
        ('Done', 'Done')
    )
    code = models.TextField(max_length=10,
                            editable=False, unique=True, default=code_generator)
    name = models.CharField(max_length=20)
    weight = models.FloatField()
    description = models.CharField(max_length=30)
    status = models.CharField(
        max_length=8, choices=STATUS_CHOICES, default='Pending')
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)
    
    
# date calculation property
    @property
    def date(self):
        date = self.createdOn.date()
        return date
    
    
# time calculation property

    @property
    def time(self):
        time = self.createdOn.time().strftime("%H:%M")
        return time
    
    
# price calculation property
    @property
    def price(self):
        sum = 0
        if self.weight in range(1, 5):
            sum = 10
            return sum
        elif self.weight in range(5, 26):
            sum = 100
            return sum
        elif self.weight > 25:
            sum = 300
            return sum

    def __str__(self):
        return f"{self.createdOn}"


# journal model

class Journal(models.Model):
    JOURNALTYPE_CHOICES = (
        ('debitCash', 'debitCash'),
        ('creditRevenue', 'creditRevenue'),
        ('creditPayable', 'creditPayable')
    )
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    type = models.CharField(
        max_length=14, choices=JOURNALTYPE_CHOICES)
    amount=models.FloatField()

   
