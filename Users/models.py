from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_image = models.ImageField(default='user.png', upload_to='profile_images')
    location = models.CharField(max_length=1000)


def __str__(self):
    return self.user.username
