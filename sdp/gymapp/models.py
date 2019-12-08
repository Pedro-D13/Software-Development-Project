from django.db import models
from phone_field import PhoneField
# Create your models here.


titles = [
    ('mr', 'Mr'),
    ('mrs', 'Mrs'),
    ('ms', 'Ms'),
    ('miss', 'Miss'),
    ('dr', 'Dr')
]

genders = [
    ('M', 'Male'),
    ('F', 'Female')
]

membership_tiers = [
    ('G', 'Gold'),
    ('S', 'Silver'),
    ('B', 'Bronze'),
]


class GymMember(models.Model):
    ''' 
    Fields required to create gym members profile needed to create a gym member
        location, Membership Type, Title, Firstname, Lastname, Email, Mobile Number, Gender, DOB,
        Credit card Credientials
    '''
    title = models.CharField(choices=titles,
                             max_length=4)  # Choice field
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    mobile_number = PhoneField(
        blank=True, help_text="Contact Phone Number")  # Not required
    # Choice field or true or false
    gender = models.CharField(choices=genders, max_length=1)
    membership_tier = models.CharField(
        choices=membership_tiers, default='B', max_length=1)
