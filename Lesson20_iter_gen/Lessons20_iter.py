"""
Итераторы
"""

# https://docs-python.ru/standart-library/modul-typing-python/
from typing import List

list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i)  # -> 1 2 3 4 5

# iterator = iter(list)
# print(iterator)
# l1 = next(iterator)
# print(l1)
# l2 = next(iterator)
# print(l2)
# l3 = next(iterator)
# print(l3)
# l4 = next(iterator)
# print(l4)
# l5 = next(iterator)
# print(l5)
#


def get_pows(from_num: int, to_num: int) -> List[int]:
    result = []
    while from_num <= to_num:
        result.append(from_num ** 2)
        from_num += 1
    return result


# print(get_pows(1, 10))  # без проблем
# print(get_pows(1, 100000000))  # в чем тут проблема?
