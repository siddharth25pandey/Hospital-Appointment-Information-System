from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views
from hospital.views import *


class TestUrls(SimpleTestCase):

    def test_urls_is_resolved(self):
        url = reverse('')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,home_view)
    
    def test_urls_is_resolved_bookapp(self):
        url = reverse('bookapp.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,bookapp_view)
    
    def test_urls_is_resolved_calladoc(self):
        url = reverse('calladoc.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,calladoc_view)
    
    def test_urls_is_resolved_feedback(self):
        url = reverse('feedback.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,feedback_view)
    
    def test_urls_is_resolved_medicalreport(self):
        url = reverse('medicalreport.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,medicalreport_view)

    def test_urls_is_resolved_admit_details(self):
        url = reverse('admit_details.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,admit_details_view)
    
    def test_urls_is_resolved_admit_details_particular(self):
        url = reverse('admit_details_particular.html',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,admit_details_particular_view)
    
    def test_urls_is_resolved_appointment_details_particular_pat(self):
        url = reverse('bookapp_details_particular_pat.html',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,appointment_details_particular_pat_view)
    
    def test_urls_is_resolved_endappointment_doc(self):
        url = reverse('endappointment_doc',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,endappointment_doc_view)

    def test_urls_is_resolved_profile_pat(self):
        url = reverse('profile_pat.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,profile_pat_view)

    #########

    def test_urls_is_resolved_yourhealth(self):
        url = reverse('yourhealth.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,yourhealth_view)

    def test_urls_is_resolved_edityourhealth(self):
        url = reverse('edityourhealth.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,edityourhealth_view)

    def test_urls_is_resolved_register_pat(self):
        url = reverse('register_pat.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,register_pat_view)

    def test_urls_is_resolved_login_pat(self):
        url = reverse('login_pat.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,login_pat_view)

    def test_urls_is_resolved_home(self):
        url = reverse('home.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,home_view)

    #########

    def test_urls_is_resolved_dash_doc(self):
        url = reverse('dashboard_doc.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,dash_doc_view)
    
    def test_urls_is_resolved_dash_doc_approve(self):
        url = reverse('dashboard_doc_approve',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,dash_doc_approve_view)
    
    def test_urls_is_resolved_admit_details_doc(self):
        url = reverse('admit_details_doc.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,admit_details_doc_view)
    
    def test_urls_is_resolved_admit_details_particular_doc(self):
        url = reverse('admit_details_particular_doc.html',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,admit_details_particular_doc_view)
    
    def test_urls_is_resolved_admit_details_particular_doc_add_charge(self):
        url = reverse('admit_details_particular_doc_add_charge',args=[1,"testcomm",3])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,admit_details_particular_doc_add_charge_view)
    
    ######
    
    def test_urls_is_resolved_discharge_doc_view(self):
        url = reverse('discharge_doc',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,discharge_doc_view)
    
    def test_urls_is_resolved_bookapp_doc(self):
        url = reverse('bookapp_doc.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,bookapp_doc_view)
    
    def test_urls_is_resolved_bookapp_doc_link(self):
        url = reverse('add_link',args=[1,"testlink"])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,bookapp_doc_link_view)
    
    def test_urls_is_resolved_appointment_details_particular_doc(self):
        url = reverse('bookapp_details_particular_doc.html',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,appointment_details_particular_doc_view)
    
    def test_urls_is_resolved_appointment_details_particular_doc_add_charge_view(self):
        url = reverse('appointment_details_particular_doc_add_charge',args=[1,"testcomm",3])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,appointment_details_particular_doc_add_charge_view)
    
    ######

    def test_urls_is_resolved_feedback_doc(self):
        url = reverse('feedback_doc.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,feedback_doc_view)
    
    def test_urls_is_resolved_register_doc(self):
        url = reverse('register_doc.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,register_doc_view)

    def test_urls_is_resolved_login_doc(self):
        url = reverse('login_doc.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,login_doc_view)


    def test_urls_is_resolved_profile_doc(self):
        url = reverse('profile_doc.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,profile_doc_view)


    def test_urls_is_resolved_dash_adm(self):
        url = reverse('dashboard_adm.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,dash_adm_view)

    def test_urls_is_resolved_dash_adm(self):
        url = reverse('dashboard_adm.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,dash_adm_view)


    def test_urls_is_resolved_patient_adm(self):
        url = reverse('patient_adm.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,patient_adm_view)


    def test_urls_is_resolved_doctor_adm(self):
        url = reverse('doctor_adm.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,doctor_adm_view)

    def test_urls_is_resolved_approve_pat(self):
        url = reverse('approve_pat.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,approve_pat_view)


    def test_urls_is_resolved_approve_doc(self):
        url = reverse('approve_doc.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,approve_doc_view)

    def test_urls_is_resolved_approve_adm(self):
        url = reverse('approve_adm.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,approve_adm_view)

    ######

    def test_urls_is_resolved_approve_doctor(self):
        url = reverse('approve_doctor',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,approve_doctor_view)

    def test_urls_is_resolved_approve_patient(self):
        url = reverse('approve_patient',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,approve_patient_view)
    
    def test_urls_is_resolved_approve_admin(self):
        url = reverse('approve_admin',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,approve_admin_view)
    
    def test_urls_is_resolved_bookapp_adm(self):
        url = reverse('bookapp_adm.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,bookapp_adm_view)
    
    def test_urls_is_resolved_admit_adm(self):
        url = reverse('admit_adm.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,admit_adm_view)

    ######

    def test_urls_is_resolved_calladoc_adm(self):
        url = reverse('calladoc_adm.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,calladoc_adm_view)

    def test_urls_is_resolved_medicalreport_adm(self):
        url = reverse('medicalreport_adm.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,medicalreport_adm_view)

    def test_urls_is_resolved_profile_adm(self):
        url = reverse('profile_adm.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,profile_adm_view)
    
    def test_urls_is_resolved_admin_adm(self):
        url = reverse('admin_adm.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,admin_adm_view)
    
    def test_urls_is_resolved_register_adm(self):
        url = reverse('register_adm.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,register_adm_view)
    
    ########

    def test_urls_is_resolved_login_adm(self):
        url = reverse('login_adm.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,login_adm_view)
    
    def test_urls_is_resolved_yourhealth_adm(self):
        url = reverse('yourhealth_adm.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,yourhealth_adm_view)
    
    def test_urls_is_resolved_admin_appointment(self):
        url = reverse('appoint_view_adm.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,admin_appointment_view)
    
    def test_urls_is_resolved_appointment_particular_adm(self):
        url = reverse('appoint_particular_adm.html',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,appointment_particular_adm_view)
    
    def test_urls_is_resolved_admin_admit(self):
        url = reverse('admit_view_adm.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,admin_admit_view)
    
    #######

    def test_urls_is_resolved_admit_particular_adm(self):
        url = reverse('admit_particular_adm.html',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,admit_particular_adm_view)
    
    def test_urls_is_resolved_pat_appointment(self):
        url = reverse('appoint_view_pat.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,pat_appointment_view)
    
    def test_urls_is_resolved_login(self):
        url = reverse('login.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,login_view)
    
    def test_urls_is_resolved_bill(self):
        url = reverse('bill.html',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,bill_view)

    def test_urls_is_resolved_bill_apt(self):
        url = reverse('bill_apt.html',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,bill_apt_view)

    #######

    def test_urls_is_resolved_approve_appoint(self):
        url = reverse('approve_appoint.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,approve_appoint_view)

    def test_urls_is_resolved_approve_app(self):
        url = reverse('approve_app',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,approve_app_view)

    def test_urls_is_resolved_patient_all(self):
        url = reverse('patient_all_view.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,patient_all_view)

    def test_urls_is_resolved_doctor_all(self):
        url = reverse('doctor_all_view.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,doctor_all_view)

    def test_urls_is_resolved_admin_all(self):
        url = reverse('admin_all_view.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,admin_all_view)

    def test_urls_is_resolved_report(self):
        url = reverse('report.html',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,report_view)

    def test_urls_is_resolved_report_apt(self):
        url = reverse('report_apt.html',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,report_apt_view)

    def test_urls_is_resolved_opcost_adm(self):
        url = reverse('opcost.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,opcost_adm_view)

    #######

    def test_urls_is_resolved_render_pdf_report(self):
        url = reverse('downloadreport',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,render_pdf_report_view)
    
    def test_urls_is_resolved_render_pdf_bill(self):
        url = reverse('downloadbill',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,render_pdf_bill_view)

    def test_urls_is_resolved_render_pdf_report_apt(self):
        url = reverse('downloadreport_apt',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,render_pdf_report_apt_view)

    def test_urls_is_resolved_render_pdf_bill_apt(self):
        url = reverse('downloadbill_apt',args=[1])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,render_pdf_bill_apt_view)
    
    def test_urls_is_resolved_render_covidvaccine_pat(self):
        url = reverse('covidvaccine.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,covidvaccine_pat_view)
    
    def test_urls_is_resolved_render_covid_vaccine_adm(self):
        url = reverse('covid_vaccine_adm.html')
        #print(resolve(url))
        self.assertEquals(resolve(url).func,covid_vaccine_adm_view) 
    
    def test_urls_is_resolved_render_track_med(self):
        url = reverse('particular_medtrack.html',args=["test"])
        #print(resolve(url))
        self.assertEquals(resolve(url).func,track_med_view) 