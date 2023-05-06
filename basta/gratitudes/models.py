from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User


class Gratitude(models.Model):
    message = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    like_count = models.PositiveIntegerField(default=0)


class Like(models.Model):
    gratitude = models.ForeignKey(Gratitude, on_delete=models.CASCADE)


@receiver(post_save, sender=Like)
def increment_like_count(sender, instance, **kwargs):
    instance.gratitude.like_count += 1
    instance.gratitude.save()
