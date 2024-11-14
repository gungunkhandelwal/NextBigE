from django.shortcuts import render
from rest_framework import generics,status
from . models import CustomUser
from . serializers import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class RegisterAPIView(generics.CreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=RegisterSerializer
    
class LoginView(APIView):
     def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({'Message': 'Invalid Credential'}, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(generics.RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=ProfileSerializer

    def get_object(self):
        return self.request.user