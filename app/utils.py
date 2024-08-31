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


# def send_internal_email(contact_info):
#     # Email subject and message
#     subject = f"New Contact Form Submission from {contact_info['name']}"
#     plain_message = f"""
#     Name: {contact_info['name']}
#     Email: {contact_info['email']}
#     Number: {contact_info.get('number', 'N/A')}
#     Message: {contact_info['message']}
#     """
    
#     # Send to your own email
#     email = EmailMultiAlternatives(
#         subject,
#         plain_message,
#         settings.EMAIL_HOST_USER,
#         [settings.EMAIL_HOST_USER]  # Your email address
#     )

#     # Send the email
#     email.send(fail_silently=False)

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

def send_internal_newsletter_subscription_email(email_info):
    subject = 'New Newsletter Subscription!'
    plain_message = f"A new newsletter subscription has been received:\n\nEmail: {email_info['email']}\n"
    
    # Render the HTML template for the internal email
    html_message = render_to_string('emails/internal_newsletter_subscription_email.html', {'email_info': email_info})
    
    # Send the email to your own email
    email = EmailMultiAlternatives(
        subject,
        plain_message,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER]  # Your email address
    )
    
    # Attach the HTML version of the message
    email.attach_alternative(html_message, "text/html")
    
    # Send the email
    email.send(fail_silently=False)
    


def send_internal_email(contact_info):
    subject = f"New Contact Form Submission from {contact_info['name']}"
    
    # Render the HTML template for the internal email
    html_message = render_to_string('emails/internal_contact_email.html', {'contact_info': contact_info})
    plain_message = f"""
    Name: {contact_info['name']}
    Email: {contact_info['email']}
    Number: {contact_info.get('number', 'N/A')}
    Message: {contact_info['message']}
    """

    # Send the email to yourself
    email = EmailMultiAlternatives(
        subject,
        plain_message,
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER]  # Your email address
    )

    # Attach the HTML version of the message
    email.attach_alternative(html_message, "text/html")

    # Send the email
    email.send(fail_silently=False)