from django.contrib import admin
from .models import GymMember
# Register your models here.


class GymMembers(admin.StackedInline):
    model = GymMember
    can_delete = False
    verbose_name = "Gym Members"


admin.site.register(GymMember)
