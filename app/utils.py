# utils.py

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def send_contact_email(to_email, user_name):
    subject = 'Thank You for Contacting Us!'
    plain_message = f"Hi {user_name},\n\nThank you for reaching out to us. We have received your message and will get back to you shortly.\n\nBest regards,\nReliance metal house"
    
    # Render the HTML template
    html_message = render_to_string('emails/contact_email.html', {'user_name': user_name})

    email = EmailMultiAlternatives(
        subject,
        plain_message,
        settings.EMAIL_HOST_USER,
        [to_email]
    )

    # Attach the HTML version of the message
    email.attach_alternative(html_message, "text/html")

    # Send the email
    email.send(fail_silently=False)

def send_newsletter_subscription_email(to_email, user_name):
    subject = 'Welcome to Our Newsletter!'
    plain_message = f"Hi {user_name},\n\nThank you for subscribing to our newsletter. Stay tuned for updates and news from us!\n\nBest regards,\nReliance metal house"
    
    # Render the HTML template
    html_message = render_to_string('emails/newsletter_subscription_email.html', {'user_name': user_name})

    email = EmailMultiAlternatives(
        subject,
        plain_message,
        settings.EMAIL_HOST_USER,
        [to_email]
    )

    # Attach the HTML version of the message
    email.attach_alternative(html_message, "text/html")

    # Send the email
    email.send(fail_silently=False)
