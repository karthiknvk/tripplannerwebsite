from django.shortcuts import render
from users.models import CustomUser
from .models import Accommodationdetailstable
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

def accommodationloginview(request):
  global user
  global accommodation
  user=request.user
  if Accommodationdetailstable.objects.filter(user=user).exists():
    accommodation=Accommodationdetailstable.objects.get(user=user)
    print("accommodation->", accommodation)
    print("user have entered details in table")
    return accommodationaccountview(request)
  else:
    print("user have not entered details in table")
    return accommodationformview(request)
    
  
def accommodationformview(request):
  global accommodation
  if request.method == "POST":
    name=request.POST["name"]
    district=request.POST["district"]
    location=request.POST["location"]
    lowest_rate=request.POST["lowest_rate"]
    highest_rate=request.POST["highest_rate"]
    restaurant = request.POST.get('restaurant')
    image = request.FILES.get('image')
    if restaurant is not None and restaurant=='on':
      restaurant=True
    else:
      restaurant=False
    print(name,district,location,lowest_rate,highest_rate,restaurant,image)
    accommodation=Accommodationdetailstable(
            user=request.user,  # Assuming you are using authentication
            name=name,
            district=district,
            location=location,
            lowest_rate=lowest_rate,
            highest_rate=highest_rate,
            restaurant=restaurant,
            image=image,
    )
    accommodation.save()
    print("accommodation user details saved succesfully")
    accommodation=Accommodationdetailstable.objects.get(user=user)
    print(accommodation)
    return render(request,"homeaccommodation.html",{'accomodation':accommodation})
  else:
    return render(request,"indexaccommodation.html")
  
def accommodationaccountview(request):
  #accommodationdetailslist=Accommodationdetailstable.objects.filter(user=user).all()
  global accommodation
  return render(request, "homeaccommodation.html", {'accommodation': accommodation})
  try:
      accommodation = Accommodationdetailstable.objects.get(user=user)
      print("accommodation->", accommodation)
      return render(request, "homeaccommodation.html", {'accommodation': accommodation})
  except Accommodationdetailstable.DoesNotExist:
      print("Accommodation details not found for this user.")
      return render(request, "homeaccommodation.html", {'accommodation': None})
  
def listofaccommodationsview(request):
  if request.method == "POST":
    district = request.POST.get('district')
    #accommodationlist=Tourpackage.objects.filter(district=destination,packagecategory=day)
  return render(request,"accommodationdetails.html",{'district':district})