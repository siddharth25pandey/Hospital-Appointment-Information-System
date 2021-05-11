from django.test import TestCase
from hospital.models import Doctor,Admin,Patient,Appointment,User,PatHealth,PatAdmit,Charges,DoctorProfessional,Medicines,OperationCosts,ChargesApt,CovidVaccination
from django.utils import timezone

class ModelTest(TestCase):
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
    
    def test_appcreation(self):
        dt = timezone.now().date()
        tm = timezone.now().time()
        self.nu.save()
        self.doc.save()
        self.pat.save()
        app = Appointment.objects.create(doctor=self.doc,patient=self.pat,calldate=dt,calltime=tm,description="testing appointment creation")
        self.assertEquals(str(app),"testing appointment creation Appointment Info")

    def test_pathealthcreation(self):
        self.nu.save()
        self.pat.save()
        ph = PatHealth(patient=self.pat,height=170,weight=70,diseases="test disease",medicines="test medicines", ts="test treatment/surgery")
        self.assertEquals(str(ph),"username Patient Profile Health Info")
    
    def test_patadmitcreation(self):
        dt = timezone.now().date()
        self.nu.save()
        self.doc.save()
        self.pat.save()
        pa = PatAdmit(patient=self.pat,doctor=self.doc,admitDate=dt,description="testing patadmit creation")
        self.assertEquals(str(pa),"username Patient Profile Admit Info")
    
    def test_medicinescreation(self):
        m = Medicines(name="test name",price=120)
        self.assertEquals(str(m),"test name Info")
    
    def test_chargescreation(self):
        dt = timezone.now().date()
        tm = timezone.now().time()
        self.nu.save()
        self.doc.save()
        self.pat.save()
        app = Appointment.objects.create(doctor=self.doc,patient=self.pat,calldate=dt,calltime=tm,description="testing appointment creation")
        app.save()
        m = Medicines(name="test name",price=120)
        m.save()
        capt = ChargesApt(Aptinfo=app,commodity=m,quantity=3)
        self.assertEquals(str(capt),"test name Info Info")

    def test_chargesaptcreation(self):
        dt = timezone.now().date()
        self.nu.save()
        self.doc.save()
        self.pat.save()
        pa = PatAdmit(patient=self.pat,doctor=self.doc,admitDate=dt,description="testing patadmit creation")
        pa.save()
        m = Medicines(name="test name",price=120)
        m.save()
        ch = Charges(Admitinfo=pa,commodity=m,quantity=3)
        self.assertEquals(str(ch),"test name Info Info")
    
    def test_doctorprofessionalcreation(self):
        self.nu.save()
        self.doc.save()
        pa = DoctorProfessional(doctor=self.doc,appfees=300,admfees=3000,totalpat=0)
        self.assertEquals(str(pa),"firstname Professional Info")
    
    def test_operationcostscreation(self):
        oc = OperationCosts(name="test name",cost=123,description="testing description")
        self.assertEquals(str(oc),"test name Cost")
    
    def test_covidvaccinationcreation(self):
        self.nu.save()
        self.pat.save()
        m = Medicines(name="test name",price=120)
        m.save()
        cv = CovidVaccination(patient=self.pat,vaccine=m)
        self.assertEquals(str(cv),"firstname Covid Vaccination")
