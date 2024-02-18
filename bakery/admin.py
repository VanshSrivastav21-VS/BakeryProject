from django.contrib import admin
from .models import Category, Product, Order, MenuItem

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(MenuItem)
admin.site.register(Order)


