from django.contrib import admin
from .models import Slot, Shelf, Products

for cls in Slot, Shelf, Products:
    admin.site.register(cls)