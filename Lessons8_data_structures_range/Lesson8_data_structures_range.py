'''
Созданиеи диапазонов

range(stop): возвращает все целые числа от 0 до stop

range(start, stop): возвращает все целые числа в промежутке от start (включая) до stop (не включая).

range(start, stop, step): возвращает целые числа в промежутке от start (включая) до stop (не включая), которые увеличиваются на значение step
'''

range(5)            # 0, 1, 2, 3, 4
range(1, 5)         # 1, 2, 3, 4
range(2, 10, 2)     # 2, 4, 6, 8
range(10, 2, -2)    # 10 8 6 4

for i in range(5):
    print(i, end=" ")

# Консольный вывод
# 0, 1, 2, 3, 4

for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print("\n")

# последовательный список чисел
numbers = list(range(10))
print(numbers)      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = list(range(2, 10))
print(numbers)      # [2, 3, 4, 5, 6, 7, 8, 9]
numbers = list(range(10, 2, -2))
print(numbers)      # [10, 8, 6, 4]
