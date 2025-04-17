from django.urls import path
from routes.coupon_route import CouponListCreateView, CouponRetrieveUpdateDestroyView

urlpatterns = [
    path('coupons/', CouponListCreateView.as_view(), name='create-list-coupon'),
    path('coupons/<uuid:id>/', CouponRetrieveUpdateDestroyView.as_view(), name='retrieve-update-delete-coupon')
]
