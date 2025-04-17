import uuid
from django.utils import timezone
from django.db import models

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


    def upd(self):
        self.updated_at = timezone.now()
        self.save()

class ApartmentType(BaseModel):
    name = models.CharField(max_length=55)
    number_of_room = models.PositiveIntegerField(default=0)
    number_of_bathroom = models.PositiveIntegerField(default=0)
    in_kitchen = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class ExtraSpace(BaseModel):
    name = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name



