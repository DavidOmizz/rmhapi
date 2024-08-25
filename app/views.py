from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import ContactInfo, NewsletterSubscription
from .serializers import ContactSerializer, NewsletterSubscriptionSerializer
from .utils import *

class ContactListCreateView(generics.ListCreateAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            # Send contact email
            send_contact_email(serializer.validated_data['email'], serializer.validated_data['name'])

            return Response({"message": "Thank you for your message."}, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewsletterSubscriptionListCreateView(generics.ListCreateAPIView):
    queryset = NewsletterSubscription.objects.all()
    serializer_class = NewsletterSubscriptionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            subscription = serializer.save()

            # Append the email to a .doc file
            with open('subscribers.doc', 'a') as file:
                file.write(f"{subscription.email}\n")
            
            # Send subscription email
            send_newsletter_subscription_email(serializer.validated_data['email'], subscription.email)

            headers = self.get_success_headers(serializer.data)
            return Response({"message": "Thank you for subscribing to our newsletter."}, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
