from django.contrib import admin
from django.urls import path
from lin_lout import views
from django.urls.conf import include
from dashboard import views

app_name = 'dashboard'

urlpatterns = [
  
   
    path('', views.HOME, name='home'),
    path('docdetail/', views.doctor_details, name='docdetail'),
    path('insdetail/', views.insurance_details, name='insdetail'),
    
    #api call for the just presentation

    path('doctor_details/', views.doctor_details, name='doctor_details'),
    path('appointmnet_details/', views.appointmnet_details, name='appointmnet_details'),
    path('Insurance_Plans_details/', views.Insurance_Plans_details, name='Insurance_Plans_details'),
    path('Insurance_Provider_details/', views.Insurance_Provider_details, name='Insurance_Provider_details'),
    path('Medical_History_details/', views.Medical_History_details, name='Medical_History_details'),
    path('Patients_details/', views.Patients_details, name='Patients_details'),
    path('Symptom_Specialities_details/', views.Symptom_Specialities_details, name='Symptom_Specialities_details'),
    path('Users_details/', views.Users_details, name='Users_details'),
    
]