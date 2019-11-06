import requests
from bs4 import BeautifulSoup

#데이터 가져오기(HTML)
res = requests.get('https://news.naver.com/')
print(res)

#soup 객체 만들기
soup = BeautifulSoup(res.text, 'html.parser')

#데이터를 발라내어 가공하기
li_list = soup.select('#today_main_news > div.hdline_news > ul > li')
#print(li_list[0])

#반복문으로 뭔가를 해보자
headlines = []
for li in li_list:
    # today_main_news > div.hdline_news > ul > li:nth-child(2) > div.hdline_article_tit > a
    headlines.append(li.select_one('div:nth-child(1) > a').text.strip())

print(headlines)
