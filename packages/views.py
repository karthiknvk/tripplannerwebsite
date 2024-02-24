from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from users.models import CustomUser
from accommodations.models import Accommodationdetailstable
from usercontribution.models import Review
from geopy.geocoders import ArcGIS,Nominatim
from geopy import distance
from django.conf import settings
from .models import Destination,Tourpackage
#import json
#from .utils import serialize_destination
#from django.http import JsonResponse
#from django.core.serializers import serialize



# Create your views here.

def logoutview(request):
    auth.logout(request)
    print("logged out")
    return redirect('/')

@login_required
def accountview(request):
    user_profile=request.user
    return render(request,'pages-profile.html',{'user_profile':user_profile})

def aboutview(request):
    user_profile=request.user
    return render(request,'pages-about.html',{'user_profile':user_profile})

@login_required
def home(request):
  user_profile=request.user
  if request.method=="POST":
    return packageview(request)
    
  else:
    #pricelist=['under 5000','5000-10000','10000-15000','above 15000']
    daylist={'1':'1daypackage','2':'2daypackage','3':'3daypackage','4':'4daypackage','5':'5daypackage','6':'6daypackage','7':'7daypackage'}
    destinationlist=['Kozhikode','Wayanad','Ernakulam','Thiruvananthapuram']
    return render(request,"pages-blank.html",{'daylist':daylist,'destinationlist':destinationlist,'user_profile':user_profile})
  

mainpackagedict=dict()
temppackagedict=dict()
mainpackagedictcopy=dict()
temppackagedictcopy=dict()
choosen_package_dict=dict()
#spotdetailsdict=dict()
@login_required
def packageview(request):
  global user_profile
  user_profile=request.user
  global day
  global destination
  global listoflandscapes
  listoflandscapes=['Beach','Temple','Mosque','Market','Pond','Shopping centre','Park','Museum','Waterfall','Reservoir','Dam','Amusement park','Planetarium','Tourist attractions','Cinema theatre','Bird watching area','Fort','Hill station','Zoo','Garden','Wildlife park','View point','Island','Water bodies','River','Church','Palace','Animal park']
  if 'itinerary' in request.POST:
      #print("package_details_list 1st time->", mainpackagedict)
      print("entering inside ITINERARYFORM in packageview if ")
      return itineraryview(request, mainpackagedict)
  elif 'filterform' in request.POST:
      #mainpackagedictcopy=dict()
      print("entering inside FILTERFORM in packageview elif1")
      return landscapefilter(request,mainpackagedictcopy,temppackagedictcopy,day)
  elif 'choiceform' in request.POST:
    print("entering inside CHOICEFORM in packageview elif2")
    day=request.POST.get('day')
    #print('day->',day)
    destination = request.POST.get('destination', '')
    mainpackagedict.clear()
    temppackagedict.clear()
    mainpackagelist=Tourpackage.objects.filter(district=destination,packagecategory=day).select_related('spotname').all() #to select all items fro tourpackage table where Tourpackage.spotname=Destination.spotname
    #print("\n")
    #print('mainpackagelist----->',mainpackagelist)
    mainspotnamelist=[]
    for package in mainpackagelist:
      number=str(package.packagenumber)
      count=package.district+number
      #print(count,"\n")
      key=count
      packagelist=[
                      package.id,                       #0
                      package.district,                 #1
                      package.packagenumber,            #2
                      package.daynumber,                #3
                      package.spottime,                 #4 
                      package.spotname,                 #5
                      package.spotname.location,        #6
                      package.spotname.landscape,       #7
                      package.spotname.cafespot,        #8
                      package.spotname.description,     #9
                      package.spotname.img,             #10
                      package.spotname.latitude,        #11
                      package.spotname.longitude,       #12
                      ]
      #print("packagelist->",packagelist,"\n")
      if key not in mainpackagedict:
        mainpackagedict[key]=[]
      mainpackagedict[key].append(packagelist)
      if key not in temppackagedict:
         temppackagedict[key]=[]
         temppackagedict[key].append(packagelist)
      else:
         continue
         
    '''
    print("*********mainpackagedict******")  
    for key in mainpackagedict:
      print(key,'->',mainpackagedict[key])
      print("\n")
    print("*********mainpackagedict******")  
    print("*********temppackagedict******")  
    for key in mainpackagedict:
      print(key,'->',temppackagedict[key])
      print("\n")
    print("*********temppackagedict******")  

    '''
    print("rendering tourpackages-html in packageview ELIF")
    print("destination:",destination)
      
    return render(request,'tour-packages.html',{'mainpackagedict':mainpackagedict,'day':day,'temppackagedict':temppackagedict,'user_profile':user_profile,'district':destination,'listoflandscapes':listoflandscapes},)
  
  else:
    '''
    print("\nin package view again")
    print("\nmainpackagedict:",mainpackagedict)
    print("\nmainpackagedictcopy:",mainpackagedictcopy)
    print("\ntemppackagedict",temppackagedict)
    print("\ntemppackagedictcopy",temppackagedictcopy)
    print("\nchoosen_package_dict",choosen_package_dict)

    '''
    print("entering inside packageview ELSE")
    print("rendering tourpackages-html in packageview ELSE")
    print("destination:",destination)
    return render(request,'tour-packages.html',{'mainpackagedict':mainpackagedict,'day':day,'temppackagedict':temppackagedict,'user_profile':user_profile,'district':destination,'listoflandscapes':listoflandscapes})

