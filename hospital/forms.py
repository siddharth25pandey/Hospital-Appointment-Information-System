from django import forms
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Doctor,Admin,Patient,Appointment,PatHealth,PatAdmit,DoctorProfessional,Medicines
import datetime
from django.forms.widgets import SelectDateWidget
from django.utils import timezone

dep=[('Cardiologist','Cardiologist'),
('Dermatologist','Dermatologist'),
('Emergency Medicine Specialist','Emergency Medicine Specialist'),
('Allergist/Immunologist','Allergist/Immunologist'),
('Anesthesiologist','Anesthesiologist'),
('Colon and Rectal Surgeon','Colon and Rectal Surgeon')
]

class ContactusForm(forms.Form):    #contact us form (feedback), used by patients/doctors to send feedbacks using mail to admins
    Name = forms.CharField(max_length=30,label="",widget=forms.TextInput(attrs={'placeholder': 'NAME'}))
    Name.widget.attrs.update({'class' : 'app-form-control'})
    Email = forms.EmailField(label="",widget=forms.TextInput(attrs={'placeholder': 'EMAIL'}))
    Email.widget.attrs.update({'class' : 'app-form-control'})
    Message = forms.CharField(max_length=500,label="",widget=forms.TextInput(attrs={'placeholder': 'MESSAGE'}))
    Message.widget.attrs.update({'class' : 'app-form-control'})

class DoctorRegisterForm(UserCreationForm): #used to register a doctor
    username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'USERNAME'}))
    username.widget.attrs.update({'class' : 'app-form-control'})
    
    email = forms.EmailField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'EMAIL'}))
    email.widget.attrs.update({'class' : 'app-form-control'})
    
    firstname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'FIRSTNAME'}))
    firstname.widget.attrs.update({'class' : 'app-form-control'})
    
    lastname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'LASTNAME'}))
    lastname.widget.attrs.update({'class' : 'app-form-control'})
    
    dob = forms.DateField(label="",widget=SelectDateWidget(years=range(1960, 2021)))
    dob.widget.attrs.update({'class' : 'app-form-control-date'})
    
    address = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'ADDRESS'}))
    address.widget.attrs.update({'class' : 'app-form-control'})
    
    city = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'CITY'}))
    city.widget.attrs.update({'class' : 'app-form-control'})
    
    country = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'COUNTRY'}))
    country.widget.attrs.update({'class' : 'app-form-control'})
    
    postalcode = forms.IntegerField(label="",widget=forms.TextInput(attrs={'placeholder': 'POSTAL CODE'}))
    postalcode.widget.attrs.update({'class' : 'app-form-control'})
    
    image = forms.ImageField(label="")
    image.widget.attrs.update({'class' : 'app-form-control'})
    
    department = forms.CharField(label="",widget = forms.Select(choices=dep))
    department.widget.attrs.update({'class' : 'app-form-control'})

    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))
    password1.widget.attrs.update({'class' : 'app-form-control'})
    
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'RE-CONFIRM'}))
    password2.widget.attrs.update({'class' : 'app-form-control'})

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname','department', 'dob', 'address', 'city', 'country', 'postalcode', 'password1', 'password2','image']
        #fields = ['username', 'email', 'firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
    
    def checkdate(self):    #form date of birth validator
        cleaned_data = self.cleaned_data
        db = cleaned_data.get('dob')
        if db < timezone.now().date():
            return True
        self.add_error('dob', 'Invalid date of birth.')
        return False

class DoctorUpdateForm(forms.ModelForm):    #used to edit a doctor instance
    firstname = forms.CharField()
    lastname = forms.CharField()
    #age = forms.IntegerField()
    dob = forms.DateField(widget=SelectDateWidget(years=range(1960, 2021)))
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postalcode = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput)
    appfees = forms.FloatField()
    admfees = forms.FloatField()
    class Meta:
        model = Doctor
        fields = ['firstname', 'lastname', 'dob', 'address', 'city', 'country', 'postalcode', 'image','appfees','admfees']


