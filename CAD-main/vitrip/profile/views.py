from django.shortcuts import render
from .models import Student
# Create your views here.
def profile(request):
    stu1 = Student()
    stu1.name = "Aarjav"
    stu1.regno = "22BCT0104"
    stu1.hostel = "M block"
    stu1.email = "aarav.jain2022@vitstudent.ac.in"
    stu1.phone = 8610748057
    return render(request, "profile.html", {'stu': stu1})
