from django.urls import path
from .views import *
urlpatterns = [
   path('reservations/', ReservationCreateView.as_view(), name='reservation_create'),
]
