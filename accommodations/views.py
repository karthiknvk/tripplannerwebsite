from django.shortcuts import render
from users.models import CustomUser
from .models import Accommodationdetailstable
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
'''
def accommodationloginview(request):
  global user
  global accommodation
  user=request.user
  print("user->",user)
  accommodationdetailslist=Accommodationdetailstable.objects.filter(user=user).values()
  print('accommodationdetailslist->',accommodationdetailslist)
  accommodation=list(accommodationdetailslist)
  print("accommodation->", accommodation)
  for i in accommodation:
    print('id->',i)
    print('\nname->',i.name,"\n")
  if accommodationdetailslist:
    print("accommodation2nd time->", accommodation)
    print("user have entered details in table")
    return accommodationaccountview(request)
  else:
    print("user have not entered details in table")
    return accommodationformview(request)
  
'''
@login_required
def accommodationloginview(request):
  global user_profile
  global accommodation
  user_profile=request.user
  if Accommodationdetailstable.objects.filter(user=user_profile).exists():
    accommodation=Accommodationdetailstable.objects.get(user=user_profile)
    #print("currentuser->", user_profile)
    #print("accommodation->", accommodation)
    print("user have entered details in table")
    return accommodationaccountview(request)
  else:
    #print("currentuser->", user_profile)
    print("user have not entered details in table")
    return accommodationformview(request)
    
@login_required  
def accommodationformview(request):
  user_profile=request.user
  global accommodation
  if request.method == "POST":
    print("entered into IF statement")
    name=request.POST.get("accommodation_name")
    accommodation_district=request.POST.get("accommodation_district")
    accommodation_location=request.POST.get("accommodation_location")
    accommodation_lowest_price=request.POST.get("accommodation_lowest_price")
    accommodation_highest_price=request.POST.get("accommodation_highest_price")
    accommodation_restaurant = request.POST.get('accommodation_restaurant')
    image1 = request.FILES.get('accommodation_image1')
    image2 = request.FILES.get('accommodation_image2')
    if accommodation_restaurant is not None and accommodation_restaurant=='on':
      restaurant=True
    else:
      restaurant=False
    #print(name,accommodation_district,accommodation_location,accommodation_lowest_price,accommodation_highest_price,accommodation_restaurant,image1,image2)
    accommodation=Accommodationdetailstable(
            user=request.user,  # Assuming you are using authentication
            name=name,
            district=accommodation_district,
            location=accommodation_location,
            lowest_rate=accommodation_lowest_price,
            highest_rate=accommodation_highest_price,
            restaurant=restaurant,
            accommodation_image1=image1,
            accommodation_image2=image2,
    )
    accommodation.save()
    #print("accommodation user details saved succesfully")
    accommodation=Accommodationdetailstable.objects.get(user=user_profile)
    print("accommodation in if statement",accommodation)
    return render(request,"acco-profile.html",{'accommodation':accommodation,'user_profile':user_profile})
  elif Accommodationdetailstable.objects.filter(user=user_profile).exists():
    print("entered into ELIF statement")
    accommodation=Accommodationdetailstable.objects.get(user=user_profile)
    print("accommodation in ELIF",accommodation)
    return render(request,"pages-accommodation.html",{'accommodation':accommodation,'user_profile':user_profile})
  else:
    print("entered into ELSE statement")
    return render(request,"pages-accommodation.html",{'user_profile':user_profile})
  
@login_required 
def accommodationaccountview(request):
  #accommodationdetailslist=Accommodationdetailstable.objects.filter(user=user).all()
  global accommodation
  print("entered into ACCOMMODATIONVIEW function")
  return render(request, "acco-profile.html", {'accommodation': accommodation,'user_profile':user_profile})
  try:
      accommodation = Accommodationdetailstable.objects.get(user=user)
      print("accommodation->", accommodation)
      return render(request, "homeaccommodation.html", {'accommodation': accommodation})
  except Accommodationdetailstable.DoesNotExist:
      print("Accommodation details not found for this user.")
      return render(request, "homeaccommodation.html", {'accommodation': None})
  
@login_required  
def listofaccommodationsview(request,district):
  accommodation_district = district
  user_profile=request.user
  accommodationdetailsdict=dict()
  accommodationdetailslist=Accommodationdetailstable.objects.filter(district=accommodation_district).all()
  number=0
  for accommodationcenter in accommodationdetailslist:
    number=number+1
    accommodationkey="Accommodation"+str(number)
    accommodationdetailstempdict=[
        accommodationcenter.name,                 #0
        accommodationcenter.district,             #1  
        accommodationcenter.location,             #2
        accommodationcenter.lowest_rate,          #3
        accommodationcenter.highest_rate,         #4
        accommodationcenter.accommodation_image1, #5
        accommodationcenter.accommodation_image2, #6
        accommodationcenter.restaurant,           #7
    ]
    accommodationdetailsdict[accommodationkey]=accommodationdetailstempdict
  print("accommodationdetailsdict",accommodationdetailsdict)
  #accommodationlist=Tourpackage.objects.filter(district=destination,packagecategory=day)
  return render(request,"acco-list.html",{'accommodation_district':accommodation_district,'user_profile':user_profile,'accommodationdetailsdict':accommodationdetailsdict})

'''
name=request.POST["name"]
    district=request.POST["district"]
    location=request.POST["location"]
    lowest_rate=request.POST["lowest_rate"]
    highest_rate=request.POST["highest_rate"]
    restaurant = request.POST.get('restaurant')
    image1 = request.FILES.get('image1')
    image2 = request.FILES.get('image2')
'''