
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from .models import *
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken






class ReservationCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Reservation successful!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('email')  
        password = data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, email=username, password=password)
        refresh = RefreshToken.for_user(user)

        return Response({
            "message": "User registered successfully",
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        }, status=status.HTTP_201_CREATED)
        

class DeactivateUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            user_token = UserToken.objects.get(user=request.user)
            
            if not user_token.status:
         
                return Response({"message": "User is already inactive."}, status=status.HTTP_400_BAD_REQUEST)
            
       
            user_token.deactivate_user()
            return Response({"message": "User deactivated and access token deleted."}, status=status.HTTP_200_OK)
        
        except UserToken.DoesNotExist:
            return Response({"message": "User token not found."}, status=status.HTTP_404_NOT_FOUND)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
    
            user_token, created = UserToken.objects.get_or_create(user=user)
            user_token.access_token = access_token
            user_token.refresh_token = refresh_token
            user_token.save()
            return Response({
                'access_token': access_token,
                'refresh_token': refresh_token,
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'detail': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MenuItem
from .serializers import MenuItemSerializer

class MenuListView(APIView):
    def get(self, request):
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        return Response(serializer.data)
