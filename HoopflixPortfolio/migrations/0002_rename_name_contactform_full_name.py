# Generated by Django 5.0.6 on 2024-07-06 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HoopflixPortfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='Name',
            new_name='Full_Name',
        ),
    ]
