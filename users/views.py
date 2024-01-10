from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . models import CustomUser
# Create your views here.

'''
def index(request):
  if request.method=="POST":
    if 'login' in request.POST:
      return loginview(request)
    elif 'signup' in request.POST:
      return signupview(request)
  else:
    django_messages = messages.get_messages(request)
    return render(request,"index.html", {'django_messages': django_messages})
'''

  
def signupview(request):
  if request.method=='POST':
    username=request.POST['username']
    email=request.POST['email']
    password1=request.POST['password']
    password2=request.POST['confirmpassword']

    if password1==password2:
      if CustomUser.objects.filter(username=username).exists():
        print('user name exist already')
        messages.warning(request,"Username exist")
        return redirect("index")
      else:
        if CustomUser.objects.filter(email=email).exists():
          print('email exist already')
          messages.warning(request,"Email exist")
          return redirect("index")
        else:
          user=CustomUser.objects.create_user(username=username,password=password1,email=email)
          user.save()
          print('user created')
          messages.success(request,"Account created")
          return redirect("/")
    else:
      messages.error(request,"Password not matching")
      print("password not matching")
      return redirect("/")
    
  else:
    django_messages = messages.get_messages(request)
    return render(request,"signup.html",{'django_messages': django_messages})
  


def loginview(request):
  if request.method=='POST':
    username=request.POST["username"]
    password=request.POST["password"]
    user=auth.authenticate(username=username,password=password)
    if user is not None:
      auth.login(request,user)
      if request.user.is_authenticated and request.user.is_accommodation:
        print("accommodation user logged in")
        return redirect('accommodations/')
      else:
        print("regular user logged in")
        messages.success(request,"")
        return redirect('packages/')
    else:
      print("invalid credentials")
      messages.error(request, 'Invalid credentials')
      return redirect('/')
    
  else:
    django_messages = messages.get_messages(request)
    return render(request,"login.html",{'django_messages': django_messages})