class AdminRegisterForm(UserCreationForm):  #used to register an admin
    username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'USERNAME'}))
    username.widget.attrs.update({'class' : 'app-form-control'})
    
    email = forms.EmailField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'EMAIL'}))
    email.widget.attrs.update({'class' : 'app-form-control'})
    
    firstname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'FIRSTNAME'}))
    firstname.widget.attrs.update({'class' : 'app-form-control'})
    
    lastname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'LASTNAME'}))
    lastname.widget.attrs.update({'class' : 'app-form-control'})
    
    
    dob = forms.DateField(label="",widget=SelectDateWidget(years=range(1960, 2021)))
    dob.widget.attrs.update({'class' : 'app-form-control-date'})
    
    address = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'ADDRESS'}))
    address.widget.attrs.update({'class' : 'app-form-control'})
    
    city = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'CITY'}))
    city.widget.attrs.update({'class' : 'app-form-control'})
    
    country = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'COUNTRY'}))
    country.widget.attrs.update({'class' : 'app-form-control'})
    
    postalcode = forms.IntegerField(label="",widget=forms.TextInput(attrs={'placeholder': 'POSTAL CODE'}))
    postalcode.widget.attrs.update({'class' : 'app-form-control'})
    
    image = forms.ImageField(label="")
    image.widget.attrs.update({'class' : 'app-form-control'})
    
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))
    password1.widget.attrs.update({'class' : 'app-form-control'})
    
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'RE-CONFIRM'}))
    password2.widget.attrs.update({'class' : 'app-form-control'})

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname', 'dob', 'address', 'city', 'country', 'postalcode', 'password1', 'password2','image']
        #fields = ['username', 'email', 'firstname', 'lastname', 'age', 'dob', 'address', 'city', 'country', 'postalcode', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class AdminUpdateForm(forms.ModelForm): #used to edit an admin instance
    firstname = forms.CharField()
    lastname = forms.CharField()
    dob = forms.DateField(widget=SelectDateWidget(years=range(1960, 2021)))
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postalcode = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Admin
        fields = ['firstname', 'lastname', 'dob', 'address', 'city', 'country', 'postalcode', 'image']


class PatientRegisterForm(UserCreationForm):    #used to register a patient
    username = forms.CharField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'USERNAME'}))
    username.widget.attrs.update({'class' : 'app-form-control'})
    
    email = forms.EmailField(required=True,label="",widget=forms.TextInput(attrs={'placeholder': 'EMAIL'}))
    email.widget.attrs.update({'class' : 'app-form-control'})
    
    firstname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'FIRSTNAME'}))
    firstname.widget.attrs.update({'class' : 'app-form-control'})
    
    lastname = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'LASTNAME'}))
    lastname.widget.attrs.update({'class' : 'app-form-control'})
      
    dob = forms.DateField(label="",widget=SelectDateWidget(years=range(1960, 2022)))
    dob.widget.attrs.update({'class' : 'app-form-control-date'})
    
    address = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'ADDRESS'}))
    address.widget.attrs.update({'class' : 'app-form-control'})
    
    city = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'CITY'}))
    city.widget.attrs.update({'class' : 'app-form-control'})
    
    country = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'COUNTRY'}))
    country.widget.attrs.update({'class' : 'app-form-control'})
    
    postalcode = forms.IntegerField(label="",widget=forms.TextInput(attrs={'placeholder': 'POSTAL CODE'}))
    postalcode.widget.attrs.update({'class' : 'app-form-control'})
    
    image = forms.ImageField(label="")
    image.widget.attrs.update({'class' : 'app-form-control'})
    
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'PASSWORD'}))
    password1.widget.attrs.update({'class' : 'app-form-control'})
    
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'RE-CONFIRM'}))
    password2.widget.attrs.update({'class' : 'app-form-control'})

    class Meta:
        model = User
        fields = ['username', 'email', 'firstname', 'lastname', 'dob', 'address', 'city', 'country', 'postalcode', 'password1', 'password2','image']
        help_texts = {k:"" for k in fields}

class PatientUpdateForm(forms.ModelForm):   #used to update a patient
    firstname = forms.CharField()
    lastname = forms.CharField()
    dob = forms.DateField(widget=SelectDateWidget(years=range(1960, 2021)))
    address = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()
    postalcode = forms.IntegerField()
    image = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Patient
        fields = ['firstname', 'lastname', 'dob', 'address', 'city', 'country', 'postalcode', 'image']


