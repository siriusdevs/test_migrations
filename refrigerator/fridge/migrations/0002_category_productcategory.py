# Generated by Django 4.1.7 on 2023-03-20 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fridge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fridge.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fridge.product')),
            ],
            options={
                'db_table': 'product_category',
            },
        ),
    ]
