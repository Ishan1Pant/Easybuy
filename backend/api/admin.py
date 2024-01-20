from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(products)
admin.site.register(order_items)
admin.site.register(shipping_address)
admin.site.register(reviews)

@admin.register(orders)
class orderadmin(admin.ModelAdmin):
    list_display=[
        'user','created_at','total_price'
    ]

