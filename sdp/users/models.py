from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save


# Create your models here.
class GymProfile(models.Model):
    member = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="", upload_to="profile_pics")
