import os

header = ['name','vitE', 'coQ10', 'bisbenthiamine','fursulthiamine','benfothiamine', 'pyridoxine', 'magnesium','manganese', 'choline','riboflavin','vitC', 'vitB5','vitB12',
'calcium', 'biotin', 'vitD3', 'molybdenum', 'betacarotene', 'vitB3', 'chondroitin','selenium','royaljelly', 'ursodeoxycholicacid',
'inositol', 'ferrum', 'vitB3','folicacid', 'zinc','gammaoryzanol','butyrated_vitB2','pyridoxalphosphate']

dir = r"C:\Users\khcho\Desktop\nutrients\parsing\moved"

# no value ingredient addition with 0.0 value
for ingredient in header:
    for file in os.listdir(dir):
        with open(f'{dir}\{file}', 'r') as fo:    
            if ingredient in fo.read():
                pass
            else:
                with open(f'{dir}\{file}', 'a') as fa:
                    fa.write(f"{ingredient} 0.0 \n")


# value sort depending on header order
for file in os.listdir(dir):
    if f"succesively_{file}" not in os.listdir(dir):
        for ingredient in header:
            with open(f'{dir}\{file}', 'r') as fo:    
                lines = fo.readlines()
                
                for line in lines:
                        if ingredient in line:
                            with open(f'{dir}\succesively_{file}', 'a') as fa:
                                fa.write(line)
                        else:
                            pass
    else:
        pass