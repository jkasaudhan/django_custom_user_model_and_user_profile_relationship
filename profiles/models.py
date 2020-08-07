from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=150)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

class CandidateProfileManager(models.Manager):
    def filter_by_address(self, address):
        return self.filter(address__icontains=address)

class CandidateProfileModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile', on_delete=models.CASCADE)
    address = models.CharField(max_length=300)
    skills = models.CharField(max_length=200)
    objects = CandidateProfileManager()

    def __str__(self):
        return self.user.email