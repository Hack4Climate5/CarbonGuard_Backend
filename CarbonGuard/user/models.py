from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    username = models.CharField(max_length=32, unique=True)
    phone_number = PhoneNumberField(unique=True)
    email = models.EmailField(unique=True)
    date_created = models.DateTimeField(timezone.now(), null=True)
    date_updated = models.DateTimeField(timezone.now(), null=True)

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
