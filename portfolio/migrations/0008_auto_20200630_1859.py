# Generated by Django 3.0 on 2020-06-30 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20200629_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='art',
            field=models.FileField(upload_to='artworks/%Y'),
        ),
    ]
