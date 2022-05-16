# Generated by Django 3.2.9 on 2022-05-16 12:48

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('full_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='full name')),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True, verbose_name='email address')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=27, null=True, region=None, verbose_name='phone number')),
                ('role', models.CharField(choices=[('Administrator', 'Administrator'), ('Doctor', 'Doctor'), ('Labtech', 'Labtech'), ('Nurse', 'Nurse'), ('Patient', 'Patient'), ('Pharmacist', 'Pharmacist'), ('Receptionist', 'Receptionist')], max_length=17, verbose_name='Role')),
                ('is_active', models.BooleanField(default=False, verbose_name='active')),
                ('is_admin', models.BooleanField(default=False, verbose_name='admin')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='bio')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics')),
                ('id_no', models.CharField(blank=True, max_length=58, null=True, verbose_name='National ID')),
                ('nationality', django_countries.fields.CountryField(default='KE', max_length=57, verbose_name='Country')),
                ('town', models.CharField(blank=True, max_length=57, null=True, verbose_name='town')),
                ('estate', models.CharField(blank=True, max_length=57, null=True, verbose_name='estate')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Single', max_length=20, verbose_name='gender')),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('Divorced', 'Divorced'), ('Single', 'Single')], default='Single', max_length=20, verbose_name='marital status')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
                ('job_id', models.CharField(blank=True, max_length=30, null=True, verbose_name='Job id')),
                ('available', models.BooleanField(default=False, verbose_name='available')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.CharField(max_length=57, unique=True, verbose_name='department name')),
                ('room_number', models.CharField(max_length=15, unique=True, verbose_name='room number')),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.administrator')),
            ],
            options={
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='bio')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics')),
                ('id_no', models.CharField(blank=True, max_length=58, null=True, verbose_name='National ID')),
                ('nationality', django_countries.fields.CountryField(default='KE', max_length=57, verbose_name='Country')),
                ('town', models.CharField(blank=True, max_length=57, null=True, verbose_name='town')),
                ('estate', models.CharField(blank=True, max_length=57, null=True, verbose_name='estate')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Single', max_length=20, verbose_name='gender')),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('Divorced', 'Divorced'), ('Single', 'Single')], default='Single', max_length=20, verbose_name='marital status')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
                ('job_id', models.CharField(blank=True, max_length=30, null=True, verbose_name='Job id')),
                ('available', models.BooleanField(default=False, verbose_name='available')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts_receptionist_departments', to='accounts.departments')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pharmacist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='bio')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics')),
                ('id_no', models.CharField(blank=True, max_length=58, null=True, verbose_name='National ID')),
                ('nationality', django_countries.fields.CountryField(default='KE', max_length=57, verbose_name='Country')),
                ('town', models.CharField(blank=True, max_length=57, null=True, verbose_name='town')),
                ('estate', models.CharField(blank=True, max_length=57, null=True, verbose_name='estate')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Single', max_length=20, verbose_name='gender')),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('Divorced', 'Divorced'), ('Single', 'Single')], default='Single', max_length=20, verbose_name='marital status')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
                ('job_id', models.CharField(blank=True, max_length=30, null=True, verbose_name='Job id')),
                ('available', models.BooleanField(default=False, verbose_name='available')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts_pharmacist_departments', to='accounts.departments')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='bio')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics')),
                ('id_no', models.CharField(blank=True, max_length=58, null=True, verbose_name='National ID')),
                ('nationality', django_countries.fields.CountryField(default='KE', max_length=57, verbose_name='Country')),
                ('town', models.CharField(blank=True, max_length=57, null=True, verbose_name='town')),
                ('estate', models.CharField(blank=True, max_length=57, null=True, verbose_name='estate')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Single', max_length=20, verbose_name='gender')),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('Divorced', 'Divorced'), ('Single', 'Single')], default='Single', max_length=20, verbose_name='marital status')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('O+', 'O+'), ('B+', 'B+'), ('AB+', 'AB+'), ('A-', 'A-'), ('O-', 'O-'), ('B-', 'B-'), ('AB-', 'AB-')], default='A+', max_length=15, verbose_name='blood group')),
                ('weight', models.FloatField(default=0.0, help_text='Enter the patients in Kgs', verbose_name='weight')),
                ('height', models.FloatField(default=0.0, help_text='Enter the patients in feets', verbose_name='height')),
                ('blood_pressure', models.FloatField(default=0.0, help_text='Enter the patients in mmHg', verbose_name='blood pressure')),
                ('blood_sugar', models.FloatField(default=0.0, help_text='Enter the patients in mg/dl', verbose_name='blood sugar')),
                ('allergies', models.TextField(blank=True, null=True, verbose_name='allergies')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='bio')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics')),
                ('id_no', models.CharField(blank=True, max_length=58, null=True, verbose_name='National ID')),
                ('nationality', django_countries.fields.CountryField(default='KE', max_length=57, verbose_name='Country')),
                ('town', models.CharField(blank=True, max_length=57, null=True, verbose_name='town')),
                ('estate', models.CharField(blank=True, max_length=57, null=True, verbose_name='estate')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Single', max_length=20, verbose_name='gender')),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('Divorced', 'Divorced'), ('Single', 'Single')], default='Single', max_length=20, verbose_name='marital status')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
                ('job_id', models.CharField(blank=True, max_length=30, null=True, verbose_name='Job id')),
                ('available', models.BooleanField(default=False, verbose_name='available')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts_nurse_departments', to='accounts.departments')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Labtech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='bio')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics')),
                ('id_no', models.CharField(blank=True, max_length=58, null=True, verbose_name='National ID')),
                ('nationality', django_countries.fields.CountryField(default='KE', max_length=57, verbose_name='Country')),
                ('town', models.CharField(blank=True, max_length=57, null=True, verbose_name='town')),
                ('estate', models.CharField(blank=True, max_length=57, null=True, verbose_name='estate')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Single', max_length=20, verbose_name='gender')),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('Divorced', 'Divorced'), ('Single', 'Single')], default='Single', max_length=20, verbose_name='marital status')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
                ('job_id', models.CharField(blank=True, max_length=30, null=True, verbose_name='Job id')),
                ('available', models.BooleanField(default=False, verbose_name='available')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts_labtech_departments', to='accounts.departments')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='bio')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics')),
                ('id_no', models.CharField(blank=True, max_length=58, null=True, verbose_name='National ID')),
                ('nationality', django_countries.fields.CountryField(default='KE', max_length=57, verbose_name='Country')),
                ('town', models.CharField(blank=True, max_length=57, null=True, verbose_name='town')),
                ('estate', models.CharField(blank=True, max_length=57, null=True, verbose_name='estate')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Single', max_length=20, verbose_name='gender')),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Widowed', 'Widowed'), ('Separated', 'Separated'), ('Divorced', 'Divorced'), ('Single', 'Single')], default='Single', max_length=20, verbose_name='marital status')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='timestamp')),
                ('job_id', models.CharField(blank=True, max_length=30, null=True, verbose_name='Job id')),
                ('available', models.BooleanField(default=False, verbose_name='available')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts_doctor_departments', to='accounts.departments')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='administrator',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accounts_administrator_departments', to='accounts.departments'),
        ),
        migrations.AddField(
            model_name='administrator',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
