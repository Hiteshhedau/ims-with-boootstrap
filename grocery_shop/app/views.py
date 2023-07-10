from django.shortcuts import render,redirect
from app.models import Product,Purchase,Sale,Customer,Vender,Vender,Stock,Cart
from app.modelForm.PurchaseForm import PurchaseForm
from app.modelForm.ProductForm import ProductForm
from app.modelForm.PurchaseForm import PurchaseForm
from app.modelForm.SaleForm import SaleForm
from app.modelForm.CustomerForm import CustomerForm
from app.modelForm.VenderForm import VenderForm
from app.modelForm.StockForm import StockForm
from app.modelForm.AddToCartForm import AddToCartForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# inventory/views.py
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import login, logout
# from django.shortcuts import render, redirect

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             login(request, form.get_user())
#             return redirect('dashboard')
#     else:
#         form = AuthenticationForm(request)
#     return render(request, 'inventory/login.html', {'form': form})


# @login_required
# def dashboard_view(request):
#     return render(request, 'inventory/dashboard.html')


# def logout_view(request):
#     logout(request)
#     return redirect('login')

@login_required
def home(request):
    stocks = Stock.objects.all()
    low_stock_threshold = 10  

    low_stock_products = []

    for stock in stocks:
        if stock.qty_left < low_stock_threshold:
            low_stock_products.append(stock)
    context = {
        'stocks': stocks,
        'low_stock_products': low_stock_products
    }
    return render(request, 'home.html',context)

@login_required
def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

@login_required
def add_customer(request):
    if request.method=='POST':
        name=request.POST['name']
        phone_number=request.POST['phone_number']
        address=request.POST['address']
        customer=Customer(name=name,phone_number=phone_number,address=address)
        customer.save()
        return redirect('customers')
    else:
        return render(request,'add_customer.html')
    
@login_required
def update_customers(request,id):
    customer = Customer.objects.get(pk=id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = CustomerForm(instance=customer)
        context = {'form': form, 'id': id}
    return render(request, 'update_customer.html', context) 

@login_required
def delete_customer(request,id):
    customer=Customer.objects.get(pk=id)
    customer.delete()
    return redirect('customers')
   
@login_required
def customers(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})   
 
@login_required
def add_product(request):    
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        product = Product(name=name,  price=price)
        product.save()
        return redirect('products')
    else:
        return render(request, 'add_product.html')

@login_required
def add_vender(request):
    if request.method=='POST':
        name=request.POST['name']
        phone_number=request.POST['phone_number']
        address=request.POST['address']
        vender=Vender(name=name,phone_number=phone_number,address=address)
        vender.save()
        return redirect('venders')
    else:
        return render(request,'add_vender.html')

@login_required
def venders(request):
    venders = Vender.objects.all()
    return render(request, 'venders.html', {'venders': venders}) 

@login_required
def delete_vender(request,id):
    vender=Vender.objects.get(pk=id)
    vender.delete()
    return redirect('venders')

@login_required
def update_vender(request,id):
    vender = Vender.objects.get(pk=id)
    if request.method == 'POST':
        form = VenderForm(request.POST, instance=vender)
        if form.is_valid():
            form.save()
            return redirect('venders')
    else:
        form = VenderForm(instance=vender)
        context = {'form': form, 'id': id}
    return render(request, 'update_vender.html', context) 

@login_required
def add_purchase(request):
    purchases = Purchase.objects.all()
    products=Product.objects.all()
    venders=Vender.objects.all()
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            product=form.cleaned_data['product']
            quantity=form.cleaned_data['quantity']
            purchase_price=form.cleaned_data['purchase_price']
            vender=form.cleaned_data['vender']
            purchase=Purchase(product=product,quantity=quantity,purchase_price=purchase_price,vender=vender)
            purchase.save()
            try:
                stock_entries=Stock.objects.get(product=product)              
                stock_entries.qty_left+=quantity   
            except Stock.DoesNotExist:              
                stock_entries=Stock(product=product,qty_left=quantity)       
            stock_entries.save()    
            return redirect('add_purchase')
    else:       
        form = PurchaseForm()
    return render(request, 'add_purchase.html', {'form': form,'purchases':purchases,'products':products,'venders':venders} )

