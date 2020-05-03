# Generated by Django 3.0 on 2020-05-03 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20200503_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='about_photo_name',
            field=models.CharField(blank=True, error_messages={'unique': 'Another profile photo with this name already exists.'}, max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='about',
            name='current_photo',
            field=models.CharField(blank=True, choices=[('enabled', 'enabled')], error_messages={'unique': 'Another photo is already enabled as about-me photo.'}, max_length=7, null=True, unique=True),
        ),
    ]
