from django.db import models
from django.contrib.auth.models import AbstractUser

class RoleChoices(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    GENERAL = 'general', 'General User'




class User(AbstractUser):
    email = None 
    role = models.CharField(max_length=50, choices=RoleChoices.choices, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.username
