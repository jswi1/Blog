from django.urls import path
from .views import *

urlpatterns = [
    path('', blog),
    path('about/', about),
    path('maqola/', maqola),
]