@login_required
def itineraryviewagain(request):
    print("entering inside itineraryviewagain ")
    print("rendering tourpackages-html in itineraryviewagain")
    print("destination:",destination)
    user_profile=request.user 
    #print("choosen package dict at itineraryviewagain->",choosen_package_dict)
    return render(request,'itinerary.html',{'choosen_package_dict':choosen_package_dict,'user_profile':user_profile,'district':destination,'listoflandscapes':listoflandscapes,'mainpackagedictcopy':mainpackagedictcopy,'mainpackagedict':mainpackagedict,})
  

@login_required
def itineraryview(request, mainpackagedict,):
    if request.method == "POST":
        print("entering inside itineraryview IF ")
        package_code = request.POST.get('package_code')
        #print("package_code->", package_code)
        global choosen_package_list
        #print("package_details_list2nd time->", mainpackagedict[package_code])
        choosen_package_list=mainpackagedict[package_code]
        print("***********************************************")
        print("choosen package list->",choosen_package_list)
        print("***********************************************")
        #print("choosen package list length->",len(choosen_package_list))
        no_of_days=len(choosen_package_list)//3
        choosen_package_dict.clear()
        inner_dict=dict()
        #print("choosen package list length divided by 3->",no_of_days)
        
        for inner_list in choosen_package_list:
          #print("choosen package dict now at top->",choosen_package_dict)
          #print("innerlist->",inner_list)
          time_key=inner_list[4]
          #print("time_key->",time_key)
          inner_dict[time_key]=inner_list
          #print("innerdictlength->",len(inner_dict))
          if len(inner_dict)<3:
            pass
            #print("inner_dict now->")
           # print("inner_dict now->",inner_dict)
            #continue
          else :
            #print("inner_dict now in else situation->",inner_dict)
            for i in range(1,no_of_days+1):
              #print(i)
              day_key='DAY'+str(i)
              #print("day_key->",day_key) 
              if day_key not in choosen_package_dict:
                #print("key not found")
                #print("ENTERED INSIDE")
                choosen_package_dict[day_key]=dict(inner_dict)
                #print("choosen package dict first->",choosen_package_dict)
                inner_dict.clear()
                break
              else:
                #print("key found,conitnuing to next")
                continue
              #problm 

    #print("choosen package dict at end->",choosen_package_dict)
    print("rendering tourpackages-html in itineraryview IF")
    print("destination:",destination)
    print("choosenpackagedict in itinerary view:",choosen_package_dict)
    return render(request,'itinerary.html',{'choosen_package_dict':choosen_package_dict,'user_profile':user_profile,'district':destination,'listoflandscapes':listoflandscapes,'mainpackagedictcopy':mainpackagedictcopy,'mainpackagedict':mainpackagedict,})

