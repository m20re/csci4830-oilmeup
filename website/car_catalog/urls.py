from django.urls import path
from . import views

urlpatterns = [
    # Automatically redirects to index.html
    path('', views.index, name='index'),

]