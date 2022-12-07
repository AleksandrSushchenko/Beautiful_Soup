import  requests
from bs4 import BeautifulSoup
from fake_headers import Headers

headers = Headers(browser='chrome', os='wim')
print(headers.generate())

HH_SP = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

def get_page(url):

    return requests.get(url, headers=headers.generate())

def parser_vakans(vacan_tag):
    link = vacan_tag.find(class_="serp-item__title")['href']
    # zp = vacan_tag.find('span').find('data-qa="vacancy-serp__vacancy-compensation"').find(class_="bloko-header-section-3")
    company = vacan_tag.find(class_="vacancy-serp-item__meta-info-company").find('a').text
    city = vacan_tag.find(class_="bloko-text").find_parent().text
    return {
        'link': link,
        # 'ZP': zp
        'company': company,
        'city': city
    }

def main():
    main_html = get_page(HH_SP).text
    soup = BeautifulSoup(main_html, features='html5lib')
    vakans = soup.find_all('div', class_="serp-item")
    for vakan in vakans:
        parsed = parser_vakans(vakan)
        print(parsed)

if __name__ == '__main__':
    main()