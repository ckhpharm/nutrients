# Generated by Django 3.1.4 on 2021-01-09 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multivitamin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ascrobicacid',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='benfotiamin',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='biotin',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='choline',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='cyanocobalamin',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='folicacid',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='inositol',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='nicotineacid',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='pantothenicacid',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='pyridoxine',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='riboflavin',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='selenium',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='tocopherol',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='udca',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='zinc',
            field=models.FloatField(null=True),
        ),
    ]