from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

phone_number_validator = RegexValidator(
    r'^[6-9]\d{9}$', 
    'Enter a valid Indian phone number'
)

class CustomUser(AbstractUser):
    phone_number=models.CharField(max_length=10,validators=[phone_number_validator],unique=True)
    date_of_birth=models.DateField( null=True,blank=True)
    last_login_ip=models.GenericIPAddressField(null=True,blank=True)

    def __str__(self):
        return self.username
