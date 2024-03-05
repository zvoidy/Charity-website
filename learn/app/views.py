from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import yagmail
import os

# Create your views here.
def home(request):
    return render(request,'index.html')
def donate(request):
    return render(request, 'donate.html')
def detail(request):
    return render(request, 'news-detail.html')
def news(request):
    return render(request, 'news.html') 

def donation_submit(request):
    if request.method=="POST":
        donation_frequency = request.POST.get('DonationFrequency')
        donation_amount = request.POST.get('flexRadioDefault')
        custom_amount = request.POST.get('custom_amount')
        donor_name = request.POST.get('donation-name')
        donor_email = request.POST.get('donation-email')
        payment_method = request.POST.get('DonationPayment')

        Donation.objects.create(
        donation_frequency=donation_frequency,
        donation_amount=donation_amount,
        custom_amount=custom_amount,
        donor_name=donor_name,
        donor_email=donor_email,
        payment_method=payment_method)

        send_donation_thank_you_email(donor_email,donor_name,donation_amount)

        return render(request, 'success.html')


def send_donation_thank_you_email(donor_email, donor_name, donation_amount):
    subject = 'Thank You for Your Donation😊'
    organization_name = "Kind Heard Charity"
    your_name = "Hari Prashanth S"
    your_title = "KHC MD"
    contact_information = "hahahaharitwo@gmail.com"

    # Format the email body
    body = f"""
    Subject: Heartfelt Thanks for Your Generous Donation

    Dear,
        I trust this email finds you well💝. On behalf of {organization_name}, I want to express our sincere gratitude for your incredibly generous donation.
    Your support means a lot to us, and it will make a significant impact. Your willingness to contribute to our mission is truly inspiring, and we are honored to have you as a supporter.
    Your donation will surely help them all, and it brings us one step closer to achieving our goals.
    We value your commitment to making a positive change, and we assure you that every penny will be used judiciously to help the needy.
    Once again, thank you, {donor_name}, for your kindness and generosity. We are grateful for individuals like you who make a difference in the lives of those we serve.
    If you have any questions or would like more information about our initiatives, please feel free to reach out. We look forward to keeping you updated on the progress we make, thanks to your support.

    Wishing you all the best,

    {your_name}
    {your_title}
    {organization_name}
    {contact_information}
    """
    
    gmail_username='hahahaharitwo@gmail.com'
    sender_name='Hari'

    yag = yagmail.SMTP('hahahaharitwo@gmail.com', 'ajre miny mftv emza')
    yag.send(to=donor_email, subject=subject, contents=body, headers = {'From': f'{sender_name} <{gmail_username}>'})
    yag.close()


def contacts(request):
        if request.method=='POST':
            first_name=request.POST.get('first-name')
            second_name=request.POST.get('last-name')
            User_mail=request.POST.get('email')
            Comment=request.POST.get('message')

        con.objects.create(
        First_name=first_name,
        Second_name=second_name,
        user_mail=User_mail,
        comment=Comment,
        )

        send_contact(first_name,User_mail)

        return render(request, 'success.html')

def send_contact(first_name,User_mail):
    subject = 'Contact from KHC😊'
    organization_name = "Kind Heard Charity"
    your_name = "Hari Prashanth S"
    your_title = "KHC MD"
    contact_information = "hahahaharitwo@gmail.com"

    # Format the email body
    body = f"""
    Dear {first_name},
        Hey there, hope you are doing fine. We will contact you soon.
        
    Wishing you all the best,

    {your_name}
    {your_title}
    {organization_name}
    {contact_information}
    """
    
    gmail_username='hahahaharitwo@gmail.com'
    sender_name='Hari'

    yag = yagmail.SMTP('hahahaharitwo@gmail.com', 'ajre miny mftv emza')
    yag.send(to=User_mail, subject=subject, contents=body, headers = {'From': f'{sender_name} <{gmail_username}>'})
    yag.close()


def volunteer_signup(request):
    if request.method=='POST':
        name=request.POST.get('volunteer-name')
        email=request.POST.get('volunteer-email')
        subject=request.POST.get('volunteer-subject')
        cv_file = request.FILES.get('volunteer-cv')
        message =request.POST.get('volunteer-message')

        existing_volunteer = Volunteer.objects.filter(email=email).first()

        if existing_volunteer:
            # Volunteer with the same email already exists
            return render(request, 'error.html', {'message': 'Volunteer with this email already exists.'})

        Volunteer.objects.create(
            name=name,
            email=email,
            subject=subject,
            cv=cv_file,
            message=message,
        )

        Volun(name,email)

        return render(request, 'success.html')
    
def Volun(name,email):
    subject = 'Volunteer from KHC😊'
    organization_name = "Kind Heard Charity"
    your_name = "Hari Prashanth S"
    your_title = "KHC MD"
    contact_information = "hahahaharitwo@gmail.com"

    # Format the email body
    body = f"""
    Dear {name},
        Hey there, we are happy that you wanted to join as a volunteer in our charity. We will contact you soon.
        
    Wishing you all the best,

    {your_name}
    {your_title}
    {organization_name}
    {contact_information}
    """
    
    gmail_username='hahahaharitwo@gmail.com'
    sender_name='Hari'

    yag = yagmail.SMTP('hahahaharitwo@gmail.com', 'ajre miny mftv emza')
    yag.send(to=email, subject=subject, contents=body, headers = {'From': f'{sender_name} <{gmail_username}>'})
    yag.close()

def news_form(request):
    if request.method=='POST':
        email=request.POST.get('subscribe-email')

        form.objects.create(
            email=email,
        )

        news_form_mail(email)

        return render(request, 'success.html')
    
import yagmail

def news_form_mail(email):
    subject = 'News form from KHC😊'
    organization_name = "Kind Heard Charity"
    your_name = "Hari Prashanth S"
    your_title = "KHC MD"
    contact_information = "hahahaharitwo@gmail.com"

    # Format the email body
    body = f"""
    Dear,
    Hey there, we are happy that you wanted our news form of charity. The file is attached below.

    Wishing you all the best,

    {your_name}
    {your_title}
    {organization_name}
    {contact_information}
    """
    
    gmail_username = 'hahahaharitwo@gmail.com'
    sender_name = 'Hari'

    yag = yagmail.SMTP('hahahaharitwo@gmail.com', 'ajre miny mftv emza')
    
    # Correct the file path and use a raw string or double backslashes
    file_path = r'D:\DJ\learn\media\DJ_notes.txt'

    # Pass the file path as a list, even if it's a single file
    yag.send(
        to=email,
        subject=subject,
        contents=body,
        headers={'From': f'{sender_name} <{gmail_username}>'},
        attachments=[file_path],
    )

    yag.close()