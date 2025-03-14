# Вопрос 1
# Что выведет на консоль следующая программа:


print({key: value for key, value in enumerate("abcd")})

# Варианты ответов:

# {}

# Syntax Error

# {0: 'a', 1: 'b', 2: 'c', 3: 'd'}

# Ничего из выше перечисленного

# Вопрос 2
# Что выведет на консоль следующая программа:


data = {1: "one", 2: "two", 3: "three"}
for key in data:
    print(key, data[key], end=",")

# Варианты ответов:

# 1 one, 2 two, 3 three,

# (1, "one"), (2, "two"), (3, "three"),

# {1: "one", 2: "two", 3: "three",}

# Программа завершится с ошибкой


# Вопрос 3
# Что выведет на консоль следующая программа:


my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict.keys())

# Варианты ответов:

# ["a", "b". "c"]

# [1, 2, 3]

# [("a", 1), ("b", 2), ("c", 3)]

# Ничего из вышеперечисленного
