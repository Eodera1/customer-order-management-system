from django.urls import path, include
from .views import CustomerViewSet, OrderViewSet

urlpatterns = [
    path('api/auth/', include('dj_rest_auth.urls')),  # Authentication endpoints
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # Registration endpoints
    # Include your other viewsets or endpoints here
    path('customers/', CustomerViewSet.as_view({'get': 'list', 'post': 'create'}), name='customer-list'),
    path('orders/', OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='order-list'),
]