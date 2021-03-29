import os
'''예외상황 정리들
1. 피리독신과 피리독살포스페이트 / 리보플라빈과 리보플라빈 부티레이트를 둘다 갖는 제품들이 있어 둘을 구분해주었다.
2. 메가트루 포커스의 경우 칼슘이 침강탄산칼슘과 인산수소칼슘수화물 둘다 있어 수동으로 수정해주었다. (CSV 파일에서)'''
replacements = {'토코페롤아세테이트50%':'vitE', '토코페롤아세테이트 2배산':'vitE',
'유비데카레논' : 'coQ10','유비데카레논10%' : 'coQ10',
'비스벤티아민':'bisbenthiamine', 
'푸르설티아민염산염':'fursulthiamine','푸르설티아민':'fursulthiamine', 
'벤포티아민':'benfothiamine',
'피리독신염산염' : 'pyridoxine', '피리독살포스페이트수화물' : 'pyridoxalphosphate',
'산화마그네슘' : 'magnesium',
'황산망간수화물' : 'manganese',
'콜린타르타르산염': 'choline',
'리보플라빈부티레이트':'butyrated_vitB2', '리보플라빈':'riboflavin',  
'아스코르브산과립97%':'vitC', '제피아스코르브산':'vitC', '아스코르브산':'vitC',
'판토텐산칼슘':'vitB5',
'시아노코발라민1000배산' :'vitB12', '시아노코발라민1%':'vitB12', '시아노코발라민100배산':'vitB12','시아노코발라민':'vitB12' , '히드록소코발라민아세트산염' :'vitB12',  
'무수인산수소칼슘' :'calcium', '인산수소칼슘수화물':'calcium', '침강탄산칼슘':'calcium',
'D-비오틴':'biotin','D-비오틴':'biotin' , 'd-비오틴1%':'biotin', 'd-비오틴':'biotin', '비오틴' : 'biotin',
'콜레칼시페롤과립':'vitD3', '농축콜레칼시페롤 산':'vitD3',
'몰리브덴함유건조효모' : 'molybdenum',
'β-카로틴20%과립':'betacarotene',
'니코틴산아미드' : 'vitB3',
'콘드로이틴설페이트나트륨':'chondroitin',
 '셀레늄함유건조효모':'selenium',
 '로얄젤리' : 'royaljelly',
 '우르소데옥시콜산' : 'ursodeoxycholicacid',
 '이노시톨': 'inositol',
 '푸마르산철' : 'ferrum',
 '폴산' : 'folicacid',
 '산화아연' : 'zinc',
 'γ-오리자놀' : 'gammaoryzanol'
 }
dir = r"C:\Users\khcho\Desktop\nutrients\parsing\product"


for file in os.listdir(dir):
    with open(f'{dir}\{file}') as infile, open(f'moved_{file}', 'w') as outfile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            outfile.write(line)