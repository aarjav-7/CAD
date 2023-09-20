from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def clienthome(request):
    return render(request, 'clienthome.html')