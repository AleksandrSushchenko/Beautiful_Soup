import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

headers = Headers(browser='chrome', os='win')
print(headers.generate())

HABR = 'https://habr.com'
HABR_ARTICLES=f'{HABR}/ru/all/'

def get_page(url):

    return requests.get(url, headers=headers.generate())

def parser_articl(artical_tag):
    time = artical_tag.find('time')['datetime']
    title = artical_tag.find('h2').find('span').text
    link = artical_tag.find('a')['href']
    link = f'{HABR}{link}'

    return {
        'time':time,
        'title':title,
        'link':link
    }

def main():
    main_html = get_page(HABR_ARTICLES).text
    soup = BeautifulSoup(main_html, features='lxml')
    articles = soup.find_all('article')
    for arcticl in articles:
        parsed = parser_articl(arcticl)
        print(parsed)

if __name__ == '__main__':
    main()
