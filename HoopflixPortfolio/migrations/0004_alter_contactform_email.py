# Generated by Django 5.0.6 on 2024-07-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HoopflixPortfolio', '0003_rename_full_name_contactform_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
    ]
