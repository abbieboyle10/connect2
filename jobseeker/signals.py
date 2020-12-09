from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_create_employee_profile(sender, instance, created, **kwargs):
    print('sender', sender)
    print('instance', sender)
    if created:
        Employee_Basics.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def post_save_create_employer_profile(sender, instance, created, **kwargs):
    print('sender', sender)
    print('instance', sender)
    if created:
        Employer_Basics.objects.create(user=instance)


@receiver(post_save, sender=Follow_Employers)
def post_save_add_to_following(sender, instance, created, **kwargs):
    sender_ = instance.sender
    receiver_ = instance.receiver
    if instance.status == 'following':
        sender_.liked.add(receiver_.user)
        receiver_.followers.add(receiver_.user)
        sender_.save()
        sender_.save()
