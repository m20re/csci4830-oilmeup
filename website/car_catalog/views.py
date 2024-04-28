from django.shortcuts import render
from .models import Car, UserProfile
from django.db.models import Q
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
    """View function for home page of the site"""
    # gets the amount of cars
    num_cars = Car.objects.all().count()

    context = {
        'num_cars' : num_cars,
    }

    return render(request, 'index.html', context=context)
# Create your views here.


class CarListView(generic.ListView):
    model = Car
    template_name = 'car_catalog/car_list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)
        sort_by = self.request.GET.get('sort_by', None)
        color = self.request.GET.get('color', None)
        style = self.request.GET.get('style', None)
        fuel_type = self.request.GET.get('fuel_type', None)
        
        #Filtering
        if color:
            queryset = queryset.filter(color=color)
        if style:
            queryset = queryset.filter(style=style)
        if fuel_type:
            queryset = queryset.filter(fuel_type=fuel_type)
        
        #Sorting
        if sort_by == 'price':
            queryset = queryset.order_by('price')
        elif sort_by == 'make':
            queryset = queryset.order_by('make')
        elif sort_by == 'color':
            queryset = queryset.order_by('color')
        # Add more sorting options here as needed.


        search_query = self.request.GET.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(make__icontains=search_query) | Q(model__icontains=search_query)
            )
        return queryset

class CarDetailView(generic.DetailView):
    model = Car
    template_name = 'car_catalog/car_detail.html'
    context_object_name = 'car'

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@login_required
def profile_view(request):
    # Get the logged in user's profile
    user_profile = UserProfile.objects.get(user=request.user)
    budget = user_profile.budget

    # Get the cars within the user's budget
    cars_within_budget = Car.objects.filter(price__lte=budget)

    context = {
        'user': request.user,
        'budget': budget,
        'cars_within_budget': cars_within_budget,
    }

    return render(request, 'profile.html', context)