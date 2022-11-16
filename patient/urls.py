from django.conf.urls import url
from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('',views.appointments, name="index"),
    path('ambulance/', views.ambulance, name="ambulance"),
    path('metaverse/', views.metaverse, name="metaverse"),
    path('patients/', views.patients, name="patients"),
    path('add-patient/', views.PatientAdd.as_view(), name="add-patient"),
    path('medications/', views.MedicationView.as_view(), name="medications"),
    path('add-medication/', views.MedicationAdd.as_view(), name="add-medication"),
    path('tests/', views.TestView.as_view(), name="tests"),
    path('add-test/', views.TestAdd.as_view(), name="add-test"),
    path('appointments/', views.appointments, name="appointments"),
    path('appointment-add/', views.AppointmentAdd.as_view(), name="add-appointment"),
    path('insurance/', views.insurance, name="insurance"),
    path('family/', views.family, name="family"),
    path('wards/', views.wards, name="wards"),
    path('tests/', views.tests, name="tests"),
    path('payments/', views.payments, name="payments"),
    path('blood/', views.blood, name="blood"),
    path('doctors/', views.DoctorView.as_view(), name="doctors"),
    path('add-doctor/', views.DoctorAdd.as_view(), name="add-doctor"),
    path('lab/', views.lab, name="lab"),
    path('settings/', views.settings, name="settings"),
]