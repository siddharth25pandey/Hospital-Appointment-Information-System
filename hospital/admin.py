from django.contrib import admin
from .models import Doctor,Admin,Patient,Appointment,PatHealth,PatAdmit,Charges,Medicines,DoctorProfessional,OperationCosts,ChargesApt,CovidVaccination

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Admin)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(PatHealth)
admin.site.register(PatAdmit)
admin.site.register(Charges)
admin.site.register(Medicines)
admin.site.register(DoctorProfessional)
admin.site.register(OperationCosts)
admin.site.register(ChargesApt)
admin.site.register(CovidVaccination)