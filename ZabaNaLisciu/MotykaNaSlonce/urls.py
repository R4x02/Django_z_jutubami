from django.urls import path
from .views import glowica

urlpatterns = [
    path("", glowica)
]