Вопрос 1
Что выведет на консоль следующая программа:


languages = ["Java", "Python", "Javascript", "C++", "C#"]
for lang in languages[:]:
    languages.remove(lang)

print(languages)

Варианты ответов:

- ["Java", "Python", "Javascript", "C++", "C#"]

- []

- Будет сгенерировано исключение

- Ничего из выше перечисленного


Вопрос 2
Что выведет на консоль следующая программа:

try:
    letters = ["a", "b"]
    print(letters[2])
except (ValueError, IndexError):
    print("Error")

Варианты ответов:

Index Error

Syntax Error

2

Error


Вопрос 3
Что выведет на консоль следующая программа:


numbers = [1, 2, 3, 4]
for idx, item in enumerate(numbers):
    del item
print(numbers)

Варианты ответов:

[1, 3]

[]

[2, 4]

[1, 2, 3, 4]

Ничего из выше перечисленного


Вопрос 4

Что выведет на консоль следующая программа:

li = ["A"]
li.extend("BCD")
print(li)


Варианты ответов:

["A", "BCD"]

["A", "B", "C", "D"]

["ABCD"]

Программа сгенерирует ошибку


Вопрос 5

Что выведет на консоль следующая программа:


def func(x, y=None):
    if y is None:
        y = [1]
    y.extend(x)
    return y


print(func([0], [2, 4, 5]))

Варианты ответов:

[2, 4, 5, [0]]

[1, 2, 4, 5, [0]]

[0, 2, 4, 5]

[0, 1, 2, 4, 5]

[2, 4, 5, 0]

Программа сгенерирует ошибку

Вопрос 6
Что выведет на консоль следующая программа:


numbers = [1, 2, 3, 4, 5]
print(2.0 in numbers, end=" ")
print("2" in numbers)

Варианты ответов:

True True

False False

True False

False True

Программа сгенерирует ошибку

Вопрос 7

Что выведет на консоль следующая программа:


numbers = [1, 2, 3, 4, 5]
print(numbers[:4].pop())

Варианты ответов:

[1, 2, 3, 4]

5

[1, 2, 3, 5]

4

1

Вопрос 8

Что выведет на консоль следующая программа:

items = [5, "t", 5.6, 3, "Python"]
print(3.0 in items, end=" ")
print(bool(items[-2:-4]))

Варианты ответов:

True True

False False

True False

False True

Вопрос 8

Что выведет на консоль следующая программа:


items = [5, "t", 5.6, 3, "Python"]
print(3.0 in items, end=" ")
print(bool(items[-2:-4]))

Варианты ответов:

True True

False False

True False

False True


Вопрос 10

Что выведет на консоль следующая программа:


li = ["in", "as", "if", "be"]
print(li[1:][:2])

Варианты ответов:

"in", "as", "if", "be"

"as", "if"

"in", "as"

"in", "as", "if"

"if", "be"

"as", "if", "be"


Вопрос 11

Что выведет на консоль следующая программа:


li = [10, 20, 30, 40]
li[1:3] = [50]
print(li)

Варианты ответов:

[10, 50, 30, 40]

[10, 50, 50, 40]

[50, 50]

[10, 50, 40]

[50]

Вопрос 12

Что выведет на консоль следующая программа:


arr = []
print(arr * 2)
Варианты ответов:

[]

[][]

None

Будет ошибка
