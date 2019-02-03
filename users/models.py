from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=1000)
    def __str__(self):
        return f'{self.user.username} Profile'




'''
from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser

class UserProfile(AbstractBaseUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=16,null=True)
    company = models.CharField(max_length=50,null=True)
    username = models.CharField(max_length=100, unique=True , null=True)
    USERNAME_FIELD = User.username

'''
