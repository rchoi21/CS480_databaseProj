from django.shortcuts import render
from rest_framework import generics, status
from .serializers import (
    VaccinesSerializer, 
    NursesSerializer, 
    PatientsSerializer, 
    CreateNursesSerializer,
    CreatePatientsSerializer,
    ScheduleSerializer,
    PatientScheduleSerializer,
    NurseScheduleSerializer,
    CreateScheduleSerializer,
    CreatePatientScheduleSerializer,
    CreateNurseScheduleSerializer,
    DeleteNursesSerializer,
    UpdateNursesSerializer,
    DeletePatientsSerializer,
    DeleteScheduleSerializer,
    DeletePatientScheduleSerializer,
    DeleteNurseScheduleSerializer,
    UpdatePatientsSerializer,
    UpdateScheduleSerializer,
    UpdatePatientScheduleSerializer,
    UpdateNurseScheduleSerializer,
    CreateVaccinesSerializer,
    DeleteVaccinesSerializer,
    UpdateVaccinesSerializer,
    )
from .models import (
    Vaccines, 
    Nurses, 
    Patients,
    Schedule,
    Patient_Schedule,
    Nurse_Schedule,
    )
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class VaccinesView(generics.ListAPIView):
    queryset = Vaccines.objects.all() # get me all Vaccines objects
    serializer_class = VaccinesSerializer # convert them all to json via serializer

class NursesView(generics.ListAPIView):
    queryset = Nurses.objects.all()
    serializer_class = NursesSerializer

class PatientsView(generics.ListAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer

class ScheduleView(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class PatientScheduleView(generics.ListAPIView):
    queryset = Patient_Schedule.objects.all()
    serializer_class = PatientScheduleSerializer

class NurseScheduleView(generics.ListAPIView):
    queryset = Nurse_Schedule.objects.all()
    serializer_class = NurseScheduleSerializer

class CreateVaccinesView(generics.CreateAPIView):
    queryset = Vaccines.objects.all() 
    serializer_class = CreateVaccinesSerializer 

class CreateNursesView(generics.CreateAPIView):
    queryset = Nurses.objects.all()
    serializer_class = CreateNursesSerializer

class CreatePatientsView(generics.CreateAPIView):
    queryset = Patients.objects.all()
    serializer_class = CreatePatientsSerializer

class CreateScheduleView(generics.CreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = CreateScheduleSerializer

class CreatePatientScheduleView(generics.CreateAPIView):
    queryset = Patient_Schedule.objects.all()
    serializer_class = CreatePatientScheduleSerializer

class CreateNurseScheduleView(generics.CreateAPIView):
    queryset = Nurse_Schedule.objects.all()
    serializer_class = CreateNurseScheduleSerializer

class DeleteVaccinesView(generics.DestroyAPIView):
    queryset = Vaccines.objects.all() 
    serializer_class = DeleteVaccinesSerializer

class DeleteNurseView(generics.DestroyAPIView):
    queryset = Nurses.objects.all()
    serializer_class = DeleteNursesSerializer

class DeletePatientsView(generics.DestroyAPIView):
    queryset = Patients.objects.all()
    serializer_class = DeletePatientsSerializer

class DeleteScheduleView(generics.DestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = DeleteScheduleSerializer

class DeletePatientScheduleView(generics.DestroyAPIView):
    queryset = Patient_Schedule.objects.all()
    serializer_class = DeletePatientScheduleSerializer

class DeleteNurseScheduleView(generics.DestroyAPIView):
    queryset = Nurse_Schedule.objects.all()
    serializer_class = DeleteNurseScheduleSerializer

class UpdateVaccinesView(generics.UpdateAPIView):
    queryset = Vaccines.objects.all() 
    serializer_class = UpdateVaccinesSerializer

class UpdateVaccinesView(generics.UpdateAPIView):
    queryset = Vaccines.objects.all() 
    serializer_class = UpdateVaccinesSerializer

class UpdateNurseView(generics.UpdateAPIView):
    queryset = Nurses.objects.all()
    serializer_class = UpdateNursesSerializer

class UpdatePatientsView(generics.UpdateAPIView):
    queryset = Patients.objects.all()
    serializer_class = UpdatePatientsSerializer

class UpdateScheduleView(generics.UpdateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = UpdateScheduleSerializer

class UpdatePatientScheduleView(generics.UpdateAPIView):
    queryset = Patient_Schedule.objects.all()
    serializer_class = UpdatePatientScheduleSerializer

class UpdateNurseScheduleView(generics.UpdateAPIView):
    queryset = Nurse_Schedule.objects.all()
    serializer_class = UpdateNurseScheduleSerializer
