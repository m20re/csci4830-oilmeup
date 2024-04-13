from django.db import models
from django.urls import reverse
from django.conf import settings
from django.db.models.functions import Lower


class Car(models.Model):
    """Model representing a car."""
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    TRANSMISSION_CHOICES = {
        ('automatic', 'Automatic'),
        ('manual', 'Manual'),
    }

    transmission = models.CharField(max_length=50, choices=TRANSMISSION_CHOICES, default='automatic')

    FUEL_CHOICES = {
        ('gasoline', 'Gasoline'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric')
    }

    fuel_type = models.CharField(max_length=50, choices=FUEL_CHOICES, default='gasoline')

    image = models.ImageField(upload_to='cars_images', blank=True, null=True)


    class Meta:
        ordering = ['year', 'make', 'model']

    def get_absolute_url(self):
        """Returns the URL to access a particular car instance."""
        return reverse('car-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.year}, {self.make}, {self.model}'
    
