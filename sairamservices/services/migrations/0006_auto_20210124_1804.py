# Generated by Django 3.1.5 on 2021-01-24 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_enquiry_slider'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name_plural': 'About Us'},
        ),
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name_plural': 'Contact Us'},
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name_plural': 'Settings'},
        ),
    ]
