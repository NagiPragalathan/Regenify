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
