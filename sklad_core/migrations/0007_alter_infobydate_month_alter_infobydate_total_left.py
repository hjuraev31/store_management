# Generated by Django 4.0.4 on 2022-11-25 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad_core', '0006_alter_product_left_alter_product_quantity_sold_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infobydate',
            name='month',
            field=models.CharField(default=0, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='infobydate',
            name='total_left',
            field=models.IntegerField(default=0),
        ),
    ]
