#!/usr/bin/env python
from django.db import models


class MyShop(models.Model):
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    product = models.CharField(max_length=40, null=False, verbose_name='Продукт')
    image = models.ImageField(upload_to="Изображения", null=False, blank=True)
    specifications = models.TextField(max_length=500, null=False, blank=True, verbose_name='Характеристики')
    about = models.TextField(max_length=500, null=True, verbose_name='Об товаре')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=True, default=0, verbose_name='Цена')
    availability = models.BooleanField(null=False, default=True, blank=True,  verbose_name='Наличие тавара')
    discount = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=True, default=0,
                                   verbose_name='Скидка')
    create_time = models.DateTimeField(auto_now_add=True, db_index=True, blank=True,  verbose_name='Созданно')
    update_time = models.DateTimeField(auto_now_add=False, db_index=True, verbose_name='Обновленно')
    type = models.ForeignKey('Type', null=True, blank=True, on_delete=models.PROTECT, verbose_name='Тип')
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.PROTECT, verbose_name='Категория')
    sub_category = models.ForeignKey('SubCategory', null=True, blank=True, on_delete=models.PROTECT,
                                     verbose_name='Под категория')

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['-update_time']
    

class Type(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Тип')
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Тип'
        verbose_name = 'Тип'
        ordering = ['name']


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категория'
        verbose_name = 'Категория'
        ordering = ['name']


class SubCategory(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Под категория')
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name='Под категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Под категория'
        verbose_name = 'Под категорияы'
        ordering = ['name']


class LiveSales(models.Model):
    seller_id = models.CharField(max_length=30, verbose_name='Номер продавец')
    sails = models.ForeignKey('Sails', null=True, on_delete=models.PROTECT, verbose_name='Данные продовца')


class Sails(models.Model):
    name = models.CharField(max_length=10, db_index=True, verbose_name='Имя продавца')
    last_name = models.CharField(max_length=20, db_index=False, verbose_name='Фамилия продовца')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Фамилия продовца'
        verbose_name = 'Фамилия продовца'
        ordering = ['last_name']