@login_required                 
def landscapeview(request):
   #global landscapelist
   print("entering inside landscapeview ")
   print("rendering tourpackages-html in landscapeview")
   print("destination:",destination)
   user_profile=request.user
   return render(request,'landscape-packages.html',{'mainpackagedictcopy':mainpackagedictcopy,'day':day,'landscapelist':landscapelist,'temppackagedictcopy':temppackagedictcopy,'mainpackagedict':mainpackagedict,'temppackagedict':temppackagedict,'user_profile':user_profile,'district':destination,'listoflandscapes':listoflandscapes})

@login_required
def landscapefilter(request,mainpackagedictcopy,temppackagedictcopy,day):
    if request.method == "POST":
      print("entering inside landscapefilter IF")
      global landscapelist
      landscapelist=request.POST.getlist('filter')
      #print(landscapelist)
      if not landscapelist:
         return redirect("packageview")
      #(request,'tour-packages.html',{'mainpackagedict':mainpackagedict,'day':day,'district':destination,'temppackagedict':temppackagedict},)
      else:
        mainpackagedictcopy.clear()
        temppackagedictcopy.clear()
        #print("landscapelist->",landscapelist)
        #print("\nDay->",day)
        #print('\nmainpackagedict->',mainpackagedict)
        #print('\nmainpackagedictcopy->',mainpackagedictcopy)
        '''
        for key,dictitems in mainpackagedict.items():
          print("item in each key")
          print(key,'->',dictitems)
          
        '''
        
        for item in landscapelist:
          for key,dictitems in mainpackagedict.items():
              if key not in mainpackagedictcopy:
                    for innerdictitems in dictitems:
                      if item in innerdictitems:
                          mainpackagedictcopy[key]=dictitems
                          for key,innerdictitems in mainpackagedictcopy.items():
                             #print("\nkey in maindictcopy",key)
                             #print("\ninnerdictitems in maindictcopy",innerdictitems)
                             for insideitems in innerdictitems:
                              #print("\ninsideitems:",insideitems)
                              if key not in temppackagedictcopy:
                                temppackagedictcopy[key]=[]
                                temppackagedictcopy[key].append(insideitems)
                              break
                              
                             
                             #print("\ninnerdictitems without list:",innerdictitems)
                             #innerdictitemslist=list(innerdictitems)
                             #
        '''
        print('\nmainpackagedict->',mainpackagedict)
        print('\ntemppackagedict->',temppackagedict)
        print('\nmainpackagedictcopy->',mainpackagedictcopy)
        print('\ntemppackagedictcopy->',temppackagedictcopy)
         
        '''               
        print("rendering tourpackages-html in landscapefilter IF")
        print("destination:",destination)
        return render(request,'landscape-packages.html',{'mainpackagedictcopy':mainpackagedictcopy,'day':day,'landscapelist':landscapelist,'temppackagedictcopy':temppackagedictcopy,'mainpackagedict':mainpackagedict,'temppackagedict':temppackagedict,'user_profile':user_profile,'district':destination,'listoflandscapes':listoflandscapes})

