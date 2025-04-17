# in your app's serializers.py
from rest_framework import serializers
from models.coupon import Coupon

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['id', 'code', 'name', 'discount', 'start_time', 'end_time', 'validity']
        read_only_fields = ['id', 'code']
