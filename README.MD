# ПАРСЕР САЙТА
https://productcenter.ru/producers/

## Порядок работы с парсером:
1) Открыть файл find_cards_in_product_site.py, и внести в переменную BASE_URL_ADS ссылку на сайт с учётом установленного фильтра по геолокации. Запустить этот файл и указать количество страниц с карточками товаров (при желании можно подпилить этот момент для автоматического определения, я не стал тратить время, мне и так норм для моих задач.). По итогу в файл product_cards_url_list.txt будут собраны ссылки на карточки производителей
2) Открыть и Запустить скрипт take_contact_info.py, он соберет информацию о контактах производителей в отдельный contact_information.txt файл.
3) Открыть и запустить скрипт work_with_contact_info.py, он соберёт в отдельные файлы: phone_number_list.txt и mail_list.txt построчно номера телефонов и адреса электронных почтовых ящиков производителей. ВНИМАНИЕ возможен такой расклад, что у производителя в графе "Телефон" было указано 2 или более номеров, в этом случае в txt файле они будут указаны не совсем корректно, обратить на это внимание (при желании можете допилить скрипт, я это может сделаю чуть позже, если мне будет это необходимо).
