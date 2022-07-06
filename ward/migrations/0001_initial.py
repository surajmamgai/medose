# Generated by Django 3.2.9 on 2022-07-06 18:07

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appointments', '0004_auto_20220706_2107'),
        ('accounts', '0002_driver'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('room_number', models.CharField(max_length=56, verbose_name='room number')),
                ('room_type', models.CharField(choices=[('Single Room', 'Single Room'), ('Twin-Shared Room', 'Twin-Shared Room'), ('Multi-Bed Room', 'Multi-Bed Room')], max_length=57, verbose_name='room type')),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.administrator')),
            ],
            options={
                'verbose_name_plural': 'Rooms',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Slot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('bed_number', models.CharField(max_length=57, verbose_name='bed number')),
                ('price_per_night', models.FloatField(default=0.0)),
                ('vacant', models.BooleanField(default=True, verbose_name='vacant')),
                ('reserved', models.BooleanField(default=False, verbose_name='reserved')),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.administrator')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ward.rooms')),
            ],
            options={
                'verbose_name_plural': 'Slots',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='WardBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admission_date', models.DateTimeField(null=True, verbose_name='admission date')),
                ('date_expected_to_leave', models.DateTimeField(null=True, verbose_name='date expected to leave')),
                ('discharge_date', models.DateTimeField(null=True, verbose_name='discharge date')),
                ('total_amount', models.FloatField(default=0.0, verbose_name='total amount')),
                ('nok_full_name', models.CharField(max_length=109, verbose_name='NOK full names')),
                ('relationship', models.CharField(choices=[('Parent', 'Parent'), ('Gurdian', 'Gurdian'), ('Spouse', 'Spouse'), ('Friend', 'Friend'), ('Relative', 'Relative'), ('Sibling', 'Sibling')], max_length=57, verbose_name='relationship')),
                ('nok_phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=27, null=True, region=None, unique=True, verbose_name='NOK phone number')),
                ('on_waiting_list', models.BooleanField(default=False, verbose_name='on waiting list')),
                ('cleared', models.BooleanField(default=False, verbose_name='cleared')),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.appointments')),
                ('slot', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='ward.slot')),
            ],
            options={
                'verbose_name_plural': 'Ward Booking',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ward_name', models.CharField(max_length=56, unique=True, verbose_name='ward name')),
                ('ward_type', models.CharField(choices=[('Causality ward', 'Causality ward'), ('General ward', 'General ward'), ('Critical Care Unit', 'Critical Care Unit'), ('Intensive Care Unit', 'Intensive Care Unit')], max_length=56, verbose_name='ward type')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=57, verbose_name='gender')),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.administrator')),
            ],
            options={
                'verbose_name_plural': 'Wards',
            },
        ),
        migrations.AddField(
            model_name='rooms',
            name='ward',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ward.ward'),
        ),
    ]