class PatientAppointmentForm(forms.ModelForm):      #used to register an appointment by patient
    doctor = forms.TypedChoiceField(label='')   #doctor is chosed from existing doctors in hospital database
    doctor.widget.attrs.update({'class' : 'app-form-control'})
    #doctorId=forms.CharField(widget=forms.Select(choices=c))  
    calldate = forms.DateField(label='',widget=SelectDateWidget(years=range(2021,2024)))    #date of appointment
    calldate.widget.attrs.update({'class' : 'app-form-control-date'})
    calltime = forms.TypedChoiceField(label='') #time of appointment
    calltime.widget.attrs.update({'class' : 'app-form-control'})
    description = forms.CharField(max_length=300,label='',widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    description.widget.attrs.update({'class' : 'app-form-control'}) 
    def __init__(self, *args, **kwargs):
        super(PatientAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].choices = [(c.id, c.firstname+"("+c.department+")") for c in Doctor.objects.filter(status=True).all()]#list of doctors to choose from, taken fresh from database
        self.fields['calltime'].choices = [('9:00 AM','9:00 AM'),('9:15 AM','9:15 AM'),('9:30 AM','9:30 AM'),('9:45 AM','9:45 AM'),('10:00 AM','10:00 AM'),('10:15 AM','10:15 AM'),('10:30 AM','10:30 AM'),('10:45 AM','10:45 AM'),('11:00 AM','11:00 AM'),('11:15 AM','11:15 AM'),('11:30 AM','11:30 AM'),('11:45 AM','11:45 AM'),('12:00 PM','12:00 PM'),('12:P5 PM','12:15 PM'),('12:30 PM','12:30 PM'),('12:45 PM','12:45 PM'),
                                            ('14:00 PM','14:00 PM'),('14:15 PM','14:15 PM'),('14:30 PM','14:30 PM'),('14:45 PM','14:45 PM'),('15:00 PM','15:00 PM'),('15:15 PM','15:15 PM'),('15:30 PM','15:30 PM'),('15:45 PM','15:45 PM'),('16:00 PM','16:00 PM'),('16:15 PM','16:15 PM'),('16:30 PM','16:30 PM'),('16:45 PM','16:45 PM'),('17:00 PM','17:00 PM')]
                                            #choices for time slot for appointment
    class Meta:
        model=Appointment
        fields=['description','calldate','calltime']


class AdminAppointmentForm(forms.ModelForm):     #used to register an appointment by admin
    doctor = forms.TypedChoiceField(label='')   #doctor is chosed from existing doctors in hospital database
    doctor.widget.attrs.update({'class' : 'app-form-control'})
    patient = forms.TypedChoiceField(label='')  #patient is chosed from existing doctors in hospital database
    patient.widget.attrs.update({'class' : 'app-form-control'})
    calldate = forms.DateField(label='',widget=SelectDateWidget(years=range(2021,2024)))    #date of appointment
    calldate.widget.attrs.update({'class' : 'app-form-control-date'})
    calltime = forms.TypedChoiceField(label='') #time of appointment
    calltime.widget.attrs.update({'class' : 'app-form-control'})
    description = forms.CharField(max_length=300,label='',widget=forms.TextInput(attrs={'placeholder': 'Description'}))
    description.widget.attrs.update({'class' : 'app-form-control'}) 
    def __init__(self, *args, **kwargs):
        super(AdminAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].choices = [(c.id, c.firstname+"("+c.department+")") for c in Doctor.objects.filter(status=True).all()]#list of doctors to choose from, taken fresh from database
        self.fields['patient'].choices = [(c.id, c.firstname) for c in Patient.objects.filter(status=True).all()]#list of patients to choose from, taken fresh from database
        self.fields['calltime'].choices = [('9:00 AM','9:00 AM'),('9:15 AM','9:15 AM'),('9:30 AM','9:30 AM'),('9:45 AM','9:45 AM'),('10:00 AM','10:00 AM'),('10:15 AM','10:15 AM'),('10:30 AM','10:30 AM'),('10:45 AM','10:45 AM'),('11:00 AM','11:00 AM'),('11:15 AM','11:15 AM'),('11:30 AM','11:30 AM'),('11:45 AM','11:45 AM'),('12:00 PM','12:00 PM'),('12:P5 PM','12:15 PM'),('12:30 PM','12:30 PM'),('12:45 PM','12:45 PM'),
                                            ('14:00 PM','14:00 PM'),('14:15 PM','14:15 PM'),('14:30 PM','14:30 PM'),('14:45 PM','14:45 PM'),('15:00 PM','15:00 PM'),('15:15 PM','15:15 PM'),('15:30 PM','15:30 PM'),('15:45 PM','15:45 PM'),('16:00 PM','16:00 PM'),('16:15 PM','16:15 PM'),('16:30 PM','16:30 PM'),('16:45 PM','16:45 PM'),('17:00 PM','17:00 PM')]
                                            #choices for time slot for appointment
    
    class Meta:
        model=Appointment
        fields=['description','calldate','calltime']



class YourHealthEditForm(forms.ModelForm):  #patient can edit their health information
    height = forms.FloatField()
    weight = forms.FloatField()
    diseases = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 10}))
    medicines = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 10}))
    ts  = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 10}))
    class Meta:
        model = PatHealth
        fields = ['height','weight','diseases','medicines','ts']
    
        
