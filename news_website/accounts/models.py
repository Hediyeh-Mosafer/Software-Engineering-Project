from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',  # جلوگیری از تداخل
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # جلوگیری از تداخل
        blank=True,
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        )
    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True,
        )
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('superuser', 'Superuser'),
        ('user', 'User'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
    