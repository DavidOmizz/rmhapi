from rest_framework import serializers
from .models import ContactInfo, NewsletterSubscription

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = ['id', 'name','number', 'email', 'message', 'created_on']

class NewsletterSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterSubscription
        fields = ['id', 'email', 'subscribed_at']
