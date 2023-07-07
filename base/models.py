from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ("doctor", "DOCTOR"),
    ("patient", "PATIENT"),
)

CATEGORIES = (
    ("HEART DISEASE", "HEART DISEASE"),
    ("EAR PROBLEMS", "EAR PROBLEMS"),
    ("COVID-19", "COVID-19"),
    ("EYE PROBLEMS", "EYE PROBLEMS"),
)

DRAFT = (("YES", "YES"), ("NO", "NO"))


class CustomUser(AbstractUser):
    address = models.TextField(null=True, blank=False)
    city = models.CharField(max_length=200, null=True, blank=False)
    pincode = models.IntegerField(null=True, blank=False)
    image = models.ImageField(upload_to="images/", null=True, blank=False)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="doctor")


# modifying user model with new fields
# choices keyword to provide dropdown to choose the role


class Blog(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    title = models.CharField(null=True, blank=False, max_length=150)
    image = models.ImageField(upload_to="images/", null=True, blank=False)
    category = models.CharField(
        max_length=20, choices=CATEGORIES, default="HEART DISEASE"
    )
    draft = models.CharField(max_length=4, choices=DRAFT, default="NO")
    summary = models.TextField(null=True, blank=False)
    content = models.TextField(null=True, blank=False)
    updated = models.DateTimeField(
        auto_now=True, null=True
    )  # whenever user updates something about this model, date is recorded
    created = models.DateTimeField(
        auto_now_add=True, null=True
    )  # records date of creation og entry of this model table

    class Meta:
        ordering = ["-updated", "created"]

class Appointment(models.Model):
    required_speciality = models.CharField(null=True, blank=False, max_length=150)
    

