from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from .models import Appointment, TimeSlot, AvailableDates, AppointmentHistory
from django.contrib import messages
from datetime import datetime,date,time
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

# Create your views here.

class Base(View):
    def get(self,request):
        return render(request,'base.html')
    
class Appoint(View):
    def get(self,request):
        if request.user.is_authenticated:
            data = Appointment.objects.filter(user_id=request.user)
            st = TimeSlot.objects.all().values_list('slots',flat=True)
            booked_slot = Appointment.objects.all().values_list('slot',flat=True)
            booked_slot = list(booked_slot)
            return render(request,'appoint.html',{'data':data,'st':st,'booked':booked_slot})
        else:
            return HttpResponseRedirect('/usersignup/')
        
    def post(self,request):
        if request.user.is_authenticated:
            booked_slot = Appointment.objects.filter(user_id=request.user).values_list('slot',flat=True)
            name = request.POST.get('name')
            age = request.POST.get('age')
            con = request.POST.get('contact')
            reason = request.POST.get('for')
            # appoint_date = request.POST.get('appoint_date')
            slot = request.POST.get('slot')
            avd = AvailableDates.objects.all().values_list('dates',flat=True)
            avd = list(avd)
            
            if '26-01-2024' in avd:
                if slot:
                    if slot not in list(booked_slot):
                        Appointment.objects.create(name=name,age=age,contact=con,reason=reason,slot=slot)
                    else:
                        messages.success(request,"This Slot Is Already Booked")
                else:
                    messages.success(request,"All Slots Are Booked Pleased Apply Tomorrow Morning")
            data = Appointment.objects.filter(user_id=request.user)
            st = TimeSlot.objects.all().values_list('slots',flat=True)
            booked_slot = list(booked_slot)
            return render(request,'appoint.html',{'data':data,'st':st,'booked':booked_slot})
        else:
            return HttpResponseRedirect('/')

def show(request):
    return render(request,'appoint.html')

def Doctor(request):
    if request.user.is_authenticated and request.user.is_staff:
        data = Appointment.objects.all()
        return render(request,'doctor.html',{'data':data})
    else:
        messages.success(request,"You Are Not A Staff Please Login to Patient Login")
        return HttpResponseRedirect('/doctsignup/') 

def History(request,id):
    data = Appointment.objects.get(pk=id)
    name = data.name
    age = data.age
    contact = data.contact
    reason = data.reason
    date = data.date
    time = data.time
    slot = data.slot
    AppointmentHistory.objects.create(name=name,age=age,contact=contact,reason=reason,date=date,time=time,slot=slot)
    Appointment.objects.get(pk=id).delete()
    return HttpResponseRedirect('/doctor/')

def Doc_SignUp(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass') 
        u = User.objects.create_user(uname,email,pass1)
        u.is_staff = True
        u.save()
    return render(request,'doct_signup.html')

def Doc_Login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=uname,password=pass1)
        if user is not None:
            login(request,user)
        return HttpResponseRedirect('/doctor/')
    

def User_SignUp(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass') 
        User.objects.create_user(uname,email,pass1)
    return render(request,'user_signup.html')

def User_Login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username=uname,password=pass1)
        if user is not None:
            login(request,user)
        return HttpResponseRedirect('/appoint/')
    
def User_Logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')