import requests
from bs4 import BeautifulSoup
import pprint

#데이터 가져오기(HTML)
headers = {
    'user-agent'    :   'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    'referer'       :   'http://www.google.com'
}
res = requests.get('https://www.youtube.com/watch?v=KyNbdxhdnGw', headers=headers)
#print(res)

#soup 객체 만들기
soup = BeautifulSoup(res.text, 'html.parser')
print(soup)

print(soup.select_one('#input-2 > div'))




