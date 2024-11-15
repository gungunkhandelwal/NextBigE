from rest_framework import serializers
from . models import CustomUser
from django.contrib.auth import authenticate

# Registeration Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username','password','phone_number','date_of_birth']
        extra_kwargs={'password':{'write_only':True}}
    
    def create(self,validate_data):
        user=CustomUser.objects.create_user(**validate_data)
        return user

# Login serializer and check if it is authenticated 
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)

    def validate(self, data):
        username=data.get('username')
        password=data.get('password')
        user=authenticate(username=username,password=password)
        if user is None:
            raise serializers.ValidationError("Invalid Credentials")
        data['user']=user
        return data 


# Serializing all detail of user
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username','phone_number','date_of_birth','last_login_ip']


