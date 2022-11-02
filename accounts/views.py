from ast import Import
from accounts.info import EMAIL_HOST_USER
#from multiprocessing import context
from projet import settings
from pyexpat.errors import messages
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.contrib.auth import logout,authenticate
from django.contrib.auth import login as mylogin
from django.contrib.auth.decorators import *
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
from .models import *

def home(request):
    newss=News.objects.order_by('-created_n')
   # newss=News.objects.all()
    paginator=Paginator(newss,1)
    page_number=request.GET.get('page')
    jobs=paginator.get_page(page_number)
    context={'page_obj':jobs}
    return render(request,'home.html',context)
'''def listing(request):
    contact_list = Contact.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list.html', {'page_obj': page_obj})
    '''
#--------------------------------------------
#def admine(request):
   
 #   return render(request,'administration.html',locals())


# Create your views here.
def creat_us(request):
    form_u=CreatUser()
    form_p=ProfiletUser
    if request.method=='POST':
        form_u=CreatUser(request.POST)
        form_p=ProfiletUser(request.POST,request.FILES)
        if form_u.is_valid() and form_p.is_valid():
            user=form_u.save(commit=False)
            prof=form_p.save(commit=False)
            prof.user=user
            user.save()
            prof.save()
            subject= 'مرحبا'
            message='  مرحبا بك معنا في موقع بلدية حاسي الرمل ' + '  ' +user.username
            from_email=settings.EMAIL_HOST_USER
            to_list=[user.email]
            send_mail(subject,message,from_email,to_list)
            return redirect(home)
        else:
            messages.error

    return render(request,'profile/creation.html',locals())
  # ------------------------------
def users_reqe(request):
    #user_now=User.objects.get(id=id)
    form_p=RequetteA()
    if request.method=='POST':
        form_p=RequetteF(request.POST,request.FILES)
        if form_p.is_valid():
            
             
            #form_p.userr=user_now

            
            form_p.save()
            subject= 'تم استلام رسالتك'
            message='  تم استلام رسالتك سيتم التواصل معكم  \n\n\n  شكراا جزيلاا ' + '  ' 
            from_email=settings.EMAIL_HOST_USER
            to_list=EMAIL_HOST_USER
            send_mail(subject,message,from_email,to_list)

            return redirect(home)

            
    context={'form':form_p}


    return render(request,'profile/requettes.html',context)

  #----------------------------------
def users_req(request,id):
    user_now=User.objects.get(id=id)
    form=RequetteF()
    if request.method=='POST':
        form=RequetteF(request.POST,request.FILES)
        if form.is_valid():
            
            form_p=form.save(commit=False)
            form_p.userr=user_now

            
            form_p.save()
            subject= 'تم استلام رسالتك'
            message='  تم استلام رسالتك سيتم التواصل معكم  \n\n\n  شكراا جزيلاا ' + '  ' +user_now.username
            from_email=settings.EMAIL_HOST_USER
            to_list=[user_now.email]
            send_mail(subject,message,from_email,to_list)

            return redirect(home)

            
    context={'form':form}


    return render(request,'profile/requette.html',context)
#-----------------------------------------------------


def user_logout(request):
    logout(request)
    return redirect(home)

def users_profile(request,id):
   
    util=User.objects.get(id=id)
    prof=profile.objects.filter(user=util)
    
    return render(request,'profile/profile.html',locals())

#------------------------------------------
def update_us(request,id):
   
    form_u=CreatUser()
    form_p=ProfiletUser
    if request.method=='POST':
        form_u=CreatUser(request.POST)
        form_p=ProfiletUser(request.POST,request.FILES)
        if form_u.is_valid() and form_p.is_valid():
            user=form_u.save(commit=False)
            prof=form_p.save(commit=False)
            prof.user=user
            user.save()
            prof.save()

            return redirect(home)
        else:
            messages.error

    return render(request,'profile/update.html',locals())
#------------------------------------------ 
'''
import requests

def index_w(request,id):
    appid='b0b546ca72c8cf29d17fc19a43989061'
    URL='https://api.openweathermap.org/data/2.5/weather?'
    PARAMS={'q':'amesterdam','appid':appid,'units':'metric'}
    r=requests.get(url=URL ,params=PARAMS)
    res =r.json()
    print('*-----------------------------*')
    print(res)
    print('*-----------------------------*')
    description = res ['weather'][0]['description']
    icon = res ['weather'][0]['icon']
    temp = res ['main']['temp']


    
    return render(request, 'weather/index.html',locals()) #returns the index.html template

'''
#----------------------------------------------------

def liens(request,id):
    return render(request,'profile/liens.html')
#-----------------------------------------------------

#----------------------------------------------------
@login_required()
def apc(request,id):
    #news=News.objects.order_by('created_n')
    req=Requette_u.objects.order_by('-created_r')
    req_f=Requette_u.objects.filter(lot_terrain=True).order_by('-created_r')
    req_ass=profile.objects.filter(list_ch='association')
    #req_ass_l=Requette_u.objects.filter(userrr=req_ass)
    new_to_del=News.objects.all()
    if request.method == 'POST':
        
        form_n=NewsF(request.POST,request.FILES)
       # form_n=NewsF(request.POST,request.FILES)
                     
        print('befor is valid')
        if form_n.is_valid():
            print('after is valid')
            form_n.save()
            return redirect(home)
    else:
            form_n=NewsF()
    
    return render(request,'administration.html',locals())

def del_n(request,id):
    dell=News.objects.get(id=id)
    dell.delete()
    return redirect(home)
#-----------------------------------------------------

def user_singin(request):
    if request.method=='POST':
        user_name=request.POST.get('username')
        pass_word=request.POST.get('password')
        user =authenticate(request,username=user_name,password=pass_word)
         
        if user is not None:
            
           mylogin(request,user) 
           return redirect(home)
        else:
            return  HttpResponse('<center><h1>اسم المستخدم او كلمة المرور خاطئة </h1></center>')
          #  messages.info(request,'erreurs fatal')
    return render(request,'profile/login.html',locals())


    

