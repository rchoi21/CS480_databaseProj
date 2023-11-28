from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Vaccines(models.Model):
    vax_id = models.AutoField(null=False, primary_key=True)
    name = models.CharField(max_length=100, null=False)
    co_name = models.CharField(max_length=100, null=False)
    doses_req = models.IntegerField(null=False, default=1)
    description = models.TextField(max_length=500, blank=True)
    available = models.IntegerField(null=False, default=0)
    on_hold = models.IntegerField(null=False, default=0)

class Nurses(models.Model):
    employee_id = models.AutoField(null=False, primary_key=True)
    fname = models.CharField(max_length=50, null=False)
    mi = models.CharField(max_length=1, blank=True)
    lname = models.CharField(max_length=50, null=False)
    age = models.IntegerField(null=False, validators=[MinValueValidator(21)])
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"
    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other")
    ]
    gender = models.CharField(max_length=1, null=False, choices=GENDER_CHOICES)
    phone_num = models.CharField(max_length=10, null=False)
    address = models.CharField(max_length=200, null=False)

class Patients(models.Model):
    ssn = models.CharField(max_length=9, primary_key=True, null=False)
    fname = models.CharField(max_length=50, null=False)
    mi = models.CharField(max_length=1)
    lname = models.CharField(max_length=50, null=False)
    age = models.IntegerField(null=False, validators=[MinValueValidator(1)])
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"
    GENDER_CHOICES = [
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other")
    ]
    gender = models.CharField(max_length=1, null=False, choices=GENDER_CHOICES)
    WHITE = "WH"
    AFRICAN_AMERICAN = "AA"
    NATIVE_AMERICAN = "NA"
    ASIAN = "AS"
    PACIFIC_ISLANDER = "PI"
    OTHER = "OT"
    RACE_CHOICES = [
        (WHITE, "White"),
        (AFRICAN_AMERICAN, "African American"),
        (NATIVE_AMERICAN, "Native American"),
        (ASIAN, "Asian"),
        (PACIFIC_ISLANDER, "Pacific Islander"),
        (OTHER, "Other")
    ]
    race = models.CharField(max_length=2, null=False)
    occupation = models.CharField(max_length=50)
    medical_history = models.TextField(max_length=500, blank=True)
    phone_num = models.CharField(max_length=10, null=False)
    address = models.CharField(max_length=200, null=False)

class Schedule(models.Model):
    schedule_id = models.AutoField(null=False, primary_key=True)
    slot = models.DateTimeField(null=False)
    num_patients = models.IntegerField(null=False, default=0)
    num_nurses = models.IntegerField(null=False, default=0)

class Patient_Schedule(models.Model):
    P_schedule_id = models.AutoField(null=False, primary_key=True)
    slot = models.TimeField(null=False)
    ssn = models.CharField(max_length=9, null=False)
    employee_id = models.IntegerField(null=False, default=0)
    vax_id = models.IntegerField(null=False)
    vax_dose = models.IntegerField(null=False, default=0)

class Nurse_Schedule(models.Model):
    N_schedule_id = models.AutoField(null=False, primary_key=True)
    slot = models.TimeField(null=False)
    employee_id = models.IntegerField(null=False, default=0)
    num_patients = models.IntegerField(null=False, default=0)
