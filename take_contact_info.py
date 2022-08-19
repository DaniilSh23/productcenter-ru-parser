from selenium import webdriver
from selenium.webdriver.common.by import By


def req_to_product_page(url):
    browser = webdriver.Chrome(executable_path='./chromedriver')
    try:
        browser.get(url)
        browser.find_element(by=By.CLASS_NAME, value='tab_contacts').click()
        contact_information = browser.find_element(by=By.CLASS_NAME, value='contact_information')
        with open('contact_information.txt', 'a', encoding='utf-8') as contact_file:
            print('Запись в файл информации об очередном производителе')
            contact_file.write(f'{"=" * 20}\n{contact_information.text}\n{"=" * 20}\n\n')

    except Exception as err:
        print(f'Хьюстон, у нас проблемы!!!\n\n {err}')

    finally:
        browser.close()
        browser.quit()


def main():
    with open('product_cards_url_list.txt', 'r', encoding='utf-8') as file_with_links:
        for i_line in file_with_links:
            print(f'https://productcenter.ru{i_line}')
            req_to_product_page(url=f'https://productcenter.ru{i_line}')



if __name__ == '__main__':
    main()
