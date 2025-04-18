from django.db import models
from user.models import User
from .booking_model import BookingDetail
from utils.base_model import BaseModel


class BookingPayment(BaseModel):
    booking_id = models.ForeignKey(BookingDetail, on_delete=models.CASCADE)
    cleaner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="cleaner")
    client = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="client")
    amount = models.CharField(max_length=15)
    promo_code = models.CharField(max_length=15)
    discounted = models.BooleanField(default=False)
    transation_id = models.CharField(max_length=15, unique=True)
    status = models.CharField(max_length=15, default="pending")

    def save(self, *args, **kwargs):
        if self:
           self.cleaner = self.booking_id.cleaner 
           self.client = self.booking_id.client
        if self.promo_code:
            self.discounted = True
        return super().save(*args, **kwargs)

class Payout(BaseModel):
    booking_id = models.ForeignKey(BookingDetail, on_delete=models.CASCADE)
    cleaner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="cleaner")
    amount = models.CharField(max_length=15)
    transation_id = models.CharField(max_length=15, unique=True)
    status = models.CharField(max_length=15, default="pending")


    def save(self, *args, **kwargs):
        if self:
           self.cleaner = self.booking_id.cleaner
        return super().save(*args, **kwargs)
    