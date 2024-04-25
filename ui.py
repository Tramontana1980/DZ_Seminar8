from logger import create_file, create_data, get_info, print_data, search_data, change_data, delete_data

from os.path import exists # функция проверки на отсутствие файла ниже

file_name = 'phone.csv'
    

command = ' '

"""Меню основного интерфейса"""
def menu():
    print(
        'Выберите вариант дальнейшего действия:\n'
        '1. Добавить контакт:\n' 
        '2. Вывести на экран:\n'
        '3. Поиск контакта:\n'
        '4. Изменение контактов:\n'
        '5. Удаление контактов:\n'
        '6. Выход:')    
    command = input('и введите номер варианта   ')
    return   command

  
"""Интерфейс"""
def interface(): # Функция общения
        
    print("Добрый день!Вы попали на специальной бот справочник от GeekBrains!")
    command = ' ' 
    while command != '4':    
        command = menu()
        while command not in ('1', '2', '3', '4', '5', '6'): 
            print("Неправильный ввод варианта, номер должен быть от 1 до 6 \n")        
            command = menu()
        if (command=='1' or command == '2' or command == '3' or command == '4' or command =='5') and not exists(file_name):
            create_file(file_name) 
        match command:
            case '1': 
                create_data(file_name, get_info()) #Функция ввода данных
            case '2': 
                print_data(file_name) #Функция вывода данных
            case '3': 
                search_data(file_name) #Функция поиска данных
            case '4': 
                change_data(file_name) #Функция изменрения данных
            case '5': 
                delete_data(file_name) #Функция удаления данных
            case '6':
                print('До свидания!') #Функция поиска данных
                return



    


