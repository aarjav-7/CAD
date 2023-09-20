from django.urls import path
from . import views

urlpatterns = [
    path('', views.signuppage, name='signpage')
]