from rest_framework import serializers
from .models import Incident, PriceList, AccountInformation, Login, ResetPassword


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = ['incident_type', 'attention', 'location', 'accused_person_company', 'complaint_description', 'image']


class PriceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceList
        fields = '__all__'


# AccountInformation Serializer
class AccountInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountInformation
        fields = ['name', 'gender', 'phone', 'dob', 'password']
        extra_kwargs = {
            'password': {'write_only': True},  # Password should not be readable
        }

    # You can add a custom validation here if needed (e.g., validate phone number format)


# ResetPasswordForm Serializer
class ResetPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResetPassword
        fields = ['oldPassword', 'newPassword', 'confirmPassword']

    # Custom validation for newPassword and confirmPassword matching
    def validate(self, data):
        if data['newPassword'] != data['confirmPassword']:
            raise serializers.ValidationError("New password and confirmation do not match.")
        return data


# LoginForm Serializer
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['userId', 'password']
        extra_kwargs = {
            'password': {'write_only': True},  # Password should not be readable
        }

    # Custom validation could be added if needed (e.g., for email validation)
