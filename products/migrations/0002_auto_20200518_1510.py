# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-18 15:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[("Men's", "Men's"), ("Woman's", "Woman's"), ('Children', 'Children'), ("Souvenir's", "Souvenir's")], default="Men's", max_length=20),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image1',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image2',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image3',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image4',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_image5',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='stock_qty',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]