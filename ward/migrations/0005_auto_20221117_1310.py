# Generated by Django 3.2.9 on 2022-11-17 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ward', '0004_auto_20221116_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='slot',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ward',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='wardbooking',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
