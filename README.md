# Внимание!!!!
# Для запуска программы запускайте код из файла "MAIN"


# Задание

## ПОТОК СОЗНАНИЯ ОБУЧАЮЩЕЙ МАШИНЫ ГИК БРЕЙНС ГЛАСИТ:

## 1. Задание написанное в уроке:

Урок 12. Семинар. Работа с файлами

Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

## 2. Пояснение преподавателя семинаре:
Будем изменять в двух файлах и удалять в двух файлах data_first_variant.csv и data_second_variant.csv
Если хотим изменить данные то будем просить у пользователя его новые данные, которые он хочет изменить 
будем брать эти функции из файлика дата криэйт и после этого будем изменять.
Здесь надо активно пользоваться срезами, то есть мы будем спрашивать номер записи которую он хочет изменить,
и будем в нашу новую переменную записывать записи, которые были до потом вставлять нашу новую переменную 
которую мы хотели изменить и оставлять наши записи которые были после. То есть для начала мы читаем данные, затем
с помощью срезов записываем те или иные данные. 
Если мы хотим удалить данные, то пользователь будем вводить номер записи, которую мы хотим изменить,
и после этого мы будем записывать все записи до и все записи после также при помощи срезов.

## 3. Комментарий Дмитрия Читалова к семинару:
Друзья, ваша задача - взять код из материалов урока (архив ответы) и реализовать следующее. 
Дополнить справочник возможностью копирования данных из одного файла в другой. 
Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

Формат сдачи: ссылка на свой репозиторий в Гитхаб.

## 4. То что было в файле "file_writing" к заданию:
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться в файле.
1) Программа должна выводить данные
2) Программа должна сохранять данные в текстовом файле
3) Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4) Использование функций. Ваша программа не должна быть линейной 

## 5. То как я понял задачу из потока сознания обучающей машины Гик Брейнс:



# Решение задачи. Алгоритм.

## 1. Создание интерфейса:
1.1. Вывод меню на экран +++
1.2. Запросить у пользователя, что он хочет сделать. Вариант действия. +++
1.3. Запустить соответствующую функцию. +++
1.4. Осуществить выход из программы +++
## 2. Создание файла +++
## 3. Добавление контактов: +++
1. Запросить новые контакты у пользователя +++
2. Открыть файл на дозапись "а" оператором with +++
3. Добавить новый контакт +++
## 4. Вывод контактов: +++
1. Открыть файл на чтение в режиме "r" оператором with +++
2. Считать файл +++
3. Вывести на экран +++
## 5. Поиск контакта: 
1. Выбор варианта поиска по телефону, по фамилии, по имени
2. Запрос данных для поиска у пользователя
3. Открыть файл в режиме "r" оператором with
4. Считываем данные в переменную
5. Осуществляем поиск данных в переменной
6. вывести на экран
## 6. Изменение контакта: 
1. Выбор варианта поиска по телефону, по фамилии, по имени и адллресу что хотим изменить
2. Запрос данных для поиска у пользователя
3. Считываем данные в переменную
4. Осуществляем поиск данных в переменной и вызываем функцию записи новых данных
5. Открыть файл в режиме "w" оператором with и перезаписать его
6. вывести на экран "Контакт изменен"
## 7. Удаление контакта: 
1. Выбор варианта поиска по телефону, по фамилии, по имени и адллресу что хотим изменить
2. Запрос данных для поиска у пользователя
3. Считываем дые в переменную
4. Осуществляем поиск данных в переменной и вызываем функцию записи новых данных
5. Открыть файл в режиме "w" оператором with и перезаписать его
6. вывести на экран "Контакт удален"
