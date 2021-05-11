from django.test import TestCase
from hospital.forms import YourHealthEditForm,DoctorUpdateForm,PatientUpdateForm,AdminUpdateForm,PatientAppointmentForm,AdminAppointmentForm,AppointmentEditForm,AdmitRegisterForm,AdminAdmitRegisterForm,AddMedForm,OpcostsForm,CovidVaccinationApplicationForm
from django.utils import timezone
from datetime import date,timedelta,time
from hospital.models import Patient,Admin,Doctor,User,Appointment,PatHealth

class FormTest(TestCase):

    nu = User(username='username',email='email@gmail.com',password='password1')
    dt = timezone.now().date()
    doc = Doctor(user=nu,firstname='firstname',
                        lastname='lastname',
                        department='department',
                        dob=dt,
                        address='address',
                        city='city',
                        country='country',
                        postalcode=12345)
    pat = Patient(user=nu,firstname='firstname',
                        lastname='lastname',
                        dob=dt,
                        address='address',
                        city='city',
                        country='country',
                        postalcode=12345)
    

    def test_yourhealtheditform_valid(self):
        yhform = YourHealthEditForm(data={
            'height': 181,
            'weight': 71,
            'diseases': "test disease",
            'medicines': "test meds",
            'ts': "test ts"
        })
        self.assertTrue(yhform.is_valid())
    
    def test_yourhealtheditform_invalid(self):
        yhform = YourHealthEditForm(data={
            'height': 181,
            'weight': 71,
            'disease': 8989,
            'medicines': "test meds",
            'ts': "test ts"
        })
        #print(form.errors)
        self.assertFalse(yhform.is_valid())
        self.assertEquals(len(yhform.errors),1)
    
    def test_doctorupdate_invalid(self):
        dt = timezone.now().date()
        form = DoctorUpdateForm(data={
            "firstname": "fname",
            "lastname": "lname",
            "dob": dt,
            "addess": "test address",
            "country": "test country",
            "city": "test city",
            "postalcode": "pincode",
            "appfees": dt,
            "admfees": 4000
        })
        #print(form.errors)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)
    
    def test_patientupdate_invalid(self):
        dt = timezone.now().date()
        form = PatientUpdateForm(data={
            "firstname": "fname",
            "lastname": "lname",
            "dob": dt,
            "addess": "test address",
            "country": "test country",
            "city": "test city",
            "postalcode": "pincode"
        })
        #print(form.errors)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)
    
    def test_adminupdate_invalid(self):
        dt = timezone.now().date()
        form = AdminUpdateForm(data={
            "firstname": "fname",
            "lastname": "lname",
            "dob": dt,
            "addess": "test address",
            "country": "test country",
            "city": "test city",
            "postalcode": "pincode"
        })
        #print(form.errors)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)

    def test_patientappointmentform_invalid(self):
        dt = date(12,12,12)
        self.nu.save()
        self.doc.save()
        self.pat.save()
        form = PatientAppointmentForm(data={
            'doctor': self.doc,
            'calldate': dt,
            'calltime': "9:00 AM",
            'description': "test description"
        })
        #print(form.errors)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),1)
    
    def test_adminappointmentform_invalid(self):
        dt = date(12,12,12)
        self.nu.save()
        self.doc.save()
        self.pat.save()
        form = AdminAppointmentForm(data={
            'doctor': self.doc,
            'patient': self.pat,
            'calldate': dt,
            'calltime': "9:00 AM",
            'description': "test description"
        })
        #print(form.errors)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)
    
    def test_appointmenteditform_valid(self):
        form = AppointmentEditForm(data={
            'description': "test description"
        })
        self.assertTrue(form.is_valid())
    
    def test_adminadmitregisterform_invalid(self):
        dt = date(12,12,12)
        self.nu.save()
        self.doc.save()
        self.pat.save()
        form = AdminAdmitRegisterForm(data={
            'doctor': self.doc,
            'patient': self.pat,
            'admitDate': dt,
            'description': "test description"
        })
        #print(form.errors)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),2)
        
    def test_addmedform_valid(self):
        form = AddMedForm(data={
            'name': "test name",
            'price': 123
        })
        self.assertTrue(form.is_valid())
    
    def test_opcostsform_valid(self):
        form = OpcostsForm(data={
            'maintenance': 11,
            'hospfee': 123,
            'roomfee': 57
        })
        print(form.errors)
        self.assertTrue(form.is_valid())
    
    
    
    