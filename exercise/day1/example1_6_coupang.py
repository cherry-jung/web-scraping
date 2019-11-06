import requests
from bs4 import BeautifulSoup
import pprint

#데이터 가져오기(HTML)
##쿠팡은 스크래핑 방지기술이 적용되어있어서 헤더를 사람이 하는것처럼 변조 해 주어야 한다.
headers = {
    'user-agent'    :   'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    'referer'       :   'https://www.coupang.com/np/campaigns/82'
}
res = requests.get('https://www.coupang.com/np/campaigns/82/components/194176?listSize=60&brand=&offerCondition=&filterType=&isPriceRange=false&minPrice=&maxPrice=&page=1&channel=user&fromComponent=N&selectedPlpKeepFilter=&sorter=bestAsc&filter=&component=194176&rating=0',
                   headers=headers)
print(res)

#soup 객체 만들기
soup = BeautifulSoup(res.text, 'html.parser')

soup.select('#productList > li')
#print(soup)
#print(len(soup.select('#productList > li')))

product_list = []
for idx, li in enumerate(soup.select('#productList > li')) :
    #print(idx)
    #print(li.select_one('a > dl > dd > div.name').text.strip())
    #print(li.select_one('a > dl > dd > div.price-area > div.price-wrap > div.price > em > strong').text)
    product_list.append(
        [
            li.select_one('a > dl > dd > div.name').text.strip(),
            li.select_one('a > dl > dd > div.price-area > div.price-wrap > div.price > em > strong').text,
            li.select_one('a > dl > dd > div.other-info > div > span.rating-total-count').text
        ]
    )
pprint.pprint(product_list)
