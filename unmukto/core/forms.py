from django import forms

from unmukto.core import enums
from phonenumber_field.modelfields import PhoneNumberField

from unmukto.core.models import Incident


class AccountInfoForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    gender = enums.Gender
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    dob = forms.DateField()
    password = forms.CharField(widget=forms.PasswordInput)


class ResetPasswordForm(forms.ModelForm):
    oldPassword = forms.CharField(widget=forms.PasswordInput)
    newPassword = forms.CharField(widget=forms.PasswordInput)
    confirmPassword = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.ModelForm):
    userId = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)


class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['incident_type', 'attention', 'location', 'accused_person_company', 'complaint_description', 'image']