from django.urls import path
from .routes.coupon_route import CouponListCreateView, CouponRetrieveUpdateDestroyView
from .routes.apartment_route import ApartmentTypeListCreateView, ApartmentTypeRetrieveUpdateDestroyAPIViewView, ExtraSpaceViewListCreate, ExtraSpaceRetrieveUpdateDestroyAPIViewView

urlpatterns = [
    path('coupons/', CouponListCreateView.as_view(), name='create-list-coupon'),
    path('coupons/<uuid:id>/', CouponRetrieveUpdateDestroyView.as_view(), name='retrieve-update-delete-coupon'),

    # Apartment
    path('apartment-types/', ApartmentTypeListCreateView.as_view(), name='create-list-coupon'),
    path('apartment-types/<uuid:id>/', ApartmentTypeRetrieveUpdateDestroyAPIViewView.as_view(), name='retrieve-update-delete-coupon'),

    # ExtraSpace
    path('extra-spaces/', ExtraSpaceViewListCreate.as_view(), name='create-list-coupon'),
    path('extra-spaces/<uuid:id>/', ExtraSpaceRetrieveUpdateDestroyAPIViewView.as_view(), name='retrieve-update-delete-coupon'),
]
