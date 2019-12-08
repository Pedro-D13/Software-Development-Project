from django.db import models
from phone_field import PhoneField
# Create your models here.


class GymMember(models.Model):
    ''' 
    Fields required to create gym members profile needed to create a gym member
        location, Membership Type, Title, Firstname, Lastname, Email, Mobile Number, Gender, DOB,
        Credit card Credientials
    '''
    title = pass  # Choice field
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    mobile_number = PhoneField(
        blank=True, help_text="Contact Phone Number")  # Not required
    gender = pass  # Choice field or true or false
