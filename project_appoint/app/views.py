from django.shortcuts import render
from django.views import View
from .models import Appointment, TimeSlot
from django.contrib import messages

# Create your views here.

class Base(View):
    def get(self,request):
        return render(request,'base.html')
    
class Appoint(View):
    def get(self,request):
        data = Appointment.objects.all()
        st = TimeSlot.objects.all().values_list('slots',flat=True)
        booked_slot = Appointment.objects.all().values_list('slot',flat=True)
        booked_slot = list(booked_slot)
        print(st)
        return render(request,'appoint.html',{'data':data,'st':st,'booked':booked_slot})
    
    def post(self,request):
        booked_slot = Appointment.objects.all().values_list('slot',flat=True)
        name = request.POST.get('name')
        age = request.POST.get('age')
        con = request.POST.get('contact')
        reason = request.POST.get('for')
        appoint_date = request.POST.get('appoint_date')
        slot = request.POST.get('slot')
        if slot not in list(booked_slot):
            Appointment.objects.create(name=name,age=age,contact=con,reason=reason,appoint_date=appoint_date,slot=slot)
        else:
            messages.success(request,"This Slot Is Already Booked")
        data = Appointment.objects.all()
        st = TimeSlot.objects.all().values_list('slots',flat=True)
        booked_slot = list(booked_slot)
        return render(request,'appoint.html',{'data':data,'st':st,'booked':booked_slot})

def show(request):
    return render(request,'appoint.html')