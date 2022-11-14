from django.conf.urls import url
from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('',views.index, name="index"),
    path('ambulance/', views.ambulance, name="ambulance"),
    path('wards/', views.wards, name="wards"),
    path('tests/', views.tests, name="tests"),
    path('payments/', views.payments, name="payments"),
    path('blood/', views.blood, name="blood"),
    path('doctors/', views.DoctorView.as_view(), name="doctors"),
    path('add-doctor/', views.DoctorAdd.as_view(), name="add-doctor"),
    path('add-patient/', views.PatientAdd.as_view(), name="add-patient"),
    path('patients/', views.PatientView.as_view(), name="patients"),
    path('appointments/', views.appointments, name="appointments"),
    path('lab/', views.lab, name="lab"),
    path('settings/', views.settings, name="settings"),
]