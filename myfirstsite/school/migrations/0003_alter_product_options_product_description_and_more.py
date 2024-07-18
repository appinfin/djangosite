# Generated by Django 5.0.3 on 2024-06-28 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_product_foto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['price'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default=False, verbose_name='Наличие'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, max_length=9, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_name',
            field=models.CharField(max_length=64, verbose_name='Наименование товара'),
        ),
    ]