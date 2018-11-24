from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


# UserProfile Model , which is created when a User Account is created due to post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shortbio = models.TextField(max_length=183, default="Your bio is not updated.Please update it")
    interests = models.CharField(max_length=80, default="Interests are not updated.Please add your Interests")
    image = models.ImageField(upload_to='profile_image', default=None, blank="True")

    def __str__(self):
        return self.user.username

    # Signals Code , post_save

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            return UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)


