# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Products(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField()
    expires = models.DateField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    shelf = models.ForeignKey('Shelf', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Shelf(models.Model):
    id = models.UUIDField(primary_key=True)
    slot = models.ForeignKey('Slot', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shelf'


class Slot(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.TextField()
    temperature = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'slot'
