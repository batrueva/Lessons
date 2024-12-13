'''
Конвертация типов данных . Функции type(), int(), float(), str()
int, float --> str - можно
str --> int, float - нельзя
'''
game_count = 21
print(type(game_count))

person1_weight = 121.25
print(type(person1_weight))

# Функция int примеры

inc_count = "2256"
print(type(inc_count))
print(inc_count)

inc_count = int(inc_count)
print(type(inc_count))
print(inc_count)

# Функция float
inc_count = "2256"
print(type(inc_count))
print(inc_count)

inc_count = float(inc_count)
print(type(inc_count))
print(inc_count)

# Функция str
inc_count = 2256
print(type(inc_count))
print(inc_count)

inc_count = str(inc_count)
print(type(inc_count))
print(inc_count)

my_data = "Что-нибудь"
my_data = int(my_data)