@login_required
def add_sale(request):
    print("add_sale")
    sales = Sale.objects.all()
    carts=Cart.objects.all()
    customers=Customer.objects.all()
    stocks=Stock.objects.all()
   
    print(request)
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            cart=form.cleaned_data['cart']
            customer=form.cleaned_data['customer']     
            form.save()
            messages.success(request, 'Product sold successfully.')
            for cart in carts:            
                stock=Stock.objects.get(product=cart.product)
                stock.qty_left-=cart.quantity
                stock.save() 
                  
            carts.delete()          
            return redirect( 'add_to_cart')
    else:            
        form = SaleForm()
    context={'sales':sales,'form': form,'carts':carts,}    
    return render(request, 'addToCart.html',context)

@login_required
def sell_record(request):
    sales=Sale.objects.all()
    return render(request,'sell_record.html',{'sales':sales})

@login_required
def purchase_delete(request,id): 
   purchase=Purchase.objects.get(pk=id)
   purchase.delete()
   return redirect('add_purchase')

@login_required
def update_purchase(request,id): 
    products = Product.objects.all() 
    venders=Vender.objects.all()
    purchase = Purchase.objects.get(pk=id)
    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
            return redirect('add_purchase')
    else:
        form = PurchaseForm(instance=purchase)
    context = {'form': form, 'id': id,'products': products,'venders':venders}
    return render(request, 'update_purchase.html', context)

@login_required
def sale_delete(request,id):
   sale=Sale.objects.get(pk=id)
   sale.delete()
   return redirect('add_sale')

@login_required
def update_sale(request,id):
    products = Product.objects.all()
    sale = Sale.objects.get(pk=id)
    if request.method == 'POST':
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect('add_sale')
    else:
        form = SaleForm(instance=sale)
    context = {'form': form, 'id': id,'products': products,}
    return render(request, 'update_sale.html', context)

@login_required
def product_delete(request,id):
    product=Product.objects.get(pk=id)
    product.delete()
    return redirect('products') 


@login_required
def product_update(request,id):
    product = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm(instance=product)
    context = {'form': form, 'id': id,}
    return render(request, 'update_product.html', context)

@login_required
def add_to_cart(request):
    carts=Cart.objects.all()
    empty=not carts.exists()
    stocks=Stock.objects.all()
    qty_error_message=""
    product_error_message=""
    num=0
    products=Product.objects.all()
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            product=form.cleaned_data['product']
            quantity=form.cleaned_data['quantity']                                                        
            stock=Stock.objects.get(product=product)
            if quantity<=stock.qty_left:                
                try:                
                    cart_item=Cart.objects.get(product=product)                      
                    cart_item.quantity+=quantity                  
                except Cart.DoesNotExist:       
                    cart_item=Cart(product=product,quantity=quantity)    
                cart_item.save()
                return redirect('add_to_cart')
            else:
                qty_error_message="Product quantity exceeds available stock."                          
    else:
        form=AddToCartForm()
    net_amount=0    
    for cart in carts:
        net_amount= net_amount+  cart.total_amount    
    context={'products':products,'carts':carts,'empty':empty,'qty_error_message':qty_error_message,'form':form,'product_error_message':product_error_message,'stocks':stocks,'net_amount':net_amount,'num':num}    
    return render(request,'addToCart.html',context)



@login_required
def remove_product_from_cart(request, id):
    cart_item = Cart.objects.get(pk=id)  
    cart_item.delete()  
    return redirect('add_to_cart')



@login_required
def view_stock(request):
    stock_items = Stock.objects.all()
    context = {'stock_items': stock_items}
    return render(request, 'stock.html', context)


@login_required
def delete_stock(request,id):
    stock=Stock.objects.get(pk=id)
    stock.delete()
    return redirect('stock') 


@login_required
def update_stock(request,id):   
    products=Product.objects.all()
    stock = Stock.objects.get(pk=id)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stock')
    else:
        form = StockForm(instance=stock)
    context = {'form': form, 'id': id,'products':products}
    return render(request, 'update_stock.html', context)



@login_required
def checkout_items(request):
    carts=Cart.objects.all()
    customers=Customer.objects.all()
    net_amount=0    
    for cart in carts:
        net_amount= net_amount+  cart.total_amount 
    context={'customers':customers,'carts':carts,'net_amount':net_amount}
    return render(request,'checkout.html',context)




