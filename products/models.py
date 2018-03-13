from django.db import models
from django.utils import timezone


class Catalog(models.Model):
    title = models.CharField('Название каталога', max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'


class Product(models.Model):
    title = models.CharField('Название продукта', max_length=100)
    slug = models.SlugField(max_length=100)
    catalog = models.ForeignKey(Catalog, verbose_name='Каталога', on_delete=models.CASCADE)
    is_import = models.BooleanField('Импортное', default=True)
    count = models.SmallIntegerField('Количество в наличи', default=0)
    shelf_life = models.DateField('Срок годности', default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
