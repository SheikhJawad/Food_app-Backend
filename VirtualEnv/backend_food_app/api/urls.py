from django.urls import path
from .views import *
urlpatterns = [
   path('reservations/', ReservationCreateView.as_view(), name='reservation_create'),
   path('register/', RegisterView.as_view(), name='register'),
   path('login/', LoginView.as_view(), name='login'),

   path('menu-items/', ParentCategoryListAPIView.as_view(), name='menu-items'),
   path('menu-items/<int:categoryId>/children/', ChildItemListAPIView.as_view(), name='child-items'),
]


