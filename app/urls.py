from django.urls import path
from .views import ContactListCreateView, NewsletterSubscriptionListCreateView

urlpatterns = [
    path('api/contact/', ContactListCreateView.as_view(), name='api-contact'),
    path('api/subscribe/', NewsletterSubscriptionListCreateView.as_view(), name='api-subscribe'),
]
