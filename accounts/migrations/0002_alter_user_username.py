# Generated by Django 4.0.4 on 2022-11-21 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, unique=True, verbose_name='Xodim'),
        ),
    ]
