import requests
from bs4 import BeautifulSoup

#데이터 가져오기(HTML)
res = requests.get('http://www.yes24.com/24/category/bestseller?CategoryNumber=001001003&sumgb=06')
print(res)

#soup 객체 만들기
soup = BeautifulSoup(res.text, 'html.parser')
#print(soup)

#데이터를 발라내어 가공하기
result_list = []
for li in soup.select('#category_layout > tr'):
    test_val = li.select_one('td.goodsTxtInfo > p > a:nth-child(1)')
    if test_val is not None :
        print(test_val.text)
        result_list.append(test_val.text)
print('END Loop')
print(result_list)
#print(len(html_list))
#print(html_list)