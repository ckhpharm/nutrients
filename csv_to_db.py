# https://wave1994.tistory.com/89 참고
import csv
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE","nutrients.settings")
django.setup()

from multivitamin.models import Product

CSV_PATH = r'C:\Users\khcho\Desktop\nutrients\final_table.csv'
# csv file read and trans to django db
with open(CSV_PATH, newline='') as csvfile:
    data_reader = csv.DictReader(csvfile)
    for row in data_reader:
        print(row)
        Product.objects.create(
            name = row['name'],
            vitE = float(row['vitE']),
            coQ10 = float(row['coQ10']),
            bisbenthiamine = float(row['bisbenthiamine']),
            fursulthiamine = float(row['fursulthiamine']),
            benfothiamine = float(row['benfothiamine']),
            pyridoxine = float(row['pyridoxine']),
            magnesium = float(row['magnesium']),
            manganese = float(row['manganese']),
            choline = float(row['choline']),
            riboflavin = float(row['riboflavin']),
            vitC = float(row['vitC']),
            vitB5 = float(row['vitB5']),
            vitB12 = float(row['vitB12']),
            calcium = float(row['calcium']),
            biotin = float(row['biotin']),
            vitD3 = float(row['vitD3']),
            molybdenum = float(row['molybdenum']),
            betacarotene = float(row['betacarotene']),
            chondroitin = float(row['chondroitin']),
            selenium = float(row['selenium']),
            royaljelly = float(row['royaljelly']),
            ursodeoxycholicacid = float(row['ursodeoxycholicacid']),
            inositol = float(row['inositol']),
            ferrum = float(row['ferrum']),
            vitB3 = float(row['vitB3']),
            folicacid = float(row['folicacid']),
            zinc = float(row['zinc']),
            gammaoryzanol = float(row['gammaoryzanol']),
            butyrated_vitB2 = float(row['butyrated_vitB2']),
            pyridoxalphosphate = float(row['pyridoxalphosphate']),

        )