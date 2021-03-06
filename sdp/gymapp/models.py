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

class_options = [
    ('spin', 'Spinning'),
    ('bxng', 'Boxing'),
    ('LBT', 'Legs bums & tums'),
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
    gender = models.CharField(choices=genders, max_length=7)
    membership_tier = models.CharField(
        choices=membership_tiers, default='B', max_length=7)

    def __str__(self):
        return f"{self.title} {self.first_name}:{self.membership_tier}"


class GymTrainer(models.Model):
    title = models.CharField(choices=titles,
                             max_length=4)  # Choice field
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    gender = models.CharField(choices=genders, max_length=7)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} {self.first_name}"


class GymClasses(models.Model):
    class_title = models.CharField(choices=class_options, max_length=4)
    class_description = models.CharField(max_length=200)
    class_date = models.DateField(auto_now=False)
    class_time = models.TimeField(auto_now=False)
    class_instructor = models.ForeignKey(
        GymTrainer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.class_title}, @{self.class_date}:{self.class_time}"
