from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
locations = ['london', 'manchester', 'kent', 'norwich']
membership_tiers = ['Bronze', 'Silver', 'Gold']


class GymLocationSelection(forms.ChoiceField):
    location = forms.ChoiceField(choices=locations)


class GymMembershipSelection(forms.ChoiceField):
    membership_tier = forms.ChoiceField(choices=membership_tiers)


class GymMemberShipRegisterForm(UserCreationForm):
    # class used to create new users, they are able to sign up
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2', ]


class GymMemberUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', ]
