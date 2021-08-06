from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
	return render(request,'index.html')

def doctors(request):
	doctors = Doctor.objects.all()
	return render(request,'doctors.html', {'doctors':doctors})