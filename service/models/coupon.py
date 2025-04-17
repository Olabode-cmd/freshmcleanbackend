from django.db import models
from .base import BaseModel
from django.utils import timezone
import random
import string

def generate_coupon_code(length=8):
    """Generate a random uppercase alphanumeric coupon code."""
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=length))


class Coupon(BaseModel):
    code = models.CharField(max_length=12, unique=True, blank=True)
    name = models.CharField(max_length=150)
    discount = models.PositiveIntegerField(default=0)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    validity = models.BooleanField(default=True)

    def is_valid(self):
        now = timezone.now()
        return self.validity and self.start_time <= now <= self.end_time

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_coupon_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - {self.name} ({self.discount}%)"
