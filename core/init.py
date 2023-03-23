import json
import os
import random

import django

from config import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.store.models import Product, Category

with open(f'{settings.BASE_DIR}/resources/products.json', encoding='utf8') as json_file:
    for item in json.load(json_file):
        product = Product()
        product.name = item['name']
        product.code = item['code']
        product.category = Category.objects.get_or_create(name=item['category'])
        product.price = float(item['price'])
        product.pvp = float(item['pvp'])
        product.stock = random.randint(50, 150)
        product.save()
        print(f'record inserted product {product.id}')
