from django.shortcuts import render
from .forms import IncidentForm, AccountInfoForm, ResetPasswordForm, LoginForm
from .models import Incident, PriceList, AccountInformation, Login, ResetPassword
from .serializers import IncidentSerializer, PriceListSerializer, AccountInformationSerializer, LoginSerializer, ResetPasswordSerializer
from rest_framework import generics, serializers


# Create your views here.
class IncidentListCreateView(generics.ListCreateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer

    def perform_create(self, request):
        serializers.save(name=self.request.user.username, userid=self.request.user.id)


class PriceListView(generics.CreateAPIView, generics.RetrieveAPIView):
    queryset = PriceList.objects.all()
    serializer_class = PriceListSerializer


class AccountInformationListCreateView(generics.CreateAPIView, generics.RetrieveAPIView):
    queryset = AccountInformation.objects.all()
    serializer_class = AccountInformationSerializer

    def perform_create(self, serializer):
        # If you want to add additional logic during the save process, like hashing the password
        password = serializer.validated_data['password']
        # Hash password or other custom logic (e.g., using make_password)
        serializer.save(password=password)


class ResetPasswordCreateView(generics.CreateAPIView):
    queryset = ResetPasswordForm.objects.all()
    serializer_class = ResetPasswordSerializer

    def perform_create(self, serializer):
        # Implement your custom logic for changing the password
        old_password = serializer.validated_data['oldPassword']
        new_password = serializer.validated_data['newPassword']
        # Validate the old password, update the password, etc.
        serializer.save()


class LoginCreateView(generics.CreateAPIView):
    queryset = LoginForm.objects.all()
    serializer_class = LoginSerializer

    def perform_create(self, serializer):
        # Add your login logic here
        user_id = serializer.validated_data['userId']
        password = serializer.validated_data['password']
        # Authenticate the user, handle login, etc.
        serializer.save()
