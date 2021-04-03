# Python 샘플 코드 #


from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus
from bs4 import BeautifulSoup
from lxml import html
encoding_key="rY4chndDGvR7J7ySsylID7pLRVCKXNf0jylzH46QtdMMH0/4p5c7RudppsDgySk7zFajk/RVPTTFmFqEdrwpvw=="
url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : encoding_key, quote_plus('pageNo') : '1', quote_plus('numOfRows') : '10', quote_plus('startCreateDt') : '20200410', quote_plus('endCreateDt') : '20200410' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
xmlobj = BeautifulSoup(response_body, 'lxml-xml')
rows= xmlobj.findAll('item')
data={}
for item in rows:
    data[item.gubun.text]=item.defCnt.text

print(data)