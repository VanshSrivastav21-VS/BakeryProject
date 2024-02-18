# Generated by Django 4.2.7 on 2024-02-18 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0005_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]