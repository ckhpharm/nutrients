from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=30)
    vitE = models.FloatField(null=True)
    coQ10 = models.FloatField(null=True)
    bisbenthiamine = models.FloatField(null=True)
    fursulthiamine = models.FloatField(null=True)
    benfothiamine = models.FloatField(null=True)
    pyridoxine = models.FloatField(null=True)
    magnesium = models.FloatField(null=True)
    manganese = models.FloatField(null=True)
    choline = models.FloatField(null=True)
    riboflavin = models.FloatField(null=True)
    vitC = models.FloatField(null=True)
    vitB5 = models.FloatField(null=True)
    vitB12 = models.FloatField(null=True)
    calcium = models.FloatField(null=True)
    biotin = models.FloatField(null=True)
    vitD3 = models.FloatField(null=True)
    molybdenum = models.FloatField(null=True)
    betacarotene = models.FloatField(null=True)
    vitB3 = models.FloatField(null=True)
    chondroitin = models.FloatField(null=True)
    selenium = models.FloatField(null=True)
    royaljelly = models.FloatField(null=True)
    ursodeoxycholicacid = models.FloatField(null=True)
    inositol = models.FloatField(null=True)
    ferrum = models.FloatField(null=True)
    vitB3 = models.FloatField(null=True)
    folicacid = models.FloatField(null=True)
    zinc = models.FloatField(null=True)
    gammaoryzanol = models.FloatField(null=True)
    butyrated_vitB2 = models.FloatField(null=True)
    pyridoxalphosphate = models.FloatField(null=True)
    image = models.ImageField(upload_to='images', null = True, blank = True)



    def __str__(self):
        return self.name
