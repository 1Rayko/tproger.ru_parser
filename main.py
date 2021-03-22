import requests
from bs4 import BeautifulSoup
import datetime

now = datetime.datetime.now()
URL = 'https://tproger.ru'

HEADERS={
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.206'
}
r=requests.get(URL,headers=HEADERS)
if r.status_code == 200:
	page = r.text
	soup = BeautifulSoup(page, 'html.parser')
	items = soup.find_all('a',class_="article-link")
	#print(items)
	i=0
	data=[]
	for j in items:
		data.append(items[i].get('href'))
		#'title': item.find('a',class_='c-events__name').get_text(strip=True),
		#print('link',item.find('a',class_='article-link').get('href'))
		i+=1
	with open('data.txt', 'a+', encoding='utf-8') as g:
		g.write(f'данные с сайта на сегодня( {str(now)}) {data}')