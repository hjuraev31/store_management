# Generated by Django 4.0.4 on 2022-11-25 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sklad_core', '0005_alter_truck_name_alter_truck_store_emp_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='left',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity_sold',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='summ',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='InfoByDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('month', models.CharField(max_length=128, null=True)),
                ('total', models.IntegerField()),
                ('card', models.IntegerField()),
                ('expenses', models.IntegerField()),
                ('emp_expenses', models.IntegerField()),
                ('un_expenses', models.IntegerField()),
                ('admin_expenses', models.IntegerField()),
                ('admin', models.CharField(choices=[('LA', 'Luqmonjon akaga'), ('AA', 'Abdujalil akaga')], default='LA', max_length=2)),
                ('total_left', models.IntegerField()),
                ('truck_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='sklad_core.truck')),
            ],
        ),
    ]
