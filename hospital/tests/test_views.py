from django.test import TestCase,Client
from django.urls import reverse
from hospital.models import Patient,Admin,Doctor,User,Appointment
from hospital.forms import AdminAppointmentForm
import json
from django.utils import timezone
from datetime import date,timedelta,time
from django.core.files.uploadedfile import SimpleUploadedFile

class TestViews(TestCase):
    nu = User(username='username',email='email@gmail.com',password='password1')
    doc = Doctor(user=nu,firstname='firstname',
                        lastname='lastname',
                        department='department',
                        dob='12/12/12',
                        address='address',
                        city='city',
                        country='country',
                        postalcode=12345)
    pat = Patient(user=nu,firstname='firstname',
                        lastname='lastname',
                        dob='12/12/12',
                        address='address',
                        city='city',
                        country='country',
                        postalcode=12345)
    
    def test_GET_home_view(self):
        client = Client()
        response = client.get(reverse(''))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'hospital/Home/home.html')

    def test_GET_login_view(self):
        client = Client()
        response = client.get(reverse('login.html'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'hospital/Home/login.html')

    def test_GET_login_pat_view(self):
        client = Client()
        response = client.get(reverse('login_pat.html'))

        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'hospital/Patient/login_pat.html')
    
    def test_GET_bookapp_adm_view(self):
        client = Client()
        response = client.get(reverse('bookapp_adm.html'))
        self.assertEquals(response.status_code,302)
    
    def test_POST_bookapp_adm_view(self):
        client = Client()
        dt = timezone.now().date()
        tm = timezone.now().time()
        response = client.post(reverse('bookapp_adm.html'),{
            'description': "testing bookapp_adm",
            'calldate': dt,
            "calltime": tm,
            'doctor': self.doc,
            'patient': self.pat
        })
        self.assertEquals(response.status_code,302)
    
    def test_GET_patient_adm_view(self):
        client = Client()
        response = client.get(reverse('patient_adm.html'))
        self.assertEquals(response.status_code,302)
    
    def test_GET_patient_all_view(self):
        client = Client()
        response = client.get(reverse('patient_all_view.html'))
        self.assertEquals(response.status_code,302)
    
    def test_GET_doctor_adm_view(self):
        client = Client()
        response = client.get(reverse('doctor_adm.html'))
        self.assertEquals(response.status_code,302)
    
    def test_GET_doctor_all_view(self):
        client = Client()
        response = client.get(reverse('doctor_all_view.html'))
        self.assertEquals(response.status_code,302)
    
    def test_GET_admin_adm_view(self):
        client = Client()
        response = client.get(reverse('admin_adm.html'))
        self.assertEquals(response.status_code,302)
    
    def test_GET_admin_all_view(self):
        client = Client()
        response = client.get(reverse('admin_all_view.html'))
        self.assertEquals(response.status_code,302)
    
    def test_GET_admit_particular_adm_view(self):
        client = Client()
        response = client.get(reverse('admit_particular_adm.html',args=[1]))
        self.assertEquals(response.status_code,302)
    
    def test_GET_approve_pat_view(self):
        client = Client()
        response = client.get(reverse('approve_pat.html'))
        self.assertEquals(response.status_code,302)
    
    def test_GET_approve_doc_view(self):
        client = Client()
        response = client.get(reverse('approve_doc.html'))
        self.assertEquals(response.status_code,302)
    
    def test_GET_approve_adm_view(self):
        client = Client()
        response = client.get(reverse('approve_adm.html'))
        self.assertEquals(response.status_code,302)
    
    def test_GET_approve_patient_view(self):
        client = Client()
        response = client.get(reverse('approve_pat.html'))
        self.assertEquals(response.status_code,302)
    
    def test_GET_approve_doctor_view(self):
        client = Client()
        response = client.get(reverse('approve_doc.html'))
        self.assertEquals(response.status_code,302)
    
    def test_GET_approve_admin_view(self):
        client = Client()
        response = client.get(reverse('approve_adm.html'))
        self.assertEquals(response.status_code,302)
    
    def test_GET_approve_appoint_view(self):
        client = Client()
        response = client.get(reverse('approve_appoint.html'))
        self.assertEquals(response.status_code,302)
    
    def test_GET_approve_app_view(self):
        client = Client()
        response = client.get(reverse('approve_app',args=[1]))
        self.assertEquals(response.status_code,302)
    
    def test_GET_appointment_details_particular_pat_view(self):
        client = Client()
        response = client.get(reverse('bookapp_details_particular_pat.html',args=[1]))
        self.assertEquals(response.status_code,302)
    
    def test_GET_pat_appointment_view(self):
        client = Client()
        response = client.get(reverse('appoint_view_pat.html'))
        self.assertEquals(response.status_code,302)
    
    def test_GET_calladoc_view(self):
        client = Client()
        response = client.get(reverse('calladoc.html'))
        self.assertEquals(response.status_code,302)
    
    def test_GET_medicalreport_view(self):
        client = Client()
        response = client.get(reverse('medicalreport.html'))
        self.assertEquals(response.status_code,302)
    
    def test_GET_bookapp_doc_view(self):
        client = Client()
        response = client.get(reverse('bookapp_doc.html'))
        self.assertEquals(response.status_code,302)
    
    def test_GET_dash_doc_approve_view(self):
        client = Client()
        response = client.get(reverse('dashboard_doc_approve',args=[1]))
        self.assertEquals(response.status_code,302)
    
    def test_GET_dash_doc_view(self):
        client = Client()
        response = client.get(reverse('dashboard_doc.html'))
        self.assertEquals(response.status_code,302)
    
    def test_GET_discharge_doc_view(self):
        client = Client()
        response = client.get(reverse('discharge_doc',args=[1]))
        self.assertEquals(response.status_code,302)
    
    def test_GET_admit_details_particular_doc_add_charge_view(self):
        client = Client()
        response = client.get(reverse('admit_details_particular_doc_add_charge',args=[1,"test comm",2]))
        self.assertEquals(response.status_code,302)
    
    def test_GET_track_med_view(self):
        client = Client()
        response = client.get(reverse('particular_medtrack.html',args=["name"]))
        self.assertEquals(response.status_code,302)

    def test_GET_covid_vaccine_adm_view(self):
        client = Client()
        response = client.get(reverse('covid_vaccine_adm.html'))
        self.assertEquals(response.status_code,302)    
    
    def test_POST_covidvaccine_pat_view(self):
        client = Client()
        response = client.post(reverse('covidvaccine.html'),{
            'commodity': 1
        })
        self.assertEquals(response.status_code,302)

    def test_POST_edityourhealth_view(self):
        client = Client()
        response = client.post(reverse('edityourhealth.html'),{
            'height': 162,
            'weight': 54,
            'diseases': "test diseases",
            'medicines': "test medicines",
            'ts': "test therapy/surgery"
        })
        self.assertEquals(response.status_code,302)
    
    def test_POST_appointment_details_particular_doc_view(self):
        client = Client()
        response = client.post(reverse('bookapp_details_particular_doc.html',args=[1]),{
            'description': "test description"
        })
        self.assertEquals(response.status_code,302)
    
    def test_POST_register_doc_view(self):
        client = Client()
        dt = timezone.now().date()
        response = client.post(reverse('register_doc.html'),{
            'username': "testusername",
            'email': "test@email.com",
            'password1': "ghoter_3",
            'password2': "ghoter_3",
            'firstname': "test fname",
            'lastname': "test lname",
            'department': "test department",
            'dob': dt,
            'address': "test address",
            'city': "test city",
            'country': "test country",
            'postalcode': 12345,
            'image': SimpleUploadedFile(name='test_image.jpg', content=open("./media/default.png", 'rb').read(), content_type='image/png')
        })
        self.assertEquals(response.status_code,200)
    
    def test_POST_register_adm_view(self):
        client = Client()
        dt = timezone.now().date()
        response = client.post(reverse('register_adm.html'),{
            'username': "testusername",
            'email': "test@email.com",
            'password1': "ghoter_3",
            'password2': "ghoter_3",
            'firstname': "test fname",
            'lastname': "test lname",
            'dob': dt,
            'address': "test address",
            'city': "test city",
            'country': "test country",
            'postalcode': 12345,
            'image': SimpleUploadedFile(name='test_image.jpg', content=open("./media/default.png", 'rb').read(), content_type='image/png')
        })
        self.assertEquals(response.status_code,200)
    
    def test_POST_register_pat_view(self):
        client = Client()
        dt = timezone.now().date()
        response = client.post(reverse('register_pat.html'),{
            'username': "testusername",
            'email': "test@email.com",
            'password1': "ghoter_3",
            'password2': "ghoter_3",
            'firstname': "test fname",
            'lastname': "test lname",
            'department': "test department",
            'dob': dt,
            'address': "test address",
            'city': "test city",
            'country': "test country",
            'postalcode': 12345,
            'image': SimpleUploadedFile(name='test_image.jpg', content=open("./media/default.png", 'rb').read(), content_type='image/png')
        })
        self.assertEquals(response.status_code,200)
    
    def test_POST_login_doc_view(self):
        client = Client()
        response = client.post(reverse('login_doc.html'),{
            'username': "testusername",
            'password': "ghoter_3"
        })
        self.assertEquals(response.status_code,200)
    
    def test_POST_login_adm_view(self):
        client = Client()
        response = client.post(reverse('login_adm.html'),{
            'username': "testusername",
            'password': "ghoter_3"
        })
        self.assertEquals(response.status_code,200)
    
    def test_POST_login_pat_view(self):
        client = Client()
        response = client.post(reverse('login_pat.html'),{
            'username': "testusername",
            'password': "ghoter_3"
        })
        self.assertEquals(response.status_code,200)
    
    def test_POST_profile_pat_view(self):
        client = Client()
        dt = timezone.now().date()
        response = client.post(reverse('register_pat.html'),{
            'username': "testusername",
            'email': "test@email.com",
            'password1': "ghoter_3",
            'password2': "ghoter_3",
            'firstname': "test fname",
            'lastname': "test lname",
            'dob': dt,
            'address': "test address",
            'city': "test city",
            'country': "test country",
            'postalcode': 12345,
            'image': SimpleUploadedFile(name='test_image.jpg', content=open("./media/default.png", 'rb').read(), content_type='image/png')
        })
        self.assertEquals(response.status_code,200)
    
    def test_POST_profile_doc_view(self):
        client = Client()
        dt = timezone.now().date()
        response = client.post(reverse('register_doc.html'),{
            'username': "testusername",
            'email': "test@email.com",
            'password1': "ghoter_3",
            'password2': "ghoter_3",
            'department': "test department",
            'firstname': "test fname",
            'lastname': "test lname",
            'dob': dt,
            'address': "test address",
            'city': "test city",
            'country': "test country",
            'postalcode': 12345,
            'image': SimpleUploadedFile(name='test_image.jpg', content=open("./media/default.png", 'rb').read(), content_type='image/png'),
            'appfees': 123,
            'admfees': 300
        })
        self.assertEquals(response.status_code,200)
    
    def test_POST_profile_adm_view(self):
        client = Client()
        dt = timezone.now().date()
        response = client.post(reverse('register_adm.html'),{
            'username': "testusername",
            'email': "test@email.com",
            'password1': "ghoter_3",
            'password2': "ghoter_3",
            'firstname': "test fname",
            'lastname': "test lname",
            'dob': dt,
            'address': "test address",
            'city': "test city",
            'country': "test country",
            'postalcode': 12345,
            'image': SimpleUploadedFile(name='test_image.jpg', content=open("./media/default.png", 'rb').read(), content_type='image/png')
        })
        self.assertEquals(response.status_code,200)