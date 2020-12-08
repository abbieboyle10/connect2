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

    email = models.CharField(max_length=200, null=True)
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    city = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    county = models.CharField(max_length=200, null=True)
    employment_status = models.CharField(max_length=200, null=True)
    fun_fact = models.CharField(max_length=200, null=True)
    achievement = models.CharField(max_length=200, null=True)

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}-{self.date_created}"

    __initial_first_name = None
    __initial_last_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initial_first_name = self.name
        self.__initial_last_name = self.last_name

    def save(self, *args, **kwargs):
        ex = False
        to_slug = self.slug
        if self.name != self.__initial_first_name or self.last_name != self.__initial_last_name or self.slug == "":
            if self.name and self.last_name:
                to_slug = slugify(str(self.name) +
                                  " " + str(self.last_name))
                ex = Employee.objects.filter(slug=to_slug).exists()
                while ex:
                    to_slug = slugify(to_slug + " " + str(get_random_code()))
                    ex = Employee.objects.filter(slug=to_slug).exists()
            else:
                to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)


class Employer(models.Model):

    company_name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=2000, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    logo = models.ImageField(default='avatar.jpg', upload_to='avatars/')
    city = models.CharField(max_length=200, null=True)
    county = models.CharField(max_length=200, null=True)
    sector = models.CharField(max_length=200, null=True)
    slug2 = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.user}-{self.date_created}"

    __initial_company_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initial_company_name = self.company_name

    def save(self, *args, **kwargs):
        ex = False
        to_slug = self.slug2
        if self.company_name != self.__initial_company_name or self.slug2 == "":
            if self.company_name:
                to_slug = slugify(str(self.company_name) +
                                  " ")
                ex = Employer.objects.filter(slug=to_slug).exists()
                while ex:
                    to_slug = slugify(to_slug + " " + str(get_random_code()))
                    ex = Employer.objects.filter(slug2=to_slug).exists()
            else:
                to_slug = str(self.user)
        self.slug2 = to_slug
        super().save(*args, **kwargs)
