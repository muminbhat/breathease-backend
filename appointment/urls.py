from django.urls import path
from .views import post_create_contact
urlpatterns = [
    path('post/', post_create_contact, name='post-contact'),
]