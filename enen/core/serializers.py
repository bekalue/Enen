# serializers.py
from rest_framework import serializers
from .models import Doctor, Patient, Assistance

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ('name', 'address', 'contactNumber', 'email', 'specialization', 'address')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('name', 'address', 'contactNumber', 'email', 'userId')

class AssistanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistance
        fields = ('assistanceText', 'doctor', 'patient', 'timestamp', 'isNew', 'isCompleted', 'symptoms')