@login_required      
def spotdetailsview(request,spotname_copy,):
   print("entering inside spotdeatilsview")
   #print("spotdetailsview function spotname_copy",spotname_copy)
   global spotdetails_spotname
   spotdetails_spotname=spotname_copy
   user_profile=request.user
   #print("spot:",spotdetails_spotname)
   spotdetailslist=Destination.objects.get(spotname=spotdetails_spotname)
   spotdetailsdict=dict()
   spotdetailsdict={
      'spotname':spotdetailslist.spotname,
      'spotdistrict':spotdetailslist.spotdistrict,
      'location':spotdetailslist.location,
      'landscape':spotdetailslist.landscape,
      'cafespot':spotdetailslist.cafespot,
      'description':spotdetailslist.description,
      'img':spotdetailslist.img,
   }
   #print("selectedspot details of spotdetailsdict:",spotdetailsdict)
   
   spotdetails_spotdistrict=spotdetailsdict['spotdistrict']
   #print("selectedspot district:",spotdetails_spotdistrict)
   spotreviewdetailsdict=dict()
   spotdetails_spotname_instance = Destination.objects.get(spotname=spotdetails_spotname)
   spotreviewdetailslist=Review.objects.filter(spotname=spotdetails_spotname_instance,spotdistrict=spotdetails_spotdistrict).all()
   #mainpackagelist=Tourpackage.objects.filter(district=destination,packagecategory=day).select_related('spotname').all()
   #print("spotreviewdetailslist:",spotreviewdetailslist)
   number=0
   for review in spotreviewdetailslist:
      number=number+1
      reviewkey="Review"+str(number)
      reviewlist=[
                      review.id,            #0
                      review.user,          #1
                      review.spotname,      #2           
                      review.spotdistrict,  #3    
                      review.content,       #4
                      review.review_image1, #5    
                      review.review_image2, #6      
                      ]
      #print("reviewlist",reviewlist)
      spotreviewdetailsdict[reviewkey]=reviewlist
   #print("spotreviewdetailsdict",spotreviewdetailsdict) 
   #spotdetailsdict{}
   #selectedspot=request.GET.get('value')
   '''''
   print("selectedspot details:",spotdetailslist)
   print("selectedspot details of spotdetailsdict:",spotdetailsdict)
   print("\nmainpackagedict:",mainpackagedict)
   print("\nmainpackagedictcopy:",mainpackagedictcopy)
   print("\ntemppackagedict",temppackagedict)
   print("\ntemppackagedictcopy",temppackagedictcopy)
   print("\nchoosen_package_dict",choosen_package_dict)
   '''
   print("rendering tourpackages-html in spotdeatilsview")
   print("destination:",destination)
   print("selectedspot reviews :",spotreviewdetailsdict)
   return render(request,"itinerary-spot-details.html",{'spotdetails_spotname':spotdetails_spotname,'user_profile':user_profile,'spotdetailsdict':spotdetailsdict,'spotreviewdetailsdict':spotreviewdetailsdict,'district':destination})

