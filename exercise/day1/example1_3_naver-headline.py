import requests
from bs4 import BeautifulSoup

#데이터 가져오기(HTML)
res = requests.get('https://news.naver.com/')
print(res)

#soup 객체 만들기
soup = BeautifulSoup(res.text, 'html.parser')

#데이터를 발라내어 가공하기
first = soup.select_one('#today_main_news > div.hdline_news > ul > li:nth-child(1) > div.hdline_article_tit > a').text
second = soup.select_one('#today_main_news > div.hdline_news > ul > li:nth-child(2) > div.hdline_article_tit > a').text
third = soup.select_one('#today_main_news > div.hdline_news > ul > li:nth-child(3) > div.hdline_article_tit > a').text
print(first, second, third )

#리스트로 변환해보자
headline_list = [first.strip(), second.strip(), third.strip()]

print(headline_list)
