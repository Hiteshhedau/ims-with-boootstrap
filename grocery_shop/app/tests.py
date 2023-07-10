from django.test import TestCase
from django.urls import reverse

from .models import *
import unittest

@unittest.skip
class ProductTestCase(TestCase):
    def setUp(self):
        self.product=Product.objects.create(name="Test Product",price=10)

    def test_product_name(self):
        self.assertEqual(self.product.name,"Test Product")

    def test_product_price(self):
        self.assertEqual (self.product.price,10)

@unittest.skip
class CustomerTestCase(TestCase):
    def setUp(self):
        self.customer=Customer.objects.create(name="Test Customer",email="test@mail.com",address="Pune",phone_number=8965352220)

    def test_customer_name(self):
        self.assertEqual(self.customer.name,"Test Customer") 

    def test_customer_email(self):
        self.assertEqual(self.customer.email,"test@mail.com")

    def test_customer_address(self):
        self.assertEqual(self.customer.address,"Pune")    
         
    def test_customer_phone_number(self):
        self.assertEqual(self.customer.phone_number,8965352220)

@unittest.skip
class VendorTestCase(TestCase):
    def setUp(self):
        self.vender=Vender.objects.create(name="Dummy Vender",address="Nagpur",phone_number=8899663322)

    def test_vender_name(self):
        self.assertEqual(self.vender.name,"Dummy Vender")    

    def test_vender_phone_number(self):
        self.assertEqual(self.vender.phone_number,8899663322) 

    def test_vender_address(self):
        self.assertEqual(self.vender.address,"Nagpur") 


@unittest.skip
class PurchaseTestCase(TestCase):
    def setUp(self):
        self.product=Product.objects.create(name="Test Product",price=10)
        self.vender=Vender.objects.create(name="Dummy Vender",address="Nagpur",phone_number=8899663322)
        self.purchase=Purchase.objects.create(product=self.product,quantity=12,purchase_price=100,vender=self.vender)
               
    def test_purchase_product(self):
        self.assertEqual(self.purchase.product,self.product)

    def test_purchase_vender(self):
        self.assertEqual(self.purchase.vender,self.vender)    


    def test_purchase_quantity(self):
        self.assertEqual(self.purchase.quantity,12)


    def test_purchase_purchase_price(self):
        self.assertEqual(self.purchase.purchase_price,100)

@unittest.skip
class CartTestCase(TestCase):
    def setUp(self):
        self.product=Product.objects.create(name="Test Product",price=10)
        self.cart=Cart.objects.create(product=self.product,quantity=15,total_amount=self.product.price*15)

    def test_cart_product(self):
        self.assertEqual(self.cart.product,self.product)

    def test_cart_quantity(self): 
        self.assertEqual(self.cart.quantity,15)

    def test_cart_total_amount(self):
        self.assertEqual(self.cart.total_amount, self.cart.total_amount)    

@unittest.skip
class SaleTestCase(TestCase):
    def setUp(self):
        self.product=Product.objects.create(name="Test Product",price=10)
        self.customer=Customer.objects.create(name="Test Customer",email="test@mail.com",address="Pune",phone_number=8965352220)
        self.cart=Cart.objects.create(product=self.product,quantity=15,total_amount=self.product.price*15)
        self.sale=Sale.objects.create(cart=self.cart,customer=self.customer)

    def test_sale_cart(self):
        self.assertEqual(self.sale.cart,self.cart)

    def test_sale_customer(self):
        self.assertEqual(self.sale.customer,self.customer)

        
@unittest.skip
class StockTestCase(TestCase):

    def setUp(self):
        self.product=Product.objects.create(name="Test Product",price=10)

        self.stock=Stock.objects.create(product=self.product,qty_left=50)

    def test_stock_product(self):
        self.assertEqual(self.stock.product,self.product)

    def test_stock_qty_left(self):
        self.assertEqual(self.stock.qty_left,50)