from django.db import models
from . import enums
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class AccountInformation(models.Model):
    name = models.CharField(max_length=255)
    gender = enums.Gender
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    dob = models.DateField()
    password = models.CharField()


class ResetPassword(models.Model):
    oldPassword = models.CharField(max_length=255)
    newPassword = models.CharField(max_length=255)
    confirmPassword = models.CharField(max_length=255)


class Login(models.Model):
    userId = models.EmailField()
    password = models.CharField(max_length=255)


class Incident(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    userid = models.IntegerField()

    INCIDENT_TYPES = [
        ('type1', 'Type 1'),
        ('type2', 'Type 2'),
    ]
    incident_type = models.CharField(max_length=50, choices=INCIDENT_TYPES)

    ATTENTION_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    attention = models.CharField(max_length=10, choices=ATTENTION_CHOICES)

    location = models.CharField(max_length=255)
    accused_person_company = models.CharField(max_length=255)
    complaint_description = models.TextField()
    image = models.ImageField(upload_to='incident_images/')

    def __str__(self):
        return f"Incident by {self.name} on {self.date}"

class PriceList(models.Model):
    date = models.DateField(auto_now_add=True)
    rice = models.DecimalField(max_digits=4, decimal_places=2)
    potato = models.DecimalField(max_digits=4, decimal_places=2)
    onion = models.DecimalField(max_digits=4, decimal_places=2)
    garlic = models.DecimalField(max_digits=4, decimal_places=2)
    green_chili = models.DecimalField(max_digits=4, decimal_places=2)


