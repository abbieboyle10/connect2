from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import Employee


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_create_profile(sender, instance, created, **kwargs):
    print('sender', sender)
    print('instance', sender)
    if created:
        Employee.objects.create(user=instance)
