from django.shortcuts import render
from .models import Car

def index(request):
    """View function for home page of the site"""
    # gets the amount of cars
    num_cars = Car.objects.all().count()

    context = {
        'num_cars' : num_cars,
    }

    return render(request, 'index.html', context=context)
# Create your views here.
