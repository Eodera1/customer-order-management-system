from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=10, default='N/A')
    phone_number = models.CharField(max_length=15, default='999999999') 
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    status = models.CharField(max_length=20, default='pending')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    item = models.CharField(max_length=100, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.customer} - {self.item} - {self.amount}'
