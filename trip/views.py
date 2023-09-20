from django.shortcuts import render

# Create your views here.


def tripinfo(request):
    return render(request, 'tripinfo.html')
