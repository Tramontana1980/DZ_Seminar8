


class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt


def name_data():
    is_valid_first_name = False # переменная с названием является допустимым именем
    while not is_valid_first_name: # пока не является ложью 
        try: # пробовать
            first_name = input("Введите имя: ") # вводим первое имя
            if len(first_name) < 2: # если длина имени меньще 2 символов
                raise NameError("Имя должно быть более двух символов") # вызывает ошибку не валидное имя
            else: # в противном случае
                is_valid_first_name = True # переменная правда
        except NameError as err:
            print(err) # печатает вызванную ошибку вызывает код ошибки и печатает ошибку
            continue
        
    return first_name

def surname_data():
    is_valid_surname = False # переменная с названием является допустимым именем
    while not is_valid_surname: # пока не является ложью 
        try: # пробовать
            surname = input("Введите Фамилию: ") # вводим первое имя
            if len(surname) < 2: # если длина имени меньще 2 символов
                raise NameError("Фамилия должна быть более двух символов") # вызывает ошибку не валидное имя
            else: # в противном случае
                is_valid_surname = True # переменная правда
        except NameError as err:
            print(err) # печатает вызванную ошибку вызывает код ошибки и печатает ошибку
            continue
        
    return surname

def phone_data():
    is_valid_phone = False # тоже самое ниже проверяем правильность ввода телефонного номера
    while not is_valid_phone:
        try:
            phone_number = int(input("Введите номер из 11 цифр: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Неверная длина номера")
            else:
                is_valid_phone = True
        except ValueError:
            print("Не валидный номер!!!")
            continue
        except LenNumberError as err:
            print(err)
            continue
    return phone_number

def address_data():
    adress = input('Введите ваш адрес: ' ) 
    return adress