# from bs4 import BeautifulSoup
# import requests
#
# if __name__ == '__main__':
#     target = 'http://sqs.sf-airlines.com/simqueryapp/#/trainingQuery'
#     user_agent = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
#     headers = {'User-Agent': user_agent}
#     req = requests.get(url = target, headers=headers)
#     html = req.text
#     bf = BeautifulSoup(html, "lxml")
#     texts = bf.find_all('div', class_ = 'card-student.card-student-external')
#     print(texts)

# 导入需要的模块
from bs4 import BeautifulSoup
import urllib.request
import csv

# 把网址 URL 存在变量里
urlpage =  'http://sqs.sf-airlines.com/simqueryapp/#/trainingQuery'

# 获取网页内容，把 HTML 数据保存在 page 变量中
page = urllib.request.urlopen(urlpage)
# 用 Beautiful Soup 解析 html 数据，
# 并保存在 soup 变量里
soup = BeautifulSoup(page, 'html.parser')
print(soup)

# 在表格中查找数据
table = soup.find('table', attrs={'class': 'card-teacher card-teacher-external'})
results = table.find_all('教员:')
print('Number of results', len(results))