from django.db import models
from django.conf import settings

from .utils import get_random_code
from django.template.defaultfilters import slugify


# Create your models here.


class Employee_Basics(models.Model):
    # basic info
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    city = models.CharField(max_length=200, null=True)
    county = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)

    role = models.CharField(max_length=200, null=True)
    sector = models.CharField(max_length=200, null=True)
    seeking_work = models.BooleanField(default=True)

    # media files
    avatar = models.ImageField(default='avatar.jpg', upload_to='avatars/')
    cover = models.ImageField(default='avatar.jpg', upload_to='covers/')
    # add video stuff
    # personal
    fun_fact = models.CharField(blank=True, max_length=2000, null=True)
    achievement = models.CharField(blank=True, max_length=2000, null=True)
    hobbies = models.CharField(blank=True, max_length=2000, null=True)
    favourite_quote = models.CharField(blank=True, max_length=2000, null=True)
    # job desires
    contract_length = models.CharField(blank=True, max_length=2000, null=True)
    remote_employee = models.BooleanField(blank=True, default=True)
    travel_distance = models.IntegerField(blank=True, null=True)
    # usercreation
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    # interaction
    liked = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='liked')
    # other
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    current_company = models.CharField(max_length=200, null=True)
    bio = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return f"{self.user}-{self.date_created.strftime('%d-%m-%Y')}"

    def get_liked(self):
        return self.liked.all()

    def get_liked_no(self):
        return self.liked.all().count()

    __initial_first_name = None
    __initial_last_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initial_first_name = self.first_name
        self.__initial_last_name = self.last_name

    def save(self, *args, **kwargs):
        ex = False
        to_slug = self.slug
        if self.first_name != self.__initial_first_name or self.last_name != self.__initial_last_name or self.slug == "":
            if self.first_name and self.last_name:
                to_slug = slugify(str(self.first_name) +
                                  " " + str(self.last_name))
                ex = Employee_Basics.objects.filter(slug=to_slug).exists()
                while ex:
                    to_slug = slugify(to_slug + " " + str(get_random_code()))
                    ex = Employee_Basics.objects.filter(slug=to_slug).exists()
            else:
                to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)

# class Employee_Personality(models.Model):


class Employee_Skills(models.Model):

    # create select list and then other option
    category_of_skill = models.CharField(max_length=200, null=True)
    name_of_skill = models.CharField(max_length=200, null=True)
    level_of_skill = models.CharField(max_length=200, null=True)
    years_of_experience = models.IntegerField(blank=True, null=True)


class Employee_Education(models.Model):
    education_title = models.CharField(max_length=200, null=True)
    education_level = models.CharField(max_length=200, null=True)
    subject = models.CharField(
        max_length=200, null=True)  # to be list with sections
    institution_name = models.CharField(max_length=200, null=True)


class Employee_Work_History(models.Model):
    company_under = models.CharField(max_length=200, null=True)
    role_name = models.CharField(max_length=200, null=True)
    # to be list with sections
    duration = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=2000, null=True)


class Employer_Basics(models.Model):
    # basics
    company_name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    sector = models.CharField(max_length=200, null=True)
    about = models.CharField(max_length=2000, null=True)
    culture = models. CharField(max_length=2000, null=True)
    city = models.CharField(max_length=200, null=True)
    county = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    # interaction
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, blank=True, related_name='followers')
    # media
    logo = models.ImageField(default='avatar.jpg', upload_to='avatars/')
    employer_cover = models.ImageField(
        default='avatar.jpg', upload_to='covers/')
    # other
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    slug2 = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f"{self.user}-{self.date_created.strftime('%d-%m-%Y')}"

    __initial_company_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initial_company_name = self.company_name

    def save2(self, *args, **kwargs):
        ex = False
        to_slug = self.slug2
        if self.company_name != self.__initial_company_name or self.slug2 == "":
            if self.company_name:
                to_slug = slugify(str(self.company_name) +
                                  " ")
                ex = Employer_Basics.objects.filter(slug=to_slug).exists()
                while ex:
                    to_slug = slugify(to_slug + " " + str(get_random_code()))
                    ex = Employer_Basics.objects.filter(slug2=to_slug).exists()
            else:
                to_slug = str(self.user)
        self.slug2 = to_slug
        super().save(*args, **kwargs)


STATUS_CHOICES = (
    ('Not following', 'Not following'),
    ('Following', 'Following')
)


class Follow_Employers(models.Model):
    sender = models.ForeignKey(
        Employee_Basics, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(
        Employer_Basics, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"
