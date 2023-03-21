from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # add additional fields in here
    name = models.CharField(null=True, blank=True, max_length=100)