'''
Конвертация типов данных . Функции type(), int(), float(), str()
int, float --> str - можно
str --> int, float - нельзя
'''
# game_count = 21
# print(type(game_count))

# person1_weight = 121.25
# print(type(person1_weight))

# # Функция int примеры

# inc_count = "2256"
# print(type(inc_count))
# print(inc_count)

# inc_count = int(inc_count)
# print(type(inc_count))
# print(inc_count)

# # Функция float
# inc_count = "2256"
# print(type(inc_count))
# print(inc_count)

# inc_count = float(inc_count)
# print(type(inc_count))
# print(inc_count)

# # Функция str
# inc_count = 2256
# print(type(inc_count))
# print(inc_count)

# inc_count = str(inc_count)
# print(type(inc_count))
# print(inc_count)

# error
# my_data = "Что-нибудь"
# my_data = int(my_data)


'''
Консольный вывод

'''
# # Функция print() примеры
# #  Выводит на отдельной строке
# print("Hello World")
# print("Hello METANIT.COM")
# print("Hello Python")

# # print(значение, end = конечные_символы) - параметр end
# print("Hello World", end=" ")
# print("Hello METANIT.COM", end=" ")
# print("Hello Python")

# print("Hello World", end=" and ")
# print("Hello METANIT.COM", end=" and ")
# print("Hello Python")

# def value(items):
#     for item in items:
#         print(item, end=' ')
# value([1,2,3,4])  

# file — файлоподобный объект (поток).
# file = open('print.txt','a+')
# def value(items):
#     for item in items:
#         print(item, file=file, end=' ')
#     file.close()  # закройте файл после работы с ним.

# value([1,2,3,4,5,6,7,8,9,10])

# sep — это может быть строка, которую необходимо вставлять между значениями, по умолчанию — пробел.
# \n перенесет каждое слово на новую строку
# print('Hello', 'World', 'Python', 'print()', sep='\n')

'''
Консольный ввод

'''
# # Функция input() примеры
# name = input("Enter your name: ")
# print(f"Your name: {name}")


# name = input("Your name: ")
# age = input("Your age: ")
# print(f"Name: {name}  Age: {age}")
# print(f"Name: {type(name)}  Age: {type(age)}")

'''
Арифметические операции

'''
## Сложение:
# print(6 + 2)  # 8

## Вычитание:
# print(6 - 2)  # 4

## Умножение:
# print(6 * 2)  # 12

## Деление:
# print(6 / 2)  # 3.0

## Целочисленное деление двух чисел:
# print(7 / 2)  # 3.5 
# print(7 // 2)  # 3 Данная операция возвращает целочисленный результат деления, отбрасывая дробную часть

## Возведение в степень:
# print(6 ** 2)  # Возводим число 6 в степень 2. Результат - 36

## Получение остатка от деления:
# print(7 % 3)  # Получение остатка от деления числа 7 на 2. Результат - 1

## Приоритет операций
'''
При последовательном использовании нескольких арифметических операций их выполнение производится в соответствии с их приоритетом.
В начале выполняются операции с большим приоритетом. Приоритеты операций в порядке убывания приведены в следующей таблице.
Операции Направление

**  Справо налево

* / // %  Слева направо

+ -  Слева направо

'''

# number = 3 + 4 * 5 ** 2 + 7
# print(number)  # 110

## Чтобы переопределить порядок операций, можно использовать скобки:
# number = (3 + 4) * (5 ** 2 + 7)
# print(number)

## Если в одной операции участвует целое число (int) и число с плавающей точкой (float), то целое число приводится к типу float
# number = (3 + 4) * (5 ** 2 + 7)
# print(number)

'''
Арифметические операции с присвоением
Ряд специальных операций позволяют использовать присвоить результат операции первому операнду:

+= Присвоение результата сложения

-= Присвоение результата вычитания

*= Присвоение результата умножения

/= Присвоение результата от деления

//= Присвоение результата целочисленного деления

**= Присвоение степени числа

%= Присвоение остатка от деления
'''
# number = 10
# number += 5
# print(number)  # 15
 
# number -= 3
# print(number)  # 12
 
# number *= 4 //=  **= %=
# print(number)  # 48
'''
Округление и функция round
'''
# first_number = 2.0001
# second_number = 5
# third_number = first_number / second_number
# print(third_number) # 0.40002000000000004

# first_number = 2.0001
# second_number = 0.1
# third_number = first_number + second_number
# print(round(third_number))  # 2

# first_number = 2.0001
# second_number = 0.1
# third_number = first_number + second_number
# print(round(third_number, 4))  # 2.1001

## округление до целого числа
# print(round(2.49))  # 2 - округление до ближайшего целого 2
# print(round(2.51))  # 3

# print(round(2.5))   # 2 - ближайшее четное
# print(round(3.5))   # 4 - ближайшее четное

