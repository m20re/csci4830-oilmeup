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
    

    class Meta:
        ordering = ['year', 'make', 'model']

    def get_absolute_url(self):
        """Returns the URL to access a particular car instance."""
        return reverse('car-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.year}, {self.make}, {self.model}'