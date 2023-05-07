from django.urls import path
from .views import *

urlpatterns = [
    path('', Homepage, name="home"),
    path('about', About, name="about"),
    path('service', Allservice, name="allservice"),
    path('store', Store, name="store"),
    path('contact', Contact, name="contact"),
]
