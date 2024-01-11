from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def addreview(request):
  user_profile=request.user
  return render(request,'pages-review.html',{'user_profile':user_profile})

@login_required
def addspot(request):
  user_profile=request.user
  return render(request,'pages-add-spot.html',{'user_profile':user_profile})

def showreview(request):
  pass