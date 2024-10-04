from django.test import TestCase
from .models import Customer, Order

class CustomerModelTest(TestCase):
    
    def setUp(self):
        # Set up a test customer
        self.customer = Customer.objects.create(
            name="John Doe", 
            code="JD123", 
            phone_number="0712345678"
        )
    
    def test_customer_creation(self):
        # Test if the customer was created successfully
        customer = Customer.objects.get(name="John Doe")
        self.assertEqual(customer.code, "JD123")
        self.assertEqual(customer.phone_number, "0712345678")
    
    def test_customer_str(self):
        # Test the __str__ method of Customer model
        customer = Customer.objects.get(name="John Doe")
        self.assertEqual(str(customer), "John Doe")


class OrderModelTest(TestCase):
    
    def setUp(self):
        # Set up a test customer and order
        self.customer = Customer.objects.create(
            name="Jane Doe", 
            code="JD456", 
            phone_number="0723456789"
        )
        self.order = Order.objects.create(
            customer=self.customer, 
            item="Laptop", 
            amount=1500.00
        )
    
    def test_order_creation(self):
        # Test if the order was created successfully
        order = Order.objects.get(customer=self.customer)
        self.assertEqual(order.item, "Laptop")
        self.assertEqual(order.amount, 1500.00)
        self.assertEqual(order.status, "pending")  # Check default value
    
    def test_order_str(self):
        # Test the __str__ method of Order model
        order = Order.objects.get(customer=self.customer)
        self.assertEqual(str(order), f'{self.customer} - Laptop - 1500.00')
    
    def test_order_customer_relationship(self):
        # Test the ForeignKey relationship between Order and Customer
        order = Order.objects.get(customer=self.customer)
        self.assertEqual(order.customer.name, "Jane Doe")
