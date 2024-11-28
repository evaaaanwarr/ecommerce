from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_staff = models.BooleanField('Is staff', default=False)
    is_pelanggan = models.BooleanField('Is pelanggan', default=False)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username

class Product:
    def __init__(self, product_id, name, description, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.stock_quantity = stock_quantity
        
    def update_stock(self, quantity):
        self.stock_quantity -= quantity

class Customer:
    def __init__(self, customer_id, name, email, phone, address):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        
    def update_address(self, new_address):
        self.address = new_address

class Transaction:
    def __init__(self, transaction_id, customer, products, total_amount):
        self.transaction_id = transaction_id
        self.customer = customer
        self.products = products  # List of Product objects
        self.total_amount = total_amount
        self.status = "Pending"
        
    def complete_transaction(self):
        self.status = "Completed"
        for product in self.products:
            product.update_stock(1)  # Assuming 1 item sold per product

class ShoppingCart:
    def __init__(self):
        self.items = []  # List of Product objects
        
    def add_item(self, product):
        self.items.append(product)
        
    def remove_item(self, product):
        self.items.remove(product)
        
    def calculate_total(self):
        return sum(product.price for product in self.items)

