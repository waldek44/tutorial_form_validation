
from django.urls import path

from . import views

urlpatterns = [
    path('formularz', views.home, name='index'),
]
