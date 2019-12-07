from django.db import models

# Create your models here.


class User(models.Model):
    # BRZ = 'Bronze'
    # SLV = 'Silver'
    # GLD = 'Gold'
    #
    # membership_tiers = [
    #     (BRZ, 'Bronze'),
    #     (SLV, 'Silver'),
    #     (GLD, 'Gold'),
    # ]
    #
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    address = models.TextField()
    email = models.EmailField(max_length=50)
    # membership_tier = models.CharField(max_length = 10, choices=membership_tiers, default=BRZ)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
