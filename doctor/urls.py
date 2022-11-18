from django.conf.urls import url
from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('',views.index, name="index"),
    path('ambulance/', views.ambulance, name="ambulance"),
    path('metaverse/', views.metaverse, name="metaverse"),
    path('patients/', views.patients, name="patients"),
    path('add-patient/', views.PatientAdd.as_view(), name="add-patient"),
    path('medications/', views.MedicationView.as_view(), name="medications"),
    path('add-medication/', views.MedicationAdd.as_view(), name="add-medication"),
    path('tests/', views.TestView.as_view(), name="tests"),
    path('add-test/', views.TestAdd.as_view(), name="add-test"),
    path('appointments/', views.appointments, name="appointments"),
    path('finances/', views.finances, name="finances"),
    path('wards/', views.wards, name="wards"),
    path('tests/', views.tests, name="tests"),
    path('payments/', views.payments, name="payments"),
    path('blood/', views.blood, name="blood"),
    path('doctors/', views.DoctorView.as_view(), name="doctors"),
    path('add-doctor/', views.DoctorAdd.as_view(), name="add-doctor"),
    path('lab/', views.lab, name="lab"),
    path('settings/', views.settings, name="settings"),
    path('screen1/', views.screen1, name="screen1"),
    path('screen2/', views.screen2, name="screen2"),
    path('screen3/', views.screen3, name="screen3"),
    path('screen4/', views.screen4, name="screen4"),
    path('screen5/', views.screen5, name="screen5"),
    path('screen6/', views.screen6, name="screen6"),





]