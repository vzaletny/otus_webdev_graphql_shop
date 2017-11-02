# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 07:30
from __future__ import unicode_literals

from django.db import migrations


def create_fish_data(apps, schema_editor):
    Product = apps.get_model('products', 'Product')
    Category = apps.get_model('products', 'Category')

    products_data = [
        {'title': 'Macbook Air 2016', 'is_published': True, 'category_id': 1},
        {'title': 'Zenbook', 'is_published': True, 'category_id': 1},
        {'title': 'Samsung A3', 'is_published': True, 'category_id': 2},
    ]

    categories_data = [
        {'title': 'Ноутбуки', 'id': 1},
        {'title': 'Мобильные телефоны', 'id': 2},
    ]

    for category_info in categories_data:
        Category(**category_info).save()
    for product_info in products_data:
        Product(**product_info).save()


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_fish_data),
    ]