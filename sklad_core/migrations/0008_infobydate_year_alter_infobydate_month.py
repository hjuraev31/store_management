# Generated by Django 4.0.4 on 2022-11-26 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad_core', '0007_alter_infobydate_month_alter_infobydate_total_left'),
    ]

    operations = [
        migrations.AddField(
            model_name='infobydate',
            name='year',
            field=models.CharField(max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='infobydate',
            name='month',
            field=models.CharField(max_length=128, null=True),
        ),
    ]