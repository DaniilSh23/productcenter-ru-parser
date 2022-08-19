

def search_phone_numbers():
    '''Функция для поиска телефонных номеров в строках файла.'''

    with open('contact_information.txt', 'r', encoding='utf-8') as file:
        for i_line in file:

            # сбор из файла номеров телефонов в отдельный файл
            if i_line.startswith('Телефон') or i_line.startswith('WhatsApp'):
                phone_number = '+'
                for i_symb in i_line:
                    if i_symb.isdigit():
                        phone_number = ''.join([phone_number, i_symb])
                with open('phone_numbers_list.txt', 'a', encoding='utf-8') as phone_file:
                    phone_number = ''.join([phone_number, '\n'])
                    phone_file.write(phone_number)

            # Сбор из файла мэйлов в отдельный файл
            elif i_line.startswith('Электронная почта'):
                company_mail = i_line.split()[2]
                with open('mail_list.txt', 'a', encoding='utf-8') as mail_file:
                    company_mail = ''.join([company_mail, '\n'])
                    mail_file.write(company_mail)


def main():
    search_phone_numbers()


if __name__ == '__main__':
    main()
