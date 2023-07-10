from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app.authentication.views import *
from app.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('products/', products, name='products'),
    path('customer/add/', add_customer, name='add_customer'),
    path('customers/', customers, name='customers'),
    path('vender/add/', add_vender, name='add_vender'),
    path('vender/', venders, name='venders'),
    path('delete-vender/<int:id>', delete_vender, name='delete_vender'),
    path('update-vender/<int:id>', update_vender, name='update_vender'),
    path('update-customers/<int:id>', update_customers, name='update_customer'),
    path('delete-customers/<int:id>', delete_customer, name='delete_customer'),
    path('products/add/', add_product, name='add_product'),
    path('purchases/add/', add_purchase, name='add_purchase'),   
    path('carts/add/', add_to_cart, name='add_to_cart'),
    path('purchase-delete/<int:id>', purchase_delete, name='purchase-delete'),
    path('update-purchase/<int:id>', update_purchase, name='update-purchase'),
    path('sale-delete/<int:id>', sale_delete, name='sale-delete'),
    path('add/sale/', add_sale, name='add_sale'),
    path('update-sale/<int:id>', update_sale, name='sale-update'),
    path('product-delete/<int:id>', product_delete, name='product-delete'),
    path('product-update/<int:id>', product_update, name='product-update'),
    path('stock/', view_stock, name='stock'),
    path('delete-stock/<int:id>', delete_stock, name='delete-stock'),
    path('update-stock/<int:id>', update_stock, name='update-stock'),
    path('remove/<int:id>', remove_product_from_cart, name='remove_product_from_cart'),
    path('checkout/' ,checkout_items,name='checkout_items'),
    path('sellrecord/' ,sell_record,name='sell_record'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('logout/', logout_view, name='logout'),
     path('accounts/login/', auth_views.LoginView.as_view(template_name='../templates/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)