from django.shortcuts import render
from rest_framework import generics
from .models import CakeVariety , DisplayCakes , CakeOrder
from .serializers import CakeVarietySerializer , DisplayCakesSerializer, CakeOrderSerializer
# Create your views here.

class DisplayCakes(generics.ListAPIView):
    queryset = DisplayCakes.objects.all()
    serializer_class = DisplayCakesSerializer

class CakeOrder(generics.ListCreateAPIView):
    queryset = CakeOrder.objects.all()
    serializer_class = CakeOrderSerializer

class CakeVariety(generics.ListCreateAPIView):
    queryset = CakeVariety.objects.all()
    serializer_class = CakeVarietySerializer

    