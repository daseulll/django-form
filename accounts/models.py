from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models

phone_number_validator = RegexValidator(r'^010[1-9]\d{7}$')

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11, validators=[phone_number_validator])    
