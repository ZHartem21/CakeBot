# Generated by Django 4.1.3 on 2022-11-28 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake_orders', '0011_remove_order_client_delivery_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='recipient_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='recipient name'),
        ),
    ]
