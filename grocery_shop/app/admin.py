from django.contrib import admin
from . import models
# Register your models here.

class VendorAdmin(admin.ModelAdmin):
    search_fields=['product__title']

    list_display=['id','full_Name','mobile','address']
admin.site.register(models.Vendor,VendorAdmin)

class UnitAdmin(admin.ModelAdmin):
    search_fields=['title']

    list_display=['id','title']

admin.site.register(models.Unit,UnitAdmin)

class ProductAdmin(admin.ModelAdmin):
    search_fields=['unit__title']

    list_display=['title','unit']

admin.site.register(models.Product,ProductAdmin)


class PurchasesAdmin(admin.ModelAdmin):
    search_fields=['product__title']

    list_display=['id','product','qty','price','total_amt','vender','pur_date']
admin.site.register(models.Purchase,PurchasesAdmin)

class SaleAdmin(admin.ModelAdmin):
    search_fields=['product__title']

    list_display=['id','product','customer','qty','price','total_amt','sale_date']
admin.site.register(models.Sale,SaleAdmin)

class InventoryAdmin(admin.ModelAdmin):
    search_fields=['product__title','product__unit__title']
    list_display=['product','pur_qty','sale_qty','total_bal_qty','pur_date','product_unit','sale_date']
admin.site.register(models.Inventory,InventoryAdmin)



class CustomerAdmin(admin.ModelAdmin):
    search_fields=['customer_name','customer_mobile']
     
    list_display=['customer_name','customer_mobile','customer_address']
admin.site.register(models.Customer,CustomerAdmin)

class PriceAdmin(admin.ModelAdmin):
    list_display=['product','amount']
admin.site.register(models.Price,PriceAdmin)