from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Patient_Post)
admin.site.register(Doctor_Post)
admin.site.register(Booking)
