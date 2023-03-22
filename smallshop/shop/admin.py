from django.contrib import admin
from .models import Product,Category
# Register your models here.

#register every model
admin.site.register(Product)
admin.site.register(Category)
