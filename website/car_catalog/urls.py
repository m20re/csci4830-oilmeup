from django.urls import path
from car_catalog import views
from django.urls import include
import sys
sys.setrecursionlimit(1500)

urlpatterns = [
    path('', views.index, name='index'),
    path('car/', views.CarListView.as_view(), name='car-list'),
    path('car/<int:pk>/', views.CarDetailView.as_view(), name='car-detail'),
    path('accounts/profile/', views.profile_view, name='profile_view'),
    path('accounts/profile/edit/', views.update_profile, name='profile_edit'),
    
]