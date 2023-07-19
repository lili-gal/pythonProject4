from django.contrib import admin
from django.urls import path

from catalog.views import home, contacts

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts)
]
