
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from orders.views import CustomerViewSet, OrderViewSet

# router = DefaultRouter()
# router.register(r'customers', CustomerViewSet)
# router.register(r'orders', OrderViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

# orders/urls.py

from django.urls import path, include
from .views import CustomerViewSet, OrderViewSet

urlpatterns = [
    path('api/auth/', include('dj_rest_auth.urls')),  # Authentication endpoints
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # Registration endpoints
    # Include your other viewsets or endpoints here
    path('customers/', CustomerViewSet.as_view({'get': 'list', 'post': 'create'}), name='customer-list'),
    path('orders/', OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='order-list'),
]
