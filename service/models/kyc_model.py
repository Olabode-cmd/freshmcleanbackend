from django.db import models
from user.models import User
from utils.base_model import BaseModel


class KYCDoucment(BaseModel):
    fullname = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    id_image = models.ImageField(upload_to="ID image")
    resume = models.FileField(upload_to="Resume")
    id_document = models.FileField(upload_to="Resume")

    def save(self, *args, **kwargs):
        ...
        return super().save()
    

class UserKYCProfile(BaseModel):
    class STATUS(models.TextChoices):
        PENDING = "PENDING", "PENDING"
        SUCCESSFUL = "SUCCESSFUL", "SUCCESSFUL"
        FAILED = "FAILED", "FAILED"
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    document = models.ForeignKey(KYCDoucment, on_delete=models.CASCADE, unique=True)
    status = models.CharField(max_length=15, choices=STATUS, default=STATUS.PENDING, blank=True)


