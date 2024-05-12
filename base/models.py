from django.db import models
import uuid
# Create your models here.
from django.contrib.auth.models import User


class UserRole(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ForeignKey field for the User model
    ROLE_CHOICES = (
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)

# class Patient(models.Model):
#     patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='patient')
#     name = models.CharField(max_length=200, null=True, blank=True)
#     username = models.CharField(max_length=200, null=True, blank=True)
#     age = models.IntegerField(null=True, blank=True)
#     email = models.EmailField(max_length=200, null=True, blank=True)
#     phone_number = models.IntegerField(null=True, blank=True)
#     address = models.CharField(max_length=200, null=True, blank=True)
#     featured_image = models.ImageField(upload_to='patients/', default='patients/user-default.png', null=True, blank=True)
#     blood_group = models.CharField(max_length=200, null=True, blank=True)
#     history = models.CharField(max_length=200, null=True, blank=True)
#     dob = models.CharField(max_length=200, null=True, blank=True)
#     nid = models.CharField(max_length=200, null=True, blank=True)
#     serial_number = models.CharField(max_length=200, null=True, blank=True)
    
#     # Chat
#     login_status = models.CharField(max_length=200, null=True, blank=True, default="offline")

#     def __str__(self):
#         return str(self.user.username)
    

class PatientDocument(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_content = models.BinaryField()
    summary = models.TextField(blank=True)
    last_updated_file = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Document ID: {self.id}, User: {self.user.username}"
    