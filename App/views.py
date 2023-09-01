from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from GameStore.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import random


# Create your views here.


def IndexPage(request):

    return render(request,"index.html")


#@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')


def StorePage(request):
    return render(request,"store.html")


@csrf_exempt
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        # if len(uname)>20:
        #     messages.info(request,"Username must be under 20 Characters")
        #     return redirect('signup')
        
        # if len(uname)<4:
        #     messages.info(request,"Username must be at least 4 Characters")
        #     return redirect('signup')
        
        if pass1==pass2:
             if User.objects.filter(username=uname).exists():
                  messages.info(request,"Username already exist")
                  return redirect('signup')
             elif User.objects.filter(email=email).exists():
                  messages.info(request,"Email Already Registered")
                  return redirect('signup')
             else:
                 otp=random.randint(100000,999999)
                 request.session["otp"]=otp
                 send_mail(
                 "title",
                 f"message : /n {otp}",
                 EMAIL_HOST_USER,
                 [email],
                  fail_silently=False
                 )
                 return render(request,'verify.html',{'otp':otp,'username':uname,'email':email,'password':pass1})
                   
        else:
              messages.info(request,"Password and Confirm Password not Matched!!!!")
              return redirect('signup')
              
    return render(request,'signup.html')


@csrf_exempt
def VerifyOTP(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        request.session["username"]=username
        request.session["password"]=password

        form=User(username=username,email=email,password=password)
        form.save()
    return JsonResponse({'data': 'Hello'},status=200)


@csrf_exempt
def NotVerify(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
    return JsonResponse({'data': 'Hello'},status=200)
  
 
def LoginPage(request):
 if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        
        # user=authenticate(request,username=username,email=email)
        # print("user:",user)
        # if user is not None:
            # login(request,user)
            # return render(request,'home.html') 
        if User.objects.filter(username=username,password=password).exists():
             messages.info(request,"")
             return render(request,"home.html",{'username':username})    
        else:
            messages.info(request,"Username or Password is Incorrect!!!!")
            return redirect('login')
 return render(request,'login.html')


def Logout(request):
    logout(request)
    return redirect('index')


def BlockDude(request):
    return render(request,'game.html')


def UnrulyTower(request):
    return render(request,'game2.html')


def StickHero(request):
    return render(request,'game3.html')


def Mario(request):
    return render(request,'game1.html')


def Flappybird(request):
    return render(request,'flappybirds.html')
