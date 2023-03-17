def read_phonebook():
    file = open('phonebook.txt', encoding='utf-8')
    print(file.read())
    file.close()

def find():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    file = open('phonebook.txt', encoding='utf-8')
    for row in file:
        if last_name and first_name in row:
            print(row)
    if last_name and first_name not in file:
        print('Абонент не найден')
    file.close()

def add_contact():
    file = open('phonebook.txt','a', encoding='utf-8')
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    file.write(f'{last_name} {first_name} {phone_number} \n')
    file.close()

def data_change():
    print('Введите фамилию, имя и номер абонента, которого хотите заменить')
    user = input('Ответ:')
    file = open('phonebook.txt', 'r', encoding='utf-8')
    text = file.read()
    file.close()
    if user in text:
        print('Введите фамилию, имя и номер абонента, которого хотите записать')
        new_user = input('Ответ:')
        file = open('phonebook.txt', 'w', encoding='utf-8') 
        file.write(text.replace(user, new_user))
        file.close() 
    else:
        print('Такой абонент не найден')

def data_delete():
    print('Введите фамилию, имя и номер абонента, которого хотите удалить')
    user = input('Ответ:')
    file = open('phonebook.txt', 'r', encoding='utf-8')
    text = file.readlines()
    file.close()
    for item in text:
        if user in item:
            text.pop(text.index(item))
            new_stroka = ''.join(map(str, text))
            file = open('phonebook.txt', 'w', encoding='utf-8') 
            file.write(new_stroka)
            file.close() 
            break
    else:
        print('Такой абонент не найден')


            
    