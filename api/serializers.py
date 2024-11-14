from rest_framework import serializers
from . models import CustomUser

# Registeration Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username','password','phone_number','date_of_birth']
        extra_kwargs={'password':{'write_only':True}}
    
    def create(self,validate_data):
        user=CustomUser.objects.create_user(**validate_data)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username','phone_number','date_of_birth','last_login_ip']