## Округление производится до ближайшего кратного 10 в степени минус округляемая часть:
## округление до двух знаков после запятой
# print(round(2.554, 2))      # 2.55
# print(round(2.5551, 2))      # 2.56
# print(round(2.554999, 2))   # 2.55
# print(round(2.499, 2))      # 2.5

'''
В Python в связи с тем, что десятичная часть числа не может быть точно представлена в виде числа float,
то это может приводить к некоторым не совсем ожидаемым результатам. Например:
Подобно о проблеме можно почитать
https://docs.python.org/3/tutorial/floatingpoint.html#tut-fp-issues
'''
## округление до двух знаков после запятой
# print(round(2.545, 2))   # 2.54
# print(round(2.555, 2))   # 2.56 - округление до четного
# print(round(2.565, 2))   # 2.56
# print(round(2.575, 2))   # 2.58
 
# print(round(2.655, 2))   # 2.65 - округление не до четного
# print(round(2.665, 2))   # 2.67
# print(round(2.675, 2))   # 2.67

'''
Поразрядные операции с числами

'''
## Двоичное представление чисел
number = 5 # в двоичной форме 101
print(f"number = {number:0b}")  # number = 101

number = 0b101  # определяем число в двоичной форме
print(f"number = {number:0b}")  # number = 101
print(f"number = {number}")  # number = 5 - в десятичной системе

number1 = 1 # в двоичной системе 0b1
print(f"number = {number1:0b}")
number2 = 2 # в двоичной системе 0b10
print(f"number = {number2:0b}")
number3 = 3 # в двоичной системе 0b11
print(f"number = {number3:0b}")
number4 = 4 # в двоичной системе 0b100
print(f"number = {number4:0b}")
number5 = 5 # в двоичной системе 0b101
print(f"number = {number5:0b}")
number6 = 6 # в двоичной системе 0b110
print(f"number = {number6:0b}")

## Логические операции
## Логические операции выполняются над отдельными разрядами числа. В Python есть следующие логические операции:

## &(логическое умножение)
## Умножение производится поразрядно, и если у обоих операндов значения разрядов равно 1, то операция возвращает 1, иначе возвращается число 0.
## Например:

# x1 = 2  # 010
# y1 = 5  # 101
# z1 = x1 & y1
# print(f"z1 = {z1}")   # z1 = 0
 
# x2 = 4  # 100
# y2 = 5  # 101
# z2 = x2 & y2
# print(f"z2 = {z2}")   # z2 = 4
# print(f"z2 = {z2:0b}")  # z2 = 100

## | (логическое сложение)

# x1 = 2      # 010
# y1 = 5      # 101
# z1 = x1|y1  # 111
 
# print(f"z1 = {z1}")     # z1 = 7
# print(f"z1 = {z1:0b}")  # z1 = 111
 
# x2 = 4          # 100
# y2 = 5          # 101
# z2 = x2 | y2    # 101
# print(f"z2 = {z2}")     # z2 = 5
# print(f"z2 = {z2:0b}")  # z2 = 101

## ^ (логическое исключающее ИЛИ/XOR)

# x = 9       #  1001
# y = 5       #  0101
# z = x ^ y   #  1100
# print(f"z = {z}")       # z = 12
# print(f"z = {z:0b}")   # z = 1100

## данную операцию применяют для простого шифрования:
# x = 45       # Значение, которое надо зашифровать - в двоичной форме 101101
# key = 102    # Пусть это будет ключ - в двоичной форме 1100110
 
# encrypt = x ^ key    # Результатом будет число 1001011 или 75
# print(f"Зашифрованное число: {encrypt}")
 
# decrypt = encrypt ^ key    # Результатом будет исходное число 45
# print(f"Расшифрованное число: {decrypt}")

## ~(инверсия). Выражение ~x фактически аналогично -(x+1). Например:
# x = 5
# y = ~x;
# print(f"y: {y}")  # -6

'''
Операции сдвига
Операции сдвига также производятся над разрядами чисел. Сдвиг может происходить вправо и влево.
x<<y - сдвигает число x влево на y разрядов. 
x>>y - сдвигает число x вправо на y разрядов
'''

# a = 16 # в двоичной форме 10000
# b = 2 
# c = a << b  # Сдвиг числа 10000 влево на 2 разряда, равно 1000000 или 64 в десятичной системе
# print(c)   #64
 
# d = a >> b  #Сдвиг числа  10000  вправо на 2 разряда, равно 100 или 4 в десятичной системе
# print(d)   #4

# a = 22 # в двоичной форме 10110
# b = 2
# c = a << b  # Сдвиг числа 10110 влево на 2 разряда, равно 1011000 или 88 в десятичной системе
# print(c)   # 88
 
# d = a >> b  # Сдвиг числа 10110 вправо на 2 разряда, равно 101 или 5 в десятичной системе
# print(d)   # 5