from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=10,null=True)
    address = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
    

class Vender(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=10,null=True)
    address = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name    

    
class Product(models.Model):
    name = models.CharField(max_length=100,null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2,null=True)

class Purchase(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    vender = models.ForeignKey(Vender,on_delete=models.CASCADE,null=True)
    date = models.DateField(auto_now_add=True)


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField( null=True)
    total_amount=models.PositiveIntegerField(editable=False,null=True)

    def save(self,*args,**kwargs):
        self.total_amount=self.quantity*self.product.price
        super().save(*args,**kwargs)

   
class Sale(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.PROTECT,blank=True,null=True)
    date = models.DateField(auto_now_add=True)
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT,blank=True,null=True)

class Stock(models.Model):
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    qty_left=models.IntegerField(null=True)  

   










