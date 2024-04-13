from django.shortcuts import render
from django.views.generic import ListView, DetailView
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

class CarListView(ListView):
    model = Car
    template_name = 'car_catalog/car_list.html'
    context_object_name = 'cars'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_catalog/car_detail.html'
    context_object_name = 'car'
