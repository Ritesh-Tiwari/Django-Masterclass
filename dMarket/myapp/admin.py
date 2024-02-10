from django.contrib import admin
from .models import Product, Orderdetail

# Register your models here.
admin.site.register(Product)
admin.site.register(Orderdetail)