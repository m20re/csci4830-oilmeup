from django.urls import path
from . import views

urlpatterns = [
    # Automatically redirects to index.html
    path('', views.index, name='index'),
    path('car/', views.CarListView.as_view(), name='car-list'),
    path('car/<int:pk>/', views.CarDetailView.as_view(), name='car-detail'),
]