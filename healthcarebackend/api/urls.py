from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)
from api.views import (RegisterView,
                       PatientCreateListView,
                       PatientDetailView,
                       DoctorListCreateView,
                       DoctorDetailView,
                       PatientDoctorsView,
                       MappingListView,
                       MappingDeleteView,
                       MappingCreateView,
                       api_root
                       )

urlpatterns = [
    # root
    path('', api_root),

    # Auth
    path('api/auth/register/', RegisterView.as_view(), name='register-user'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='login-user'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view()),

    # Patients
    path('api/patients/',
         PatientCreateListView.as_view(),
         name='patients-list'),
    path('api/patients/<int:pk>/',
         PatientDetailView.as_view(),
         name='patient-details'),

    # Doctors
    path('api/doctors/',
         DoctorListCreateView.as_view(),
         name='doctors-list'),
    path('api/doctors/<int:pk>/',
         DoctorDetailView.as_view(),
         name='doctor-details'),

    # Mappings
    path('api/mappings/', MappingListView.as_view(), name='mapping-list'),
    path('api/mappings/<int:pk>/', MappingDeleteView.as_view(), name='mapping-detail'),
    path('api/mappings/create/',
         MappingCreateView.as_view(),
         name="create-mapping"),
    path('api/mappings/<int:patient_id>/', PatientDoctorsView.as_view()),
]
