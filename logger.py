
from csv import DictReader, DictWriter 
from data_create import name_data, surname_data, phone_data, address_data


file_name = 'phone.csv'

"""Получаем номер строки исключения"""
class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

"""Получаем наименование ошибки"""
class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt

"""Функция создания файла"""
def create_file(file_name): 

    with open(file_name, "w", encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон', 'Адрес']) # заголовки в файле txt
        f_writer.writeheader()


"""Фугкция чтения файла"""
def read_file(file_name): 
    with open(file_name, "r", encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader) # Возвращаем каждый список каждой строки файла



"""Функция получения информации у пользователя"""
def get_info(): 
    name = name_data() # Функция имени, которую будем брать из  файла data_create
    surname = surname_data() # Функция фамилии, которую будем брать из  файла data_create
    phone = phone_data() # Функция номера телефона, которую будем брать из  файла data_create
    address = address_data() # Функция адреса, которую будем брать из  файла data_create

    return [name,surname,phone,address] # возвращаем из функции значения Имени Фамилии Номера телефона и адреса

"""Функция добавления данных в файл"""
def create_data(file_name, lst): # функция записи. вводные файл и список
    res = read_file(file_name) # вызов файла на чтение при помощи функции чтения и присваиваем переменной результат
    for el in res: # для каждого элемента в списке
        if el["Телефон"] == str(lst[2]): 
            #"""# если значение поля с именем телефон совпадает со значением с индексом 2 - последнее"""
            print('Такой телефон уже есть')
            return # тогда выводится такой телефон уже есть
            
    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2], "Адрес": lst[3]} # создаем словаь и записываем данные из списка
    res.append(obj) # в переменную добавляем результат чтения списка
    with open(file_name, 'a', encoding='utf-8', newline='') as data: # открываем фал для записи
        f_writer = DictWriter(data, fieldnames=['Имя', 'Фамилия', 'Телефон','Адрес'])
        f_writer.writerow(obj) # записываем ряды списка результат в файл
        # writer.writerows(rows):Метод writer.writerows() запишет все строки rows, которые должны находится в 
        # итерируемом объекте в файловый объект, отформатированный в соответствии с текущим диалектом csv.Dialect.

"""Функция вывода дланных из файла"""
def print_data(file_name):
    data = read_file(file_name)
    a=sum(1 for e in data if isinstance(e, dict))
    columns = [key for key in data[0]]
    # печать таблицы с колонками максимальной длинны строки 20
    # печать шапки таблицы
    for column in columns:
        print(f'{column:{20}}', end='')
    print()
    # печать разделителя шапки
    print(f'{"="*20*5}')
    # печать тела таблицы
    for i in range(a):
        for j in range(4):
            print(f'{data[i][columns[j]]:{20}}', end='')
        print()


   
        


"""Функция пориска данных"""
def search_data(file_name):
    print(
        'Выберите вариант поиска:\n'
        '1. По имени:\n' 
        '2. По фамилии:\n'
        '3. По номеру телефона:\n' 
        '4. По адресу (Город):')    
    command = input('и введите номер варианта   ')
    while command not in ('1', '2', '3', '4'): 
        print("Неправильный ввод варианта, номер должен быть от 1 до 4 \n")
        command = input('введите номер варианта   ')        
    search = input('Введите данные для поиска:    ')
    res = read_file(file_name)
    res2 = []
    print(f'{'Номер контакта':{20}}',f'{'Имя':{20}}',f'{'Фамилия':{20}}',f'{'Телефон':{20}}',f'{'Адрес'}')
    print()
    j=0
    i=1
    print ('Найденные контакты:')
    for el in res: # для каждого элемента в списке
        if el["Имя"].lower() == search.lower() and command == '1' or el["Фамилия"].lower() == search.lower() and command == '2' or el["Телефон"] == search and command == '3' or el["Адрес"].lower() == search.lower() and command == '4':             
            print(f'{i:{20}}', f'{el["Имя"]:{20}}',f'{el["Фамилия"]:{20}}',f'{el["Телефон"]:{20}}',f'{el["Адрес"]:{20}}')
            obj = {"Номер контакта": i, "Имя": el["Имя"], "Фамилия": el["Фамилия"], "Телефон": el["Телефон"], "Адрес": el["Адрес"]} # создаем словаь и записываем данные из списка
            res2.append(obj) # в переменную добавляем результат чтения списка
            i+=1
            j+=1
    if j==0:
        print('0 \r')
    return res2     
    


def change_data(file_name): 
    data = read_file(file_name)
    old_contact = search_data(file_name)
    command = len(old_contact)
    i = 1
    
    if command > 1:
        i = int(input('Введите номер контакта который хотите изменить:      '))
        while i < 1 or i > command:
            print(f'Неправильный ввод, номер должен быть от 1 до {command} \n')
            i = int(input('введите номер контакта для изменения   '))       
    
    print('')
    print('Введите новые данные контакта')
    
    for el in old_contact:
        for k, v in el.items():
            if k == 'Номер контакта' and v==i:
                r = el.setdefault('Телефон')
              
    new_contact = get_info()
    
    for el in data:
        for k, v in el.items():
            if k == 'Телефон' and v == r:
                    el['Имя'] = new_contact[0]
                    el['Фамилия'] = new_contact[1]
                    el['Телефон'] = new_contact[2]
                    el['Адрес']= new_contact[3]

    with open(file_name, 'w', encoding='utf-8', newline='') as f: # открываем фал для записи
        f_writer = DictWriter(f, fieldnames=['Имя', 'Фамилия', 'Телефон','Адрес'])
        f_writer.writeheader()
        f_writer.writerows(data)
    print('Контакт изменен!')
    return 
    
           
            
"""функция удаления данных"""
def delete_data(file_name): 
    data = read_file(file_name)
    old_contact = search_data(file_name)
    command = len(old_contact)
    
    i = int(input('Введите номер контакта который хотите удалить:      '))
    
    while i < 1 or i > command:
        print(f'Неправильный ввод, номер должен быть от 1 до {command} \n')
        i = int(input('введите номер контакта для удаления   '))  
        
    for el in old_contact:
        for k, v in el.items():
            if k == 'Номер контакта' and v == i:
                r1 = el.setdefault('Имя')
                r2 = el.setdefault('Фамилия')
                r3 = el.setdefault('Телефон')
                r4 = el.setdefault('Адрес')

    for el in data:
        if el['Имя'] == r1 and el['Фамилия'] == r2 and el['Телефон'] == r3 and el['Адрес'] == r4:
            el.pop('Имя')
            el.pop('Фамилия')
            el.pop('Телефон')
            el.pop('Адрес') 
    
    data2 = [x for x in data if x]

    with open(file_name, 'w', encoding='utf-8', newline='') as f: # открываем фал для записи
        f_writer = DictWriter(f, fieldnames=['Имя', 'Фамилия', 'Телефон','Адрес'])
        f_writer.writeheader()
        f_writer.writerows(data2)
    print('Контакт удален!')
    
