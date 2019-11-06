# 작업목록을 만들자
# Flow Summary
# 1. URL 확보 : https://finance.naver.com/sise/
# 2. 받아온 HTML파일에서 코스피 지수를 포함하는 SPAN tag를 찾는다
# 3. 찾아낸 데이터를 확보한다.
# 4. 데이터를 저장한다.

# Flow
# Action. 1
# requests 모듈을 사용하여 가져오자
import requests
res = requests.get('https://finance.naver.com/sise/')
#print(res)
#print(res.text)
html_from_server = res.text


# Action. 2
# 찾는법 1 : css selector를 이용하여 찾거나 XPath 문법을 이용하여 찾는다.
# 찾는법 2 : 정규식을 활용하여 찾는다.

# css selector(chrome의 개발자도구에서 복사해올수 있다.
# #KOSPI_now
# #contentarea > div.box_top_submain2 > div.lft > ul > li:nth-child(1) > a > span.blind

# XPath 문법을 써보자
# //*[@id="contentarea"]/div[1]/div[1]/ul/li[1]

## 내용을 파싱하기위해 beautifulsoup을 이용하여 정제하자
# beautifulsoup4를 찾아 설치
# web-formed HTML로 바꿔보자
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_from_server,'html.parser')
#print(soup)

the_tag = soup.select_one('#contentarea > div.box_top_submain2 > div.lft > ul > li:nth-child(1) > a > span.blind')

# Action. 3
# 찾아온 아이를 데이터를 확보하자
print(the_tag)
print(the_tag.text)




## 실습 2 뉴스의 헤드라인을 가져와보자
res = requests.get('https://news.naver.com/')
html_from_server = res.text
soup = BeautifulSoup(html_from_server,'html.parser')

the_tag = soup.select_one('#today_main_news > div.hdline_news > ul > li:nth-child(1) > div.hdline_article_tit > a')

print(the_tag)
print(the_tag.text.strip())


# Action. 4
# 배열을 이용하여 태그를 가져와보자
