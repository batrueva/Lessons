# '''
# Открытие и закрытие файлов
# open(file, mode) r, w, a, b, rb, wb, r+, w+, a+
# '''

from datetime import timedelta, datetime
from datetime import timedelta

from datetime import datetime
from datetime import time
from datetime import date

from zipfile import ZipFile, ZIP_DEFLATED
from zipfile import ZipFile
import shelve
import pickle
import csv


# myfile = open("hello.txt", "w")

# myfile = open("image.png", "wb")

myfile = open("hello.txt", "w")

myfile.close()

try:
    myfile = open("hello.txt", "w")
    try:
        print("Работа с файлом")
    finally:
        myfile.close()
except Exception as ex:
    print(ex)

'''
with open(file, mode) as myfile:
    инструкции
'''

with open("hello.txt", "w") as myfile:
    print("Work with myfile")

'''
Запись в текстовый файл
'''

with open("hello.txt", "w") as file:
    file.write("hello world")

print("File write")
#
with open("hello.txt", "a") as file:
    file.write("\nhello work")

print("Файл изменен")
#
lines = ["Hello Word\n", "Hello Work\n", "Hello World\n"]
with open("hello2.txt", "a") as file:
    file.writelines(lines)

print("Список строк записан в файл")

#

with open("hello.txt", "a") as myfile:
    print("\nhello metanit.com", file=myfile)

'''
Чтение файла
'''
#
with open("hello.txt", "r") as file:
    for line in file:
        print(line)

#

with open("hello.txt", "r") as file:
    for line in file:
        print(line, end="")

#
with open("hello.txt", "r") as file:
    str1 = file.readline()      # считываем первую строку
    print(str1, end="")
    str2 = file.readline()      # считываем вторую строку
    print(str2)


#
with open("hello.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()

#
with open("hello.txt", "r") as file:
    content = file.read()
    print(type(content))
    print(content)
#
with open("hello.txt", "r") as file:
    contents = file.readlines()
    str1 = contents[0]
    str2 = contents[1]
    print(str1, end="")
    print(str2)
#
filename = "hello.txt"
with open(filename, encoding="utf8") as file:
    text = file.read()


'''
Чтение и запись
'''

with open("hello.txt", "w+") as file:
    file.write("Hello world\nHello work\n")  # сначала записываем данные
    file.seek(0)        # перемещаемся к первому байту в файле
    content = file.read()   # считываем данные
    print(content)


'''
Перемещение по файлу
file.seek(n)
'''
with open("hello.txt", "w+") as file:
    file.write("Hello world\n")  # сначала записываем данные
    file.seek(6)                # перемещаемся к шестому байту в файле
    content = file.read()       # считываем данные
    print(content)      # world


'''
Пример
'''

# имя файла
FILENAME = "messages.txt"

# запись строки в файл


def write():
    message = input("Введите строку: ")
    with open(FILENAME, "a") as file:
        file.write(message + "\n")

# чтение файла файл


def read():
    with open(FILENAME, "r") as file:
        for message in file:
            print(message, end="")
    print()  # перевод строки для разделения меню и вывода


while (True):
    selection = int(
        input("1.Запись в файл\t\t2.Чтение файла\t\t3.Выход\nВыберите действие: "))
    match selection:
        case 1: write()
        case 2: read()
        case 3: break
        case _: print("Некорректный ввод")

print("Программа завершена")

'''
Файлы CSV
'''

FILENAME = "users.csv"

users = [
    ["Tom", 28],
    ["Alice", 23],
    ["Bob", 34]
]

with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)


with open(FILENAME, "a", newline="") as file:
    user = ["Sam", 31]
    writer = csv.writer(file)
    writer.writerow(user)

'''
Работа со словарями
'''

FILENAME = "users2.csv"

users = [
    {"name": "Tom", "age": 28},
    {"name": "Alice", "age": 23},
    {"name": "Bob", "age": 34}
]

with open(FILENAME, "w", newline="") as file:
    columns = ["name", "age"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()

    # запись нескольких строк
    writer.writerows(users)

    user = {"name": "Sam", "age": 41}
    # запись одной строки
    writer.writerow(user)

with open(FILENAME, "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], "-", row["age"])

'''
Бинарные файлы
'''
FILENAME = "forest.png"             # файл для чтения
NEWFILENAME = "forest_new.png"      # файл для записи

image_data = []     # список для хранения считанных данных

# считываем файл в список image_data
with open(FILENAME, "rb") as file:
    image_data = file.read()

# запись выше считанных байт в новый файл
with open(NEWFILENAME, "wb") as file:
    file.write(image_data)

print(f"Файл {FILENAME} скопирован в {NEWFILENAME}")

'''
Модуль pickle
'''

FILENAME = "user.dat"

name = "Tom"
age = 19

with open(FILENAME, "wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)

with open(FILENAME, "rb") as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print("Имя:", name, "\tВозраст:", age)

#

FILENAME = "users.dat"

users = [
    ["Tom", 28, True],
    ["Alice", 23, False],
    ["Bob", 34, False]
]

with open(FILENAME, "wb") as file:
    pickle.dump(users, file)


with open(FILENAME, "rb") as file:
    users_from_file = pickle.load(file)
    for user in users_from_file:
        print("Имя:", user[0], "\tВозраст:",
              user[1], "\tЖенат/замужем:", user[2])

'''
Модуль shelve

open(путь_к_файлу[, flag="c"[, protocol=None[, writeback=False]]])
'''
#
d = shelve.open(filename)
d.close()
#

FILENAME = "states2"
with shelve.open(FILENAME) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"

with shelve.open(FILENAME) as states:
    print(states["London"])
    print(states["Madrid"])

'''
Чтение данных   
'''
#
with shelve.open(FILENAME) as states:
    key = "Brussels"
    if key in states:
        print(states[key])
#
with shelve.open(FILENAME) as states:
    state = states.get("Brussels", "Undefined")
    print(state)
#
with shelve.open(FILENAME) as states:
    for key in states:
        print(key, " - ", states[key])

#
with shelve.open(FILENAME) as states:

    for city in states.keys():
        print(city, end=" ")        # London Paris Berlin Madrid
    print()
    for country in states.values():
        print(country, end=" ")     # Great Britain France Germany Spain

#
with shelve.open(FILENAME) as states:

    for state in states.items():
        print(state)
'''
Обновление данных

'''

FILENAME = "states2"
with shelve.open(FILENAME) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"

with shelve.open(FILENAME) as states:

    states["London"] = "United Kingdom"
    states["Brussels"] = "Belgium"
    for key in states:
        print(key, " - ", states[key])

'''
Удаление данных

'''
#
with shelve.open(FILENAME) as states:

    state = states.pop("London", "NotFound")
    print(state)
#
with shelve.open(FILENAME) as states:

    del states["Madrid"]    # удаляем объект с ключом Madrid


#
with shelve.open(FILENAME) as states:

    states.clear()
