from django.shortcuts import render
from django.db.models import Sum
from django.views.generic import ListView
from accounts.models import Doctor, Patient, Profile
from appointments.models import Appointments, Medication, Test
from django.forms import ModelForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.
def index(request):
    return render(request, 'index.html')

def metaverse(request):
    return render(request, 'views/metaverse.html')

def appointments(request):
    user = request.user
    print(user.id)
    try:
        doctor = Doctor.objects.get(user=user.id)
        model = Appointments.objects.filter(doctor=doctor.id)
    except Exception as e:
        doctor = Doctor.objects.get(user=1)
        model = Appointments.objects.filter(doctor=doctor.id)
    return render(request, 'doctor/appointments.html', {'data': model, 'user': user, 'doctor': doctor})

def patients(request):
    user = request.user
    print(user.id)
    try:
        doctor = Doctor.objects.get(user=user.id)
        model = Appointments.objects.filter(doctor=doctor.id)
    except Exception as e:
        doctor = Doctor.objects.get(user=1)
        model = Appointments.objects.filter(doctor=doctor.id)
    return render(request, 'doctor/patients.html', {'data': model, 'user': user, 'doctor': doctor})

def finances(request):
    user = request.user
    print(user.id)
    try:
        doctor = Doctor.objects.get(user=user.id)
        model = Appointments.objects.filter(doctor=doctor.id)
    except Exception as e:
        doctor = Doctor.objects.get(user=1)
        model = Appointments.objects.filter(doctor=doctor.id)
    total = model.aggregate(Sum('appointment_fee'))['appointment_fee__sum'] 
    print(total)
    return render(request, 'doctor/finances.html', {'data': model, 'user': total, 'doctor': doctor})

class PatientAddForm(ModelForm):
    class Meta:
        model = Patient
        exclude = ['medicine', 'price', 'paid', 'date_dispenced', 'dispenced']

class PatientAdd(CreateView):
    form_class = PatientAddForm
    success_url = ('/dashboard/patients/')
    template_name = 'doctor/patient-add.html'

class MedicationAddForm(ModelForm):
    class Meta:
        model = Medication
        exclude = ['medicine', 'price', 'paid', 'date_dispenced', 'dispenced']

class MedicationAdd(CreateView):
    form_class = MedicationAddForm
    success_url = ('/dashboard/medications/')
    template_name = 'doctor/medication-add.html'

class MedicationView(ListView):
    model = Medication
    template_name = 'doctor/medications.html'

class TestAddForm(ModelForm):
    class Meta:
        model = Test
        exclude = ['medicine', 'price', 'paid', 'date_dispenced', 'dispenced']

class TestAdd(CreateView):
    form_class = TestAddForm
    success_url = ('/dashboard/tests/')
    template_name = 'doctor/test-add.html'

class TestView(ListView):
    model = Test
    template_name = 'doctor/tests.html'



def ambulance(request):
    return render(request, 'views/ambulance.html')


def wards(request):
    return render(request, 'views/wards.html')


def tests(request):
    return render(request, 'views/tests.html')


def payments(request):
    return render(request, 'views/payments.html')


def blood(request):
    return render(request, 'views/blood.html')


def doctors(request):
    return render(request, 'views/doctors.html')

class DoctorView(ListView):
    model = Doctor
    template_name = 'views/doctors.html'

class DoctorAddForm(ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class DoctorAdd(CreateView):
    # model = Doctor
    # fields = '__all__'
    form_class = DoctorAddForm
    template_name = 'views/add-doctor.html'


def lab(request):
    return render(request, 'views/lab.html')

def settings(request):
    return render(request, 'views/settings.html')

