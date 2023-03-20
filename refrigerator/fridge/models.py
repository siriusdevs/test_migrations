from django.db import models
from uuid import uuid4


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)

    class Meta:
        abstract = True


class Slot(UUIDMixin):
    name = models.TextField()
    temperature = models.IntegerField()

    def __str__(self):
        return f'{self.name} with temp: {self.temperature}*C'

    class Meta:
        db_table = 'slot'


class Shelf(UUIDMixin):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'shelf'

class Product(UUIDMixin):
    name = models.TextField()
    expires = models.DateField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, blank=True, null=True)
    

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'product'


class Category(UUIDMixin):
    name = models.TextField()

    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        db_table = 'category'


class ProductCategory(UUIDMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'product_category'
