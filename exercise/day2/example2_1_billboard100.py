import requests
from bs4 import BeautifulSoup
import pprint

URL = 'https://www.billboard.com/charts/hot-100'
HEADERS = {
        'user-agent'    :   'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
        'referer'       :   'http://www.google.com'
    }

def get_soup():
    # 데이터 가져오기(HTML)
    res = requests.get(URL, headers=HEADERS)
    # print(res)

    # soup 객체 만들기
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup)
    return soup

def main():
    soup = get_soup()

    billboard_list = []
    for li in soup.select('#charts > div > div.chart-list.container > ol > li'):
    # print(len(soup.select('#charts > div > div.chart-list.container > ol > li')))
        #print(li.select_one('button'))
        #print('##############################')
        #print(li.select_one('button > span:nth-child(3) > span:nth-child(3)'))
        #print('========================')
        billboard_list.append([
            li.select_one('button > span.chart-element__information > span.chart-element__information__song.text--truncate.color--primary').text,
            li.select_one('button > span.chart-element__information > span.chart-element__information__artist.text--truncate.color--secondary').text,
            li.select_one('button > span:nth-child(3) > span:nth-child(3)').text
        ])

    pprint.pprint(billboard_list)

main()
