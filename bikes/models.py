from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):          
        return self.name.title() 

class BikeType(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):          
        return self.name.title() 

class Bike(models.Model):
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1980), max_value_current_year])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    bike_type = models.ForeignKey(
        BikeType, 
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
        )
    manufacturer = models.ForeignKey(
        Manufacturer, 
        on_delete=models.CASCADE,
        blank=False,
        null=False
        )


