from django.db import models

class Slot(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField()
    temperature = models.IntegerField()

    def __str__(self):
        return f'{self.name} with temp: {self.temperature}*C'

    class Meta:
        db_table = 'slot'

class Shelf(models.Model):
    id = models.UUIDField(primary_key=True)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(id)

    class Meta:
        db_table = 'shelf'

class Products(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField()
    expires = models.DateField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'products'