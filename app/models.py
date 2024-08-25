from django.db import models

class ContactInfo(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    number = models.CharField(max_length=15,blank=True, null=True)
    message = models.CharField(max_length=2000)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email