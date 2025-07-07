from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models import Patient, Doctor, PatientDoctorMapping
from api.serializers import (
    UserRegisterSerializer,
    PatientSerializer,
    DoctorSerializer,
    MappingSerializer)
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'patients': reverse('patients-list', request=request, format=format),
        'doctors': reverse('doctors-list', request=request, format=format),
        'list mapping': reverse('mapping-list', request=request, format=format),
        'create mapping': reverse('create-mapping', request=request, format=format),
        'signup': reverse('register-user', request=request, format=format),
        'login': reverse('login-user', request=request, format=format),
    })


# Auth APIs
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


# Patient Views
class PatientCreateListView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]


# Doctor Views
class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]


class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]


# Mappings
class MappingCreateView(generics.CreateAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]


class MappingListView(generics.ListAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]


class PatientDoctorsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, patient_id):
        mappings = PatientDoctorMapping.objects.filter(patient_id=patient_id)
        serializer = MappingSerializer(mappings, many=True)
        return Response(serializer.data)


class MappingDeleteView(generics.DestroyAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [permissions.IsAuthenticated]
