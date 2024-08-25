from django.contrib import admin
from .models import ContactInfo, NewsletterSubscription
# Register your models here.

@admin.register(ContactInfo)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_on')

@admin.register(NewsletterSubscription)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('email','subscribed_at')