# Generated by Django 3.1.7 on 2021-06-18 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multivitamin', '0006_remove_product_benfotiamin'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='imagePath',
            field=models.CharField(default='img/impactamin.jpg', max_length=100),
        ),
    ]
