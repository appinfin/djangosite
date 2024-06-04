# Generated by Django 5.0.3 on 2024-06-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=64)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=7, max_length=9, null=True)),
                ('in_stock', models.BooleanField(default=False)),
                ('width', models.PositiveSmallIntegerField()),
                ('heigth', models.PositiveSmallIntegerField()),
                ('foto', models.ImageField(blank=True, height_field=models.PositiveSmallIntegerField(), null=True, upload_to='photos/%Y/%m/%d/', width_field=models.PositiveSmallIntegerField())),
            ],
        ),
    ]
