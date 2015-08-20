from django.db import models
from django.core.validators import RegexValidator

class Registration(models.Model):

    name = models.CharField(max_length=200, null=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: "
                                                                   "'+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True, null=False) # validators should be a list
    email = models.EmailField(null=False)
    remarks = models.CharField(max_length=2000)
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)
