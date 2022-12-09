import re

import  requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import json

headers = Headers(browser='chrome', os='wim')
print(headers.generate())

HH_SP = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

def get_page(url):

    return requests.get(url, headers=headers.generate())

def parser_vakans(vacan_tag):
    link = vacan_tag.find(class_="serp-item__title")['href']
    zp = vacan_tag.find(class_="bloko-header-section-3").find_next_sibling().find_next_sibling().text
    company = vacan_tag.find(class_="vacancy-serp-item__meta-info-company").find('a').text
    city = vacan_tag.find(class_='bloko-v-spacing-container bloko-v-spacing-container_base-2').find_next_sibling().text
    flask = vacan_tag.find(class_="g-user-content").find(text=re.compile('Flask'))
    django = vacan_tag.find(class_="g-user-content").find(text=re.compile('Django'))

    if flask == None:
        flask = False
    else:
        flask = True

    if django == None:
        django = False
    else:
        django = True

    return {
        'link': link,
        'ZP': zp.replace('\u202f', ' '),
        'company': company,
        'city': city.replace('\xa01\xa0','...'),
        'flask': flask,
        'django': django
    }

def write_json (data, file_name):
    data = json.dumps(data)
    data = json.loads(data)
    with open(file_name, 'a', encoding='utf-8') as file:
        json.dump(data, file)
        file.write('\n')

def main():
    main_html = get_page(HH_SP).text
    soup = BeautifulSoup(main_html, features='html5lib')
    vakans = soup.find_all('div', class_="serp-item")
    for vakan in vakans:
        parsed = parser_vakans(vakan)
        if parsed['flask'] == True or parsed['django'] == True:
            print(parsed)
            write_json(parsed, 'vuborka_hh.json')


if __name__ == '__main__':
    main()
