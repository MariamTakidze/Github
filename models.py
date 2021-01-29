from django.db import models

# Create your models here.
class Washer(models.Model):
    first_name     = models.CharField(max_length=120)
    lastname       = models.CharField(max_length=120)
    Sal_percentage = models.IntegerField()

    def __str__(self):
        return self.first_name

class Car(models.Model):
    car_id     = models.CharField(max_length=120)
    car_type   = models.CharField(max_length=120)
    wash_price = models.IntegerField()

    def __str__(self):
        return self.car_id

class Order(models.Model):
    order_date      = models.DateTimeField()
    completion_date = models.DateTimeField()
    order_price     = models.IntegerField()
    washer          = models.ForeignKey('Washer',on_delete=models.CASCADE)
    car             = models.ForeignKey('Car', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.washer}{self.car}"
