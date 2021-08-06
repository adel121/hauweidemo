from django.db import models

# Create your models here.


class Patient(models.Model):
	username = models.CharField(max_length = 1000, default = "no name")
	password = models.CharField(max_length = 1000, )
	country = models.CharField(max_length = 1000, default = "no country")
	gender = models.CharField(max_length=1, default = "M")



class Doctor(models.Model):
	username = models.CharField(max_length = 1000, default = "no name")
	password = models.CharField(max_length = 1000, )
	country = models.CharField(max_length = 1000, default = "no countrt")	
	gender = models.CharField(max_length=1, default = "M")


class Booking(models.Model):
	patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
	doctor = models.ForeignKey(Doctor,on_delete = models.CASCADE)
	date = models.DateTimeField('Booking Date', null=True, blank=True, default=None)


class Patient_Post(models.Model):
	title = models.CharField(max_length=30, default="no title")
	content = models.CharField(max_length=10000, default="empty post")
	patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
	date = models.DateTimeField('Post Date', null=True, blank=True, default=None)


class Doctor_Post(models.Model):
	title = models.CharField(max_length=30, default="no title")
	content = models.CharField(max_length=10000, default="empty post")
	doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
	date = models.DateTimeField('Post Date', null=True, blank=True, default=None)



