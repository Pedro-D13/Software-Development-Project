from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import (GymLocationSelection, GymMembershipSelection,
                    GymMemberUpdateForm, GymMemberShipRegisterForm)

# Create your views here.


def register(request):
    if request.method == "POST":
        user_form = GymMemberShipRegisterForm(request.POST)
        location_form = GymLocationSelection(request.POST)
        membership_form = GymMembershipSelection(request.POST)
        if user_form.is_valid() and location_form.is_valid() & membership_form.is_valid():
            user_form.save()
            location_form.save()
            membership_form.save()
            username = user_form.cleaned_data.get('username')
            location = location_form.cleaned_data.get('location')
            membership = membership_form.cleaned_date_get('membership_tier ')
            messages.success(
                request, f"Your account has been created! for {username} {membership} @ {location} you  are now able to login")
            return redirect("login")
    else:
        form = GymMemberShipRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def location(request):
    if request.method == "POST":
        form = GymLocationSelection(request.POST)

        if form.is_valid():
            form.save()
            location = form.cleaned_data.get('location')
