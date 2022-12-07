import requests
from bs4 import BeautifulSoup
from fake_headers import Headers

headers = Headers(browser='chrome', os='win')
print(headers.generate())

HABR = 'https://habr.com'
HABR_ARTICLES=f'{HABR}/ru/all/'

def get_page(url):

    return requests.get(url, headers=headers.generate())

def main():
    main_html = get_page(HABR_ARTICLES).text
    soup = BeautifulSoup(main_html, features='lxml')
    articles = soup.find_all('article')
    print(len(articles))

if __name__ == '__main__':
    main()
