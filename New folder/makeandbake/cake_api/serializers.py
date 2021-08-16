from rest_framework import serializers
from .models import CakeVariety , DisplayCakes , CakeOrder

class CakeVarietySerializer(serializers.ModelSerializer):
    class Meta:
        model = CakeVariety
        fields = '__all__'

class DisplayCakesSerializer(serializers.ModelSerializer):
    cake_type = serializers.StringRelatedField()
    class Meta:
        model = DisplayCakes
        fields = '__all__'

class CakeOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CakeOrder
        fields = '__all__'