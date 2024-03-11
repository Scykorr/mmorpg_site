from django.urls import path, include
from .views import AccountProfile, UpdateProfile, auth_code


urlpatterns = [
    path('', include('allauth.urls')),
]
