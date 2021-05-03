from django.db import models
from django.conf import settings
from phone_field import PhoneField


class Profile(models.Model):
    GENDER = [
        ('L', 'Laki-laki'),
        ('P', 'Perempuan')
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birth_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, verbose_name="Gender", help_text="Jenis kelamin")
    phone_number = PhoneField(blank=True, verbose_name="Phone Number", help_text="Phone Number")
    mobile_number = models.CharField(max_length=12, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    terms_of_use = models.BooleanField(default=False)
