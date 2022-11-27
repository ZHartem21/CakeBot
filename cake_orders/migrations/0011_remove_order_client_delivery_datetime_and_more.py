# Generated by Django 4.1.3 on 2022-11-27 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake_orders', '0010_cake_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='client_delivery_datetime',
        ),
        migrations.RemoveField(
            model_name='order',
            name='forecast_delivery_datetime',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_datetime',
            field=models.DateTimeField(default='2020-01-01', verbose_name='date and time of the delivery'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='', max_length=50, verbose_name='Status of the order'),
            preserve_default=False,
        ),
    ]
