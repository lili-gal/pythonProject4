from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(max_length=100, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='Изображение')
    category = models.CharField(max_length=100, verbose_name='Категория')
    purchase_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена за покупку')
    date_of_creation = models.DateField(**NULLABLE, verbose_name='Дата создания')
    last_modified_date = models.DateField(**NULLABLE, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name} {self.description} {self.category}'


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.TextField(max_length=100, verbose_name='Описание')
    created_at = models.DateField(**NULLABLE, verbose_name='Изменения')

    def __str__(self):
        return f'{self.name} {self.description}'


