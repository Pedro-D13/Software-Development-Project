# Generated by Django 3.0 on 2019-12-08 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0003_remove_user_membership_tier'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]