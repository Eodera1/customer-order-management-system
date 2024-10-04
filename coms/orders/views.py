from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderSerializer
from django.shortcuts import get_object_or_404
from .utils import send_sms

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Create your views here.
def perform_create(self, serializer):
    order = serializer.save()
    
    # Retrieve the customer for the order
    customer = get_object_or_404(Customer, pk=order.customer.id)
    
    # Create the SMS message
    message = f"Hello {customer.name}, your order for {order.item} has been placed."
    
    # Send the SMS using Africa's Talking API
    response = send_sms(customer.phone_number, message)
    
    # You can add logging or response handling for the SMS if needed
    print(f"SMS sent to {customer.phone_number}: {response}")
