from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import bs4

url = 'http://apis.data.go.kr/1471057/MdcinPrductPrmisnInfoService1/getMdcinPrductIrdntItem'

# 요청 파트로 고정해서 쓰면 되겠다. 비맥스메타정으로 테스트 해보니 주성분 따라 <item>으로 분리 되어있다.
vitBList = ['비맥스메타정', '비맥스액티브정', '비맥스골드정',
'엑세라민비정', '엑세라민엑소정',
'임팩타민프리미엄정', '임팩타민파워정', 
'아로나민골드정', '아로나민씨플러스정',
'벤포벨정',  
'메가트루골드정', '메가트루포커스정',
'렛잇비정']




for prod in vitBList:
    serviceKey = '45fXS0vIomfppKtAWnp2KbUWmW9vj4aJHjYr7DRkJZkAVAciGJ4W4jB9j9nQMGg8b1jLdJr9we6UpoyV9HOkQg=='
    queryParams = '?' + urlencode({ quote_plus('ServiceKey') : serviceKey, quote_plus('Prduct') : prod, quote_plus('numOfRows') : 30})

    request = Request(url + queryParams)
    request.get_method = lambda: 'GET'
    response_body = urlopen(request).read().decode('utf8')

    # xml parsing part using bs4
    xmlobj = bs4.BeautifulSoup(response_body, 'lxml-xml')
    rows = xmlobj.findAll('item')
    rowLen = len(rows)
    
    dir = r"C:\Users\khcho\Desktop\nutrients\parsing\product"
    f = open(f"{dir}\{prod}.txt","w")
    f.write("name " + prod + ' ' +"\n")
    
    for i in range(rowLen):
        columns = rows[i].find_all()
        f.write(columns[5].text + ' ' + columns[6].text + ' ' +'\n')
        
    f.close()

# 어떤 이유에서인지 API 자체에 아로나민 시리즈는 성분명이 중복 기입되어있다. 이건 수동으로 수정해줬다. 
# 공공 API 사이트에 말해줘야 되나
