from django.contrib import admin
from .models import Destination,Onedaypackage,Twodaypackage,Threedaypackage,Fourdaypackage,Fivedaypackage,Sixdaypackage,Sevendaypackage,Tourpackage

# Register your models here.

admin.site.register(Destination)
admin.site.register(Tourpackage)