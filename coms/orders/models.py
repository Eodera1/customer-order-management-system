from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.core.exceptions import ValidationError

# Create your models here.
class Customer(TimeStampedModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, default='N/A')
    phone_number = models.CharField(max_length=15)
    
    def clean(self):
        # Validation for Customer code
        if self.code == 'N/A' and self.name:
            raise ValidationError("Code cannot be 'N/A' when the customer's name is provided.")
        
        # Custom validation for phone_number (optional)
        if not self.phone_number.isdigit() or len(self.phone_number) != 10:
            raise ValidationError("Phone number must be a valid 10-digit number.")
    
    def __str__(self):
        return self.name
    
class Order(TimeStampedModel):
    status = models.CharField(max_length=20, default='pending')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    item = models.CharField(max_length=100, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        # Validation for Order amount
        if self.amount is not None and self.amount <= 0:
            raise ValidationError("Order amount must be greater than zero.")
        
        if not self.item:
            raise ValidationError("Item cannot be empty when placing an order.")
    
    def __str__(self):
        return f'{self.customer} - {self.item} - {self.amount}'
