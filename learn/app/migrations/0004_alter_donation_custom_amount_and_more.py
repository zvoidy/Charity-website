# Generated by Django 5.0.2 on 2024-03-01 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='custom_amount',
            field=models.CharField(default='none'),
        ),
        migrations.AlterField(
            model_name='donation',
            name='donation_amount',
            field=models.CharField(default='none'),
        ),
    ]
