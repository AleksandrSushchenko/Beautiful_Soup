import requests
from bs4 import BeautifulSoup


html = requests.get('https://2ip.ru').text

bs = BeautifulSoup(html, features='html5lib')
tag = bs.find(id='d_clip_button')
span_ip=tag.find('span')
print(span_ip)
ip_adress=span_ip.text
print(ip_adress)
