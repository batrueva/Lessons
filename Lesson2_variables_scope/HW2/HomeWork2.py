'''
Задания к уроку 2. Конвертация типов данных
'''

# 1. Измените и дополните код,
# что бы переменная salary_type хранила результат функции type() со значением int.
salary = "50000"
salary_type = int(50000)
print(salary_type)
# требуемый вывод:
# <class 'int'>

# 2. Исправьте ошибку в коде, что бы получить требуемый вывод.
mark = "5+"
print(mark, "баллов")
# требуемый вывод:
# 5+ баллов

# 3. Конвертируйте переменные и введите только целые числа через дефис.
score1 = 50.5648
score2 = 23.5501
score3 = 96.560
print()
# требуемый вывод:
# 50-23-96

'''
Задания к уроку 2. Арифметические операции

1. Напишите программу, которая вычисляет процент по банковскому вкладу.
Пусть для вычисления процентов по банковскому вкладу применяется формула (P * R * T) / 100, где:
P – начальная сумма
R – процент по вкладу
T – количество лет



Пользователь вводит эти данные, а программа выводит ему ответ - сумму начисленных процентов. 

Пример работы:
Начальная сумма вклада: 250000
Процент по вкладу: 36
Количество лет: 2
Начисленные проценты: 180000.0
'''

# Решение
P = input("Начальная сумма вклада:")
R = input("Процент по вкладу:")
T = input("Количество лет:")

S = (P * R * T) / 100
print("Начисленные проценты:" S)


'''
2. Напишите программу, в которой пользователь вводит температуру в градусах Цельсия,
 а программа переводит их в градусы Фаренгейта.
 Для перевода применяется формула:
°F= (9/5)*(°C) + 32

Пример работы программы:
Введите температуру в градусах Цельсия: 19
19.0  градусов Цельсия равны  66.2  градусам Фаренгейта
'''
T1 = input Введите температуру в градусах Цельсия:
T2 = (9/5)*(T1) + 32
print(T1 градусов Цельсия равны T2 градусам Фаренгейта)
#Решение