def mapview(request,day_key_value):
  user_profile=request.user
  print("choosen package dict in map view",choosen_package_dict)
  map_package_dict=choosen_package_dict[day_key_value]
  print("choosen package dict in map view",map_package_dict)
  #geocoder=Nominatim(user_agent="tpw")
  #gcode=ArcGIS()
  #loc1="Kozhikode Beach"
  #loc2="Thikkodi drive-in beach"
  '''
  gcode=ArcGIS()
  place_name="Kozhikode Beach"
  place_name_details=gcode.geocode('modinagar')
  print("place_name_details:",place_name_details)
  print("place__details:",gcode.geocode('modinagar'))
  print("place__details_lat:",gcode.geocode(place_name).latitude)
  print("********************************")
  geocoder=Nominatim(user_agent="tpw")
  loc1="Kozhikode Beach"
  loc2="Mananchira Square"
  loc3="mananchira square"
  cordinate1=geocoder.geocode(loc1)
  cordinate2=geocoder.geocode(loc2)
  cordinate3=geocoder.geocode(loc3)
  print("cord1 Koz:",cordinate1)
  print("cord2 Man:",cordinate2)
  print("cord3 man:",cordinate3)
  print("cord1 lat and long KOZ:",cordinate1.latitude,cordinate1.longitude)
  print("cord3 lat and long man:",cordinate3.latitude,cordinate3.longitude)
  print("cord2 lat and long Man:",cordinate2.latitude,cordinate2.longitude)
  lat1,long1=(cordinate1.latitude),(cordinate1.longitude)
  lat2,long2=(cordinate2.latitude),(cordinate2.longitude)
  place1=(lat1,long1)
  place2=(lat2,long2)
  print("distance:",distance.distance(place1,place2))
   #gmap=googlemaps.Client(key=settings.GOOGLE_MAP_API)
   #print("gmap value",gmap)
   #place_name_details=gmap.geocode(place_name)
   #print("place_name_details",place_name_details)

  '''
  '''
  map_package_dict={
      'spotname':map_package_list
  }
  '''
  lat_long_list=[]
  value=0
  for key,items in map_package_dict.items():
     print("value now:",value)
     loc1=items[5]
     print("Latitude",items[5],"=",items[11])
     lat=items[11]
     print("Longitude",items[5],"=",items[12])
     long=items[12]
     spotname=items[5].spotname
     lat_long_dict={'spotname':items[5].spotname,'latitude':lat,'longitude':long}
     lat_long_list.append(lat_long_dict)
     print("lspotname",spotname)
     print("listappended",lat_long_dict)
     value=value+1
     if value==3:
        break
     '''
     if value==1:
        Morning=items
        Morningloc=items[5]
        print("morningloc:",Morningloc)
        print("loc1:",loc1)
        cord1=geocoder.geocode(loc2)
        print("cord1:",cord1)
        Morninglat=cord1.latitude
        Morninglong=cord1.longitude
     elif value==2:
        Afternoon=items
     elif value==3:
        Evening=items
     value=value+1
     print("\n Morning time:",Morning)
     print("\n Afternoon time:",Afternoon)   
     print("\n Evening time:",Evening) 
     '''
     
  #lat_long_list=[{'latitude': 11.255534762482503, 'longitude': 75.76633491897731}, {'latitude': 11.253835976496681, 'longitude': 75.78246464851674}, {'latitude': 11.24884769802104, 'longitude': 75.83385923323074}]
  list10=["hi","1332",23932]
  print("list10:",list10)
  print("tyoe of list10:",type(list10))
  11.255534762482503, 75.76633491897731
  11.253835976496681, 75.78246464851674
  11.24884769802104, 75.83385923323074
  print("latlonglist:",lat_long_list)
  #print("morningloclong:",Morninglong)
  #print("tyoe of morning:",type(loc1))
  #selected_map_package_dict={'Morning':Morning,'Afternoon':Afternoon,'Evening':Evening}
  return render(request,"maps.html",{'day_key_value':day_key_value,'choosen_package_dict':choosen_package_dict,'map_package_list':map_package_dict,'user_profile':user_profile,'list10':list10,'lat_long_list':lat_long_list})
    
@login_required  
def listofaccommodationsview(request,district):
  listoflandscapes=['Beach','Temple','Mosque','Market','Pond','Shopping centre','Park','Museum','Waterfall','Reservoir','Dam','Amusement park','Planetarium','Tourist attractions','Cinema theatre','Bird watching area','Fort','Hill station','Zoo','Garden','Wildlife park','View point','Island','Water bodies','River','Church','Palace','Animal park']
  accommodation_district = district
  user_profile=request.user
  accommodationdetailsdict=dict()
  accommodationdetailslist=Accommodationdetailstable.objects.filter(district=accommodation_district).all()
  number=0
  print("accommodationdetailslist ***************",accommodationdetailslist)
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
  return render(request,"acco-list.html",{'accommodation_district':accommodation_district,'user_profile':user_profile,'accommodationdetailsdict':accommodationdetailsdict,'listoflandscapes':listoflandscapes,'mainpackagedictcopy':mainpackagedictcopy,'mainpackagedict':mainpackagedict,'choosen_package_dict':choosen_package_dict,})

