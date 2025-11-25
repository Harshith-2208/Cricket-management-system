from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('umpire', 'Umpire'),
        ('player', 'Player'),
    )

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='player'  
    )
