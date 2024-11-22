# api/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Reservation
from .serializers import ReservationSerializer

class ReservationCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Reservation successful!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