def createpackageview(request):
   print("day createpackageview",day)
   print("destinaton createpackageview",destination)
   selected_place_from_destinations=Destination.objects.filter(spotdistrict=destination).all()
   print("selected_place_from_destinations",selected_place_from_destinations)
   if request.method=="POST":
      create_package_selected_list=request.POST.getlist('create_package_selected_list')
      print("create_package_selected_list",create_package_selected_list)
      return render(request,"create_package.html",{'day':day,'destination':destination,'create_package_selected_list':create_package_selected_list})
   else:
      return render(request,"create_package.html",{'day':day,'destination':destination,'selected_place_from_destinations':selected_place_from_destinations})
'''
    if day == '1': #day is in string format
        mainpackagedict.clear()
        mainpackagelist=Onedaypackage.objects.filter(district=destination).select_related('spotname').all()
        mainspotnamelist=[]
        for package in mainpackagelist:
          number=str(package.packagenumber)
          count=package.district+number
          print(count,"\n")
          key=count
          packagelist=[package.id,                      #0
                      package.district,                 #1
                      package.packagenumber,            #2
                      package.daynumber,                #3
                      package.spottime,                 #4 
                      package.spotname,                 #5
                      package.spotname.location,        #6
                      package.spotname.landscape,       #7
                      package.spotname.cafespot,        #8
                      package.spotname.description,     #9
                      package.spotname.img              #10
                      ]
          print("packagelist->",packagelist,"\n")
          if key not in mainpackagedict:
            mainpackagedict[key]=[]
          mainpackagedict[key].append(packagelist)

    elif day == '2': #day is in string format
        mainpackagedict.clear()
        mainpackagelist=Twodaypackage.objects.filter(district=destination).select_related('spotname').all()
        mainspotnamelist=[]
        for package in mainpackagelist:
          number=str(package.packagenumber)
          count=package.district+number
          print(count,"\n")
          key=count
          packagelist=[package.id,                      #0
                      package.district,                 #1
                      package.packagenumber,            #2
                      package.daynumber,                #3
                      package.spottime,                 #4 
                      package.spotname,                 #5
                      package.spotname.location,        #6
                      package.spotname.landscape,       #7
                      package.spotname.cafespot,        #8
                      package.spotname.description,     #9
                      package.spotname.img              #10
                      ]
          print("packagelist->",packagelist,"\n")
          if key not in mainpackagedict:
            mainpackagedict[key]=[]
          mainpackagedict[key].append(packagelist)

    elif day == '5': #day is in string format
        mainpackagedict.clear()
        mainpackagelist=Threedaypackage.objects.filter(district=destination).select_related('spotname').all()
        mainspotnamelist=[]
        for package in mainpackagelist:
          number=str(package.packagenumber)
          count=package.district+number
          print(count,"\n")
          key=count
          packagelist=[package.id,                      #0
                      package.district,                 #1
                      package.packagenumber,            #2
                      package.daynumber,                #3
                      package.spottime,                 #4 
                      package.spotname,                 #5
                      package.spotname.location,        #6
                      package.spotname.landscape,       #7
                      package.spotname.cafespot,        #8
                      package.spotname.description,     #9
                      package.spotname.img              #10
                      ]
          print("packagelist->",packagelist,"\n")
          if key not in mainpackagedict:
            mainpackagedict[key]=[]
          mainpackagedict[key].append(packagelist)

    
    elif day == '7': #day is in string format
        mainpackagedict.clear()
        mainpackagelist=Sevendaypackage.objects.filter(district=destination).select_related('spotname').all()
        mainspotnamelist=[]
        for package in mainpackagelist:
          number=str(package.packagenumber)
          count=package.district+number
          print(count,"\n")
          key=count
          packagelist=[package.id,                      #0
                      package.district,                 #1
                      package.packagenumber,            #2
                      package.daynumber,                #3
                      package.spottime,                 #4 
                      package.spotname,                 #5
                      package.spotname.location,        #6
                      package.spotname.landscape,       #7
                      package.spotname.cafespot,        #8
                      package.spotname.description,     #9
                      package.spotname.img              #10
                      ]
          print("packagelist->",packagelist,"\n")
          if key not in mainpackagedict:
            mainpackagedict[key]=[]
          mainpackagedict[key].append(packagelist)
    
    '''