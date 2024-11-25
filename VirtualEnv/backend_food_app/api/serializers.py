# api/serializers.py
from rest_framework import serializers
from .models import *

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'reservation_date', 'people_count', 'special_request']





class ChildItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildItem
        fields = ['id', 'title', 'description', 'price', 'image']


class ParentCategorySerializer(serializers.ModelSerializer):
    items = ChildItemSerializer(many=True, read_only=True)

    class Meta:
        model = ParentCategory
        fields = ['id', 'title', 'description', 'image', 'items']

