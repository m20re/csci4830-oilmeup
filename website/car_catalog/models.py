from django.db import models
from django.urls import reverse
from django.conf import settings
from django.db.models.functions import Lower
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
import io


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

    # resizes the image
    def save(self, *args, **kwargs):
        # If an image exists, resize it
        if self.image:
            # open the image
            im = Image.open(self.image)

            # Convert to RGB to avoid errors
            if im.mode != 'RGB':
                im = im.convert('RGB')
            
            # Resize the image
            im.thumbnail((600, 400), Image.Resampling.LANCZOS)

            # Move the image into memory
            output = io.BytesIO()
            im.save(output, format='JPEG', quality=100)
            output.seek(0)

            # Overwrite the old image
            self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg', output.getbuffer().nbytes, None)
        
        # Use django's ORM save to save to the database
        super(Car, self).save(*args, **kwargs)





    class Meta:
        ordering = ['year', 'make', 'model']

    def get_absolute_url(self):
        """Returns the URL to access a particular car instance."""
        return reverse('car-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.year}, {self.make}, {self.model}'
    
