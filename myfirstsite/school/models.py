from django.db import models

# # Create your models here.
class Product(models.Model):
    prod_name = models.CharField(max_length=64, verbose_name='Наименование товара')
    price = models.DecimalField(max_digits=7,
                                decimal_places=2,
                                max_length=9,
                                null=True, blank=True,
                                verbose_name='Цена')
    in_stock = models.BooleanField(default=False, verbose_name='Наличие')
    width = models.PositiveSmallIntegerField()
    heigth = models.PositiveSmallIntegerField()
    foto = models.ImageField(upload_to='photos/%Y/%m/%d/',
                             null=True,
                             blank=True,
                             width_field='width',
                             height_field='heigth')
    description = models.TextField('Описание', max_length=300, null=True, blank=True)
    
    def __unicode__(self):
        return self.prod_name
    
    def __str__(self):
        return self.prod_name
    
    class Meta:
        verbose_name='Товар'
        verbose_name_plural='Товары'
        ordering=['price']