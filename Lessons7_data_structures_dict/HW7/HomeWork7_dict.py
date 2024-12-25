'''
Задания к уроку 6. Словари
'''

# 1. Выведите значение возраста из словаря person.
person = {"name": "Kelly", "age": 25, "city": "New york"}
# требуемый вывод:
# 25


# 2. Значениями словаря могут быть и списки.
# Допишите словарь с ключами BMW, ВАЗ, Tesla
# и списками из 3х моделей в качестве значений.
models_data = {..., "Tesla": ["Modes S", ...]}
print(models_data["Tesla"][0])
# требуемый вывод:
# Modes S

# 3. Исправьте ошибки в коде, что бы получить требуемый вывод.
d1 = {"a": 100. "b": 200. "c": 300}
d2 = {a: 300, b: 200, d: 400}
print(d1["b"] == d2["b"])
# требуемый вывод:
# True