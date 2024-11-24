# api/serializers.py
from rest_framework import serializers
from .models import *

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'reservation_date', 'people_count', 'special_request']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'image', 'link']
