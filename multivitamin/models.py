from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=30)
    nicotineacid = models.FloatField(null=True)
    riboflavin = models.FloatField(null=True)
    benfotiamin = models.FloatField(null=True)
    biotin = models.FloatField(null=True)
    zinc = models.FloatField(null=True)
    cyanocobalamin = models.FloatField(null=True)
    udca = models.FloatField(null=True)
    inositol = models.FloatField(null=True)
    choline = models.FloatField(null=True)
    tocopherol = models.FloatField(null=True)
    pantothenicacid = models.FloatField(null=True)
    folicacid = models.FloatField(null=True)
    pyridoxine = models.FloatField(null=True)
    selenium = models.FloatField(null=True)
    ascrobicacid = models.FloatField(null=True)

    def __str__(self):
        return self.name
