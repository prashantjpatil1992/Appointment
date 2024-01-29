from django.contrib import admin
from .models import Appointment,TimeSlot, AvailableDates, AppointmentHistory

# Register your models here.
@admin.register(Appointment)
class AdminDoc(admin.ModelAdmin):
    list_display = ['name','age','contact','reason','date','time']

@admin.register(AppointmentHistory)
class AdminDoc(admin.ModelAdmin):
    list_display = ['name','age','contact','reason','date','time']

admin.site.register(TimeSlot)
admin.site.register(AvailableDates)