# Generated by Django 4.2.7 on 2024-02-18 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0004_userprofile_delete_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
