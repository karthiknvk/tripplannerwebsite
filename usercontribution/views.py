from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review,Newspot
from packages.models import Destination
# Create your views here.

spotreviewdetailsdict=dict()

@login_required
def addreview(request):
  #print("entered addreview function succesfully")
  user_profile=request.user
  if request.method=="POST":
    spotdistrict=request.POST.get('spotdistrict')
    spotname2=request.POST.get('spotname')
    content=request.POST.get('content')
    review_image1=request.FILES.get('review_image1')
    review_image2=request.FILES.get('review_image2')
    #print("deatils colected succesfully")

    spotname_obj=Destination.objects.get(spotname=spotname2)
    review=Review(
      user=request.user,  # for user
      spotname=spotname_obj,
      spotdistrict=spotdistrict,
      content=content,
      review_image1=review_image1,
      review_image2=review_image2,
    )
    review.save()
    #print("review add succesfully by ",user_profile)
    #print("review_spotname in add review",review_spotname)
    #print("spotreviewdetailsdict in add review",spotreviewdetailsdict)
    return render(request,'spot-review.html',{'user_profile':user_profile,'review_spotname':review_spotname,'spotreviewdetailsdict':spotreviewdetailsdict})

@login_required
def reviewpage(request,):
  user_profile=request.user
  global spotreviewdetailsdict
  global review_spotname
  if request.method=="POST":
    review_spotname=request.POST.get('spotname')
    spotreviewdetailslist=Destination.objects.get(spotname=review_spotname)
    spotreviewdetailsdict.clear()
    spotreviewdetailsdict={
        'spotname':spotreviewdetailslist.spotname,
        'spotdistrict':spotreviewdetailslist.spotdistrict,
        'location':spotreviewdetailslist.location,
    }
    #print("spotname in reviewpage",review_spotname)
    #print("spotreviewdetailsdict in reviewpage",spotreviewdetailsdict)
  return render(request,'spot-review.html',{'user_profile':user_profile,'review_spotname':review_spotname,'spotreviewdetailsdict':spotreviewdetailsdict})

@login_required
def reviewpage2(request,review_spotname_copy):
  #print("review_spotname in add review2",review_spotname_copy)
  global spotreviewdetailsdict
  global review_spotname
  review_spotname=review_spotname_copy
  spotreviewdetailsdict = {}
  user_profile=request.user
  spotreviewdetailslist=Destination.objects.get(spotname=review_spotname)
  spotreviewdetailsdict.clear()
  spotreviewdetailsdict={
        'spotname':spotreviewdetailslist.spotname,
        'spotdistrict':spotreviewdetailslist.spotdistrict,
        'location':spotreviewdetailslist.location,
  }
  #print("spotname in reviewpage2",review_spotname)
  #print("spotreviewdetailsdict in reviewpage2",spotreviewdetailsdict)
  return render(request,'spot-review.html',{'user_profile':user_profile,'review_spotname':review_spotname,'spotreviewdetailsdict':spotreviewdetailsdict})

@login_required
def addspot(request):
  user_profile=request.user
  if request.method=="POST":
    newspotname=request.POST.get("newspotname")
    newspotdistrict=request.POST.get("newspotdistrict")
    newspotlocation=request.POST.get("newspotlocation")
    newspotcontent=request.POST.get("newspotcontent")
    newspotimage1=request.FILES.get("newspotimage1")
    newspotimage2=request.FILES.get("newspotimage2")
    newspotimage3=request.FILES.get("newspotimage3")
    print("newspotimage1=",newspotimage1)
    print("newspotimage2=",newspotimage2)
    print("newspotimage3=",newspotimage3)

    if newspotimage1==None and newspotimage2==None and newspotimage3==None:
      print("it can't be empty")
      messages.error(request, 'Atleast add one image')
      
    else:
      newspot=Newspot(
        user=request.user,
        spotname=newspotname,
        district=newspotdistrict,
        location=newspotlocation,
        description=newspotcontent,
        new_spot_image1=newspotimage1,
        new_spot_image2=newspotimage2,
        new_spot_image3=newspotimage3,
      )
      newspot.save()
      print("spot added succesfully by",user_profile)
      messages.success(request, 'Spot added succesfully')
    django_messages = messages.get_messages(request)
    return render(request,'pages-add-spot.html',{'user_profile':user_profile,'django_messages': django_messages})

  else:
    django_messages = messages.get_messages(request)
    return render(request,'pages-add-spot.html',{'user_profile':user_profile,'django_messages': django_messages})

@login_required
def showreview(request):
  pass