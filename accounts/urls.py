from django.urls import path, include
from .views import UserRegister

urlpatterns = [
    path('registration/', UserRegister.as_view(), name='user-registration'),
]