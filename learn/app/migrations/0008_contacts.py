# Generated by Django 5.0.2 on 2024-03-01 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_delete_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=10)),
                ('Second_name', models.CharField(max_length=10)),
                ('user_mail', models.EmailField(max_length=254)),
                ('comment', models.TextField(max_length=30)),
            ],
        ),
    ]
