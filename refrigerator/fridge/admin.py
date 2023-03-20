from django.contrib import admin
from .models import *

for cls in Slot, Shelf, Product, Category, ProductCategory:
    admin.site.register(cls)