class AppointmentEditForm(forms.ModelForm): #doctor can edit appointment description field, be it adding new lines or deleting a few of the old one
    description = forms.CharField(max_length=300,label='',widget=forms.TextInput(attrs={'placeholder': 'DESCRIPTION'}))
    description.widget.attrs.update({'class' : 'app-form-control'}) 
    class Meta:
        model = Appointment
        fields = ['description']

class AdmitRegisterForm(forms.ModelForm):   #doctor can admit a patient
    description = forms.CharField(max_length=300,label='',widget=forms.TextInput(attrs={'placeholder': 'DESCRIPTION'}))
    description.widget.attrs.update({'class' : 'app-form-control'}) 
    admitDate = forms.DateField(label='',widget=SelectDateWidget)
    admitDate.widget.attrs.update({'class' : 'app-form-control-date'})
    class Meta:
        model = PatAdmit
        fields = ['description','admitDate']

class AdminAdmitRegisterForm(forms.ModelForm):  #admin can admit a patient
    doctor = forms.TypedChoiceField(label='')   #doctor is chosed from existing doctors in hospital database
    doctor.widget.attrs.update({'class' : 'app-form-control'})
    patient = forms.TypedChoiceField(label='')  #patient is chosed from existing doctors in hospital database
    patient.widget.attrs.update({'class' : 'app-form-control'})
    description = forms.CharField(max_length=300,label='',widget=forms.TextInput(attrs={'placeholder': 'DESCRIPTION'}))
    description.widget.attrs.update({'class' : 'app-form-control'}) 
    admitDate = forms.DateField(label='',widget=SelectDateWidget) 
    admitDate.widget.attrs.update({'class' : 'app-form-control-date'})
    
    def __init__(self, *args, **kwargs):
        super(AdminAdmitRegisterForm, self).__init__(*args, **kwargs)
        self.fields['doctor'].choices = [(c.id, c.firstname+"("+c.department+")") for c in Doctor.objects.filter(status=True).all()]#list of doctors to choose from, taken fresh from database
        self.fields['patient'].choices = [(c.id, c.firstname) for c in Patient.objects.filter(status=True).all()]#list of patients to choose from, taken fresh from database

    class Meta:
        model = PatAdmit
        fields = ['description','admitDate']


class DoctorProfessionalUpdateForm(forms.ModelForm):    #doctor can edit their feees
    appfees = forms.FloatField(label='',widget=forms.TextInput(attrs={'placeholder': 'APPOINTMENT FEES'}))
    appfees.widget.attrs.update({'class' : 'app-form-control'})
    admfees = forms.FloatField(label='',widget=forms.TextInput(attrs={'placeholder': 'ADMIT FEES'}))
    admfees.widget.attrs.update({'class' : 'app-form-control'})
    class Meta:
        model = DoctorProfessional
        fields = ['appfees','admfees']


class AddMedForm(forms.ModelForm):  #admin can add medicines to database
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'NAME'}))
    name.widget.attrs.update({'class' : 'app-form-control'})
    price = forms.FloatField(label='',widget=forms.TextInput(attrs={'placeholder': 'PRICE'}))
    price.widget.attrs.update({'class' : 'app-form-control'})
    class Meta:
        model = Medicines
        fields = ['name','price']

class OpcostsForm(forms.Form):  #admin can change hospital operation charges, like maintenence fee
    maintenance = forms.FloatField(label='',widget=forms.TextInput(attrs={'placeholder':'MAINTAINANCE CHARGE'}))
    maintenance.widget.attrs.update({'class' : 'app-form-control'})
    hospfee = forms.FloatField(label='',widget=forms.TextInput(attrs={'placeholder': 'HOSPITAL FEE'}))
    hospfee.widget.attrs.update({'class' : 'app-form-control'})
    roomfee = forms.FloatField(label='',widget=forms.TextInput(attrs={'placeholder': 'ROOM FEE'}))
    roomfee.widget.attrs.update({'class' : 'app-form-control'})

class CovidVaccinationApplicationForm(forms.Form):  #patient can apply for covid vaccine
    commodity = forms.TypedChoiceField(label='')    #choose type of vaccine
    commodity.widget.attrs.update({'class' : 'app-form-control'})
    
    def __init__(self, *args, **kwargs):
        super(CovidVaccinationApplicationForm, self).__init__(*args, **kwargs)
        covaxin = Medicines.objects.all().filter(name="covaxin").first()    #fetch covaxin vaccine information from database
        covishield = Medicines.objects.all().filter(name="covishield").first()  #fetch covishield vaccine information from database
        self.fields['commodity'].choices = [(covaxin.id, covaxin.name), (covishield.id, covishield.name)]