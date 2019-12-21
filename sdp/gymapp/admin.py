from django.contrib import admin
from .models import GymMember, GymClasses, GymTrainer
# Register your models here.

admin.site.register(GymMember)
admin.site.register(GymTrainer)
admin.site.register(GymClasses)
