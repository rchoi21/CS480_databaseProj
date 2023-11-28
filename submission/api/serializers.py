from rest_framework import serializers
from .models import (
    Vaccines, 
    Nurses, 
    Patients,
    Schedule,
    Patient_Schedule,
    Nurse_Schedule,
    )

class VaccinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccines
        fields = ('vax_id', 'name', 'co_name', 'doses_req','description', 'available', 'on_hold')

class NursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurses
        fields = ('employee_id', 'fname', 'mi', 'lname', 'age', 'gender', 'phone_num', 'address')

class PatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ('ssn', 'fname', 'mi', 'lname', 'age', 'gender', 'race', 'occupation', 'medical_history', 'phone_num', 'address')

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('schedule_id', 'slot', 'num_patients', 'num_nurses')

class PatientScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient_Schedule
        fields = ('P_schedule_id', 'slot', 'ssn', 'employee_id', 'vax_id', 'vax_dose')

class NurseScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse_Schedule
        fields = ('N_schedule_id', 'slot', 'employee_id', 'num_patients')

class CreateVaccinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccines
        fields = ('name', 'co_name', 'doses_req','description', 'available', 'on_hold')

class CreateNursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurses
        fields = ('fname', 'mi', 'lname', 'age', 'gender', 'phone_num', 'address')

class CreatePatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ('ssn', 'fname', 'mi', 'lname', 'age', 'gender', 'race', 'occupation', 'medical_history', 'phone_num', 'address')

class CreateScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('slot', 'num_patients', 'num_nurses')

class CreatePatientScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient_Schedule
        fields = ('slot', 'ssn', 'employee_id', 'vax_id', 'vax_dose')

class CreateNurseScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse_Schedule
        fields = ('slot', 'employee_id', 'num_patients')

class DeleteVaccinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccines
        fields = ('vax_id', 'name', 'co_name', 'doses_req','description', 'available', 'on_hold')

class DeleteNursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurses
        fields = ('employee_id', 'fname', 'mi', 'lname', 'age', 'gender', 'phone_num', 'address')

class DeletePatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ('ssn', 'fname', 'mi', 'lname', 'age', 'gender', 'race', 'occupation', 'medical_history', 'phone_num', 'address')

class DeleteScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('schedule_id', 'slot', 'num_patients', 'num_nurses')

class DeletePatientScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient_Schedule
        fields = ('P_schedule_id', 'slot', 'ssn', 'employee_id', 'vax_id', 'vax_dose')
        
class DeleteNurseScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse_Schedule
        fields = ('N_schedule_id', 'slot', 'employee_id', 'num_patients')

class UpdateVaccinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccines
        fields = ('vax_id', 'name', 'co_name', 'doses_req','description', 'available', 'on_hold')

class UpdateNursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurses
        fields = ('employee_id', 'fname', 'mi', 'lname', 'age', 'gender', 'phone_num', 'address')

class UpdatePatientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = ('ssn', 'fname', 'mi', 'lname', 'age', 'gender', 'race', 'occupation', 'medical_history', 'phone_num', 'address')

class UpdateScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('schedule_id', 'slot', 'num_patients', 'num_nurses')

class UpdatePatientScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient_Schedule
        fields = ('P_schedule_id', 'slot', 'ssn', 'employee_id', 'vax_id', 'vax_dose')
        
class UpdateNurseScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse_Schedule
        fields = ('N_schedule_id', 'slot', 'employee_id', 'num_patients')