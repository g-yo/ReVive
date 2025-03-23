from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import random
import string

def generate_random_password(length=10):
    """Generate a random password with specified length"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def send_registration_confirmation(user_email, username):
    """Send a confirmation email when a user registers"""
    subject = 'Welcome to Rehab Center - Registration Successful'
    html_message = render_to_string('email_templates/registration_confirmation.html', {
        'username': username,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [user_email],
        html_message=html_message,
        fail_silently=False,
    )

def send_application_confirmation(user_email, username, application_type):
    """Send a confirmation email when a user submits an application"""
    subject = 'Rehab Center - Application Submitted Successfully'
    html_message = render_to_string('email_templates/application_confirmation.html', {
        'username': username,
        'application_type': application_type,
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [user_email],
        html_message=html_message,
        fail_silently=False,
    )

def send_application_status_update(user_email, username, application_type, status, start_date=None):
    """Send an email when an application status is updated"""
    subject = f'Rehab Center - Application {status.capitalize()}'
    
    context = {
        'username': username,
        'application_type': application_type,
        'status': status,
    }
    
    if start_date and status == 'approved':
        context['start_date'] = start_date
    
    html_message = render_to_string('email_templates/application_status_update.html', context)
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [user_email],
        html_message=html_message,
        fail_silently=False,
    )

def send_staff_credentials(staff_email, staff_name, username, password):
    """Send login credentials to newly added staff"""
    subject = 'Rehab Center - Your Staff Account Details'
    html_message = render_to_string('email_templates/staff_credentials.html', {
        'staff_name': staff_name,
        'username': username,
        'password': password,
        'login_url': 'http://localhost:8000/login/',  # Update with your actual login URL
    })
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject,
        plain_message,
        settings.DEFAULT_FROM_EMAIL,
        [staff_email],
        html_message=html_message,
        fail_silently=False,
    )
