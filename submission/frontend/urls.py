from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('login', index),
    path('register-nurse', index)
]