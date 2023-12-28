from django.contrib import admin
from .models import Products, Order

# Register your models here.
admin.site.site_header =" E-Commerce Website"
admin.site.site_title = "Admin page"
admin.site.index_title = "Manage E-commerce shop"


class ProductsAdmin(admin.ModelAdmin):

    def change_category_to_default(self,request,queryset):
        queryset.update(category = "default")
    
    change_category_to_default.short_description= 'Default Category'
    list_display = ('title','price','discount_pice','category','description')
    search_fields = ('title','category',)
    actions = ('change_category_to_default',)
    fields = ('title','price')
    list_editable = ('price','category')

admin.site.register(Products,ProductsAdmin)
admin.site.register(Order)

