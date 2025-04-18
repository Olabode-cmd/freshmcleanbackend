from django.urls import path
from .routes.coupon_route import CouponListCreateView, CouponRetrieveUpdateDestroyView
from .routes.kyc_router import UserKYCProfileListCreateView, UserKYCProfileRetrieveUpdateDestroyView
from .routes.apartment_route import ApartmentTypeListCreateView, ApartmentTypeRetrieveUpdateDestroyAPIViewView, ExtraSpaceViewListCreate, ExtraSpaceRetrieveUpdateDestroyAPIViewView

urlpatterns = [
    path('coupons/', CouponListCreateView.as_view(), name='create-list-coupon'),
    path('coupons/<uuid:id>/', CouponRetrieveUpdateDestroyView.as_view(), name='retrieve-update-delete-coupon'),

    # Apartment
    path('apartment-types/', ApartmentTypeListCreateView.as_view(), name='create-list-apartment-type'),
    path('apartment-types/<uuid:id>/', ApartmentTypeRetrieveUpdateDestroyAPIViewView.as_view(), name='retrieve-update-delete-apartment-type'),

    # ExtraSpace
    path('extra-spaces/', ExtraSpaceViewListCreate.as_view(), name='create-list-extra-space'),
    path('extra-spaces/<uuid:id>/', ExtraSpaceRetrieveUpdateDestroyAPIViewView.as_view(), name='retrieve-update-delete-extra-space'),

    #KYC
    path('user-cleaner-kyc/', UserKYCProfileListCreateView.as_view(), name='create-list-kyc'),
    path('user-cleaner-kyc/<uuid:id>/', UserKYCProfileRetrieveUpdateDestroyView.as_view(), name='retrieve-update-delete-kyc'),

]
