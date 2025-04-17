from django.db import models
from .base import BaseModel, ExtraSpace, ApartmentType
from user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

WEEKDAYS = [
    ('MON', 'MONDAY'),
    ('TUE', 'TUESDAY'),
    ('WED', 'WEDNESDAY'),
    ('THU', 'THURSDAY'),
    ('FRI', 'FRIDAY'),
    ('SAT', 'SATURDAY'),
    ('SUN', 'SUNDAY')
]

class Booking(BaseModel):
    class STATUS_CHOICES(models.TextChoices):
        NOT_STARTED = "NOT STARTED", "NOT STARTED"
        IN_PROGRESS = "IN PROGRESS", "IN PROGRESS"
        COMPLETED =  "COMPLETED", "COMPLETED"
    class SCHEDULE(models.TextChoices):
        ON_OFF = "ON-OFF", "ON-OFF"
        WEEKLY = "WEEKLY", "WEEKLY"
        BI_WEEKLY = "BI-WEEKLY", "BI-WEEKLY"
        MONTHLY = "MONTHLY", "MONTHLY"
    cleaner = models.ForeignKey(User, related_name='cleanings', on_delete=models.CASCADE)
    client = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)
    apartment = models.ForeignKey(ApartmentType, on_delete=models.CASCADE)
    number_of_room = models.PositiveIntegerField(default=0)
    number_of_bath = models.PositiveIntegerField(default=0)
    schedule = models.CharField(max_length=20, choices=SCHEDULE, default=SCHEDULE.ON_OFF)
    number_of_days = models.PositiveIntegerField(default=0)
    selected_days = models.CharField(max_length=20, choices=WEEKDAYS)
    extra_spaces = models.ManyToManyField(ExtraSpace, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    cleaning_location = models.TextField()
    extra_spaces = models.ManyToManyField(ExtraSpace, blank=True)
    number_of_extras = models.PositiveIntegerField(default=0, null=True)
    weekdays = models.CharField(max_length=12, choices=WEEKDAYS, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES.NOT_STARTED)
    week_type = models.IntegerField(choices=[(1, "Week 1"), (2, "Week 2"),(2, "Week 2"), (2, "Week 2")], null=True, blank=True)
    day_of_month = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1),  MaxValueValidator(31)])


    def calculate_price(self):
        apartment_price = self.apartment.price
        room_diff = max(0, self.number_of_room - self.apartment.number_of_room)
        bath_diff = max(0, self.number_of_bath - self.apartment.number_of_bathroom)


        extra_room_price = room_diff * 13
        extra_bath_price = bath_diff * 7

        extras_total = 0
        if self.extra_spaces.exists():
            for extra in self.extra_spaces.all():
                extras_total += extra.price * (self.number_of_extras or 1)


        days_count = 1  
        if self.schedule == self.SCHEDULE.WEEKLY and self.selected_days:
            days_count = len(self.selected_days.split(',')) 
        elif self.schedule == self.SCHEDULE.BI_WEEKLY and self.selected_days:
            days_count = len(self.selected_days.split(',')) * 2
        elif self.schedule == self.SCHEDULE.MONTHLY and self.selected_days:
            days_count = len(self.selected_days.split(',')) * 4

        self.number_of_days = days_count

        total_price = (apartment_price + extra_room_price + extra_bath_price + extras_total) * days_count
        return total_price

    def save(self, *args, **kwargs):
        self.price = self.calculate_price()
        super().save(*args, **kwargs)
  
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    

    

    

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.pk:
            self.price += sum(space.price for space in self.extra_spaces.all())
            super().save(update_fields=['price'])

    def __str__(self):
        return f"{self.client.username} booking with {self.cleaner.username} - {self.status}"
