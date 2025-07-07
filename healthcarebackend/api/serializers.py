from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Patient, Doctor, PatientDoctorMapping
from rest_framework.reverse import reverse


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class PatientSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'condition', 'user', 'url']
        read_only_fields = ['user']

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse('patient-details', args=[obj.pk], request=request)


class DoctorSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialty', 'url']

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse('doctor-details', args=[obj.pk], request=request)


class MappingSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'url']

    def get_url(self, obj):
        request = self.context.get('request')
        return reverse('mapping-detail', args=[obj.pk], request=request)
