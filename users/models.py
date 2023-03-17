from django.db import models
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class profileModel(models.Model):
    users = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.users.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created: 
        if created:
            profileModel.objects.create(users=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profilemodel.save()
