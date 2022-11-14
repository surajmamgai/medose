from django.shortcuts import render
from django.views.generic import ListView
from accounts.models import Doctor, Patient
from django.forms import ModelForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.
def index(request):
    return render(request, 'index.html')


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

class PatientAddForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class PatientAdd(CreateView):
    # model = Patient
    # fields = '__all__'
    form_class = PatientAddForm
    template_name = 'views/patient-add.html'


def patients(request):
    return render(request, 'views/patients.html')


class PatientView(ListView):
    model = Patient
    template_name = 'views/patients.html'


def appointments(request):
    return render(request, 'views/appointments.html')


def lab(request):
    return render(request, 'views/lab.html')

def settings(request):
    return render(request, 'views/settings.html')

