from django.db import models
from django.conf import settings
from .utils import get_random_code
from django.template.defaultfilters import slugify

# Create your models here.


class Employee(models.Model):

    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    avatar = models.ImageField(default='avatar.jpg', upload_to='avatars/')
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.CharField(max_length=200, null=True)
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    city = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    county = models.CharField(max_length=200, null=True)
    employment_status = models.CharField(max_length=200, null=True)
    fun_fact = models.CharField(max_length=200, null=True)
    achievement = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.user}-{self.date_created}"

    def saveit(self, *args, **kwargs):
        ex = False
        if self.name and self.last_name:
            to_slug = slugify(str(self.name) + " " + str(self.last_name))
            ex = Employee.objects.filter(slug=to_slug).exists()
            while ex:
                to_slug = slugify(to_slug + " " + str(get_random_code()))
                ex = Employee.objects.filter(slug=to_slug).exists()
        else:
            to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)


class Employer(models.Model):

    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name