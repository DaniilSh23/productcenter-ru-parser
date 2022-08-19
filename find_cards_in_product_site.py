import requests
from bs4 import BeautifulSoup


BASE_URL_ADS = 'https://productcenter.ru/producers/r-kaluzhskaia-obl-174/page-'


def product_cards(req_result):
    '''Парсинг ссылок на производителей со страницы'''

    soup = BeautifulSoup(req_result, 'lxml')
    product_cards = soup.find_all(class_='ci_main')

    with open('product_cards_url_list.txt', 'a', encoding='utf-8') as product_cards_file:
        for i_card in product_cards:
            product_cards_url = i_card.find(class_='image').find('a').get('href')
            print(product_cards_url)
            product_cards_file.write(f'{product_cards_url}\n')


def req_to_site(number_of_pages):
    '''Функция для запроса к страницами сайта с производителями.'''
    for i_number in range(1, number_of_pages + 1):
        url_ads = f'{BASE_URL_ADS}{i_number}'
        req_result = requests.get(url=url_ads).content
        product_cards(req_result)


def main():
    number_of_pages = int(input('Введите количество страниц с карточками производителей:  '))
    req_to_site(number_of_pages)


if __name__ == '__main__':
    main()
