from django.db import models
from django.forms import model_to_dict


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Nombre')

    def __str__(self):
        return self.name

    def toJSON(self):
        return model_to_dict(self)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    code = models.CharField(max_length=20, unique=True, verbose_name='Código')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Categoría')
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00, verbose_name='Precio de Compra')
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['category'] = self.category.toJSON()
        item['price'] = float(self.price)
        return item

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
