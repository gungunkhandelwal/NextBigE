from django.shortcuts import render
from rest_framework import generics,status
from . models import CustomUser
from . serializers import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class RegisterAPIView(generics.CreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=RegisterSerializer

class LoginView(generics.GenericAPIView):
    def post(self,request,*args,**kwargs):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(username=username,password=password)
        if user:
            refresh=RefreshToken.for_user(user)
            return Response({
                'refresh':str(refresh),
                'access':str(refresh.access_token),
            })
        return Response({'Message':'Invalid Credential'},status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=ProfileSerializer

    def get_object(self):
        return self.request.user