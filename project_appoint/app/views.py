from django.shortcuts import render
from django.views import View
from .models import Appointment

# Create your views here.

class Base(View):
    def get(self,request):
        return render(request,'base.html')
    
class Appoint(View):
    def get(self,request):
        return render(request,'appoint.html')
    
    def post(self,request):
        name = request.POST.get('name')
        age = request.POST.get('age')
        con = request.POST.get('contact')
        reason = request.POST.get('for')
        Appointment.objects.create(name=name,age=age,contact=con,reason=reason)
        return render(request,'appoint.html')

