# Generated by Django 3.1.7 on 2021-06-18 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multivitamin', '0007_product_imagepath'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='imagePath',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]