from django.db import models
from django.contrib.auth.models import User
import datetime

departments=[('Cardiologist','Cardiologist'),   
('Dermatologist','Dermatologist'),
('Emergency Medicine Specialist','Emergency Medicine Specialist'),
('Allergist/Immunologist','Allergist/Immunologist'),
('Anesthesiologist','Anesthesiologist'),
('Colon and Rectal Surgeon','Colon and Rectal Surgeon')
]   #possible departments for doctor

def defaultuser():  #for deleted users(Patient, Doctor, Admin)
    us = User(username="deleteduser",email="deleteduser@deleted.com")
    return us.id        

class Doctor(models.Model): #doctor details
    user =  models.ForeignKey(User, on_delete=models.CASCADE,related_name="Doctor") #user foreign key
    image = models.ImageField(default="default.png",upload_to="profile_pics")   #profile picture
    firstname = models.CharField(max_length=100,default='firstname')    #doctor firstname
    lastname = models.CharField(max_length=100,default='lastname')  #doctor lastname
    dob = models.DateField(default=datetime.date.today) #doctor date of birth
    address = models.CharField(max_length=300,default="address")    #doctor address
    city = models.CharField(max_length=100,default="city")  #doctor city
    country = models.CharField(max_length=100,default="country")    #doctor country
    postalcode = models.IntegerField(default=0) #doctor postalcode
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')  #doctor department from choices given as list
    status=models.BooleanField(default=False)   #doctor status(approved/on-hold)
    def __str__(self):
        return f'{self.user.username}'
        


class Admin(models.Model):  #admin details
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Admin")  #user foreign key
    image = models.ImageField(default="default.png",upload_to="profile_pics")   #profile picture
    firstname = models.CharField(max_length=100,default='firstname')    #admin firstname
    lastname = models.CharField(max_length=100,default='lastname')  #admin lastname
    dob = models.DateField(default=datetime.date.today) #date of birth
    address = models.CharField(max_length=300,default="address")    #admin address
    city = models.CharField(max_length=100,default="city")  #admin city
    country = models.CharField(max_length=100,default="country")    #admin country
    postalcode = models.IntegerField(default=0) #admin postalcode
    status = models.BooleanField(default=False) #admin status(approved/on-hold)
    def __str__(self):
        return f'{self.user.username} Admin Profile'


class Patient(models.Model):    #patient details
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Patient")    #user foreign key
    image = models.ImageField(default="default.png",upload_to="profile_pics",null=True, blank=True) #profile picture
    firstname = models.CharField(max_length=100,default='firstname')    #patient firstname
    lastname = models.CharField(max_length=100,default='lastname')  #patient lastname
    dob = models.DateField(default=datetime.date.today) #patient date of birth
    address = models.CharField(max_length=300,default="address")    #patient address
    city = models.CharField(max_length=100,default="city")  #patient city
    country = models.CharField(max_length=100,default="country")    #patient country
    postalcode = models.IntegerField(default=0) #patient postalcode
    status=models.BooleanField(default=False)   #patient status(approved/on-hold)
    def __str__(self):
        return f'{self.user.username} Patient Profile'



class Appointment(models.Model):    #patient appointment details
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="PatientApp") #patient foreign key
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="DoctorApp")    #doctor foreign key
    description=models.TextField(max_length=500)    #description (symptoms/how to take medicines/causes/precautions)
    link=models.TextField(null=True, blank=True)    #video call room link
    calldate=models.DateField(null=True, blank=True)    #call date
    calltime=models.TimeField(null=True, blank=True)    #call time/slot
    status=models.BooleanField(default=False)   #appointment status(approved/on-hold)
    finished=models.BooleanField(default=False) #appointment finished/to-be-done
    def __str__(self):
        return f'{self.description} Appointment Info'


class PatHealth(models.Model):  #personal health details of patient
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="PatientHealth")  #patient foreign key    
    height=models.FloatField(default=0) #patient height
    weight=models.FloatField(default=0) #patient weight
    diseases=models.CharField(max_length=2000,default='somediseases')   #patient diseases
    medicines=models.CharField(max_length=2000,default='somemedicines') #patient medicines
    ts=models.CharField(max_length=2000,default='treatments/surgery')   #patient treatments/surgeries
    status=models.BooleanField(default=False)   #field to determine whether this instance is filled by the patient or not. if it is not built, it is False and patient has to first fill it
    def __str__(self):
        return f'{self.patient} Health Info'


class PatAdmit(models.Model):   #patient admit details
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="PatientAdmit")   #patient foreign key
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="DoctorAdmit")  #doctor foreign key
    admitDate=models.DateField()    #date on which patient is admitted
    description=models.TextField()  #description (symptoms/how to take medicines/causes/precautions)
    dischargeDate=models.DateField(null=True, blank=True)   #date on which patient is discharged
    def __str__(self):
        return f'{self.patient} Admit Info'

class Medicines(models.Model):  #medicines record
    name = models.TextField()   #name of medicine
    price = models.FloatField() #price of medicine
    def __str__(self):
        return f'{self.name} Info'

class Charges(models.Model):    #charges with respect to admit
    Admitinfo=models.ForeignKey(PatAdmit, on_delete=models.CASCADE, related_name="AdmitDetails")    #admit foreign key
    commodity=models.ForeignKey(Medicines, on_delete=models.CASCADE, related_name="AdmitDetails")   #medicine foreign key
    quantity=models.IntegerField(default=1) #quantity of medicine(commodity)
    def __str__(self):
        return f'{self.commodity} Info'

class ChargesApt(models.Model): #charges with respect to appointment
    Aptinfo=models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name="AptDetails") #appointment foreign key
    commodity=models.ForeignKey(Medicines, on_delete=models.CASCADE, related_name="AptDetails") #medicine foreign key
    quantity=models.IntegerField(default=1) #quantity of medicine(commodity)
    def __str__(self):
        return f'{self.commodity} Info'


class DoctorProfessional(models.Model): #professional details of a doctor
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="DoctorProfessional")   #doctor foreign key
    appfees=models.FloatField() #appointment fees for doctor
    admfees=models.FloatField() #admit fees for doctor
    totalpat = models.IntegerField(default=0)   #total patients treated by doctor
    def __str__(self):
        return f'{self.doctor.firstname} Professional Info'


class OperationCosts(models.Model):     #for easier and smoother day-to-day hospital works, admin can change costs
    name=models.TextField() #name of hospital operation (eg. maintenance)
    cost=models.FloatField()#cost of hospital operation
    description=models.TextField(null=True, blank=True) #description about the operation
    def __str__(self):
        return f'{self.name} Cost'

class CovidVaccination(models.Model):       #to track and record patients who are vaccinated
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="PatientVaccination") #patient foreign key
    vaccine=models.ForeignKey(Medicines, on_delete=models.CASCADE, related_name="Vaccine")  #medicine(here, vaccine) foreign key
    def __str__(self):
        return f'{self.patient.firstname} Covid Vaccination'