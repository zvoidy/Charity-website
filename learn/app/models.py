from django.db import models


# Create your models here.
class Donation(models.Model):
    donation_frequency = models.CharField(max_length=10)
    donation_amount = models.CharField(default='none')
    custom_amount = models.CharField(default='none')
    donor_name = models.CharField(max_length=100)
    donor_email = models.EmailField()
    payment_method = models.CharField(max_length=20)

class con(models.Model):
    First_name=models.CharField(max_length=10)
    Second_name=models.CharField(max_length=10)
    user_mail=models.EmailField()
    comment=models.TextField(max_length=30)

class Volunteer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    cv = models.FileField( upload_to='volunteer_cvs/',null=False, blank=False)
    message = models.TextField(blank=True)

class form(models.Model):
    email=models.EmailField(max_length=255)