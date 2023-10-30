from django.contrib import admin

# Register your models here.

from django.contrib import admin
from LittleLemonAPI.models import Order, MenuItem, Category, OrderItem, Cart

admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(MenuItem)#need for adding menu items
admin.site.register(Category)#need for making categorys