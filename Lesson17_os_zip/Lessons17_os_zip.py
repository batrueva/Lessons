'''
Модуль OS и работа с файловой системой

mkdir(): создает новую папку

rmdir(): удаляет папку

rename(): переименовывает файл

remove(): удаляет файл
'''

# Создание и удаление папки


# путь относительно текущего скрипта
os.mkdir("hello")
# абсолютный путь
os.mkdir("c://somedir")
os.mkdir("c://somedir/hello")


# путь относительно текущего скрипта
os.rmdir("hello")
# абсолютный путь
os.rmdir("c://somedir/hello")

# Переименование файла

os.rename("C://SomeDir/somefile.txt", "C://SomeDir/hello.txt")

# Удаление файла

os.remove("C://SomeDir/hello.txt")

# Существование файла

filename = input("Введите путь к файлу: ")
if os.path.exists(filename):
    print("Указанный файл существует")
else:
    print("Файл не существует")

'''
Пример
Программа подсчета слов
'''


def get_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(
        ".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words


def get_words_dict(words):
    words_dict = dict()

    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict


def main():
    filename = input("Введите путь к файлу: ")
    if not os.path.exists(filename):
        print("Указанный файл не существует")
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)
        print(f"Кол-во слов: {len(words)}")
        print(f"Кол-во уникальных слов: {len(words_dict)}")
        print("Все использованные слова:")
        for word in words_dict:
            print(word.ljust(20), words_dict[word])


if __name__ == "__main__":
    main()


'''
Запись и чтение архивных zip-файлов

ZipFile(file, mode='r', compression=ZIP_STORED, allowZip64=True, compresslevel=None, *, strict_timestamps=True, metadata_encoding=None)
Параметры:

file: путь к zip-файлу

mode: режим открытия файла. Может принимать следующие значения:

r: применяется для чтения существующего файла

w: применяется для записи нового файла

a: применяется для добавления в файл

compression: тип сжатия файла при записи. Может принимать значения:

ZIP_STORED: архивация без сжатия (значение по умолчанию)

ZIP_DEFLATED: стандартный тип сжатия при архивации в zip

ZIP_BZIP2: сжатие с помощью способа BZIP2

ZIP_LZMA: сжатие с помощью способа LZMA

allowZip64: если равно True, то zip-файл может быть больше 4 Гб

compresslevel: уровень сжатия при записи файла. Для типов сжатия ZIP_STORED и ZIP_LZMA не применяется. Для типа ZIP_DEFLATED допустимые значения от 0 до 9, а для типа ZIP_BZIP2 допустимые значения от 1 до 9.

strict_timestamps: при значении False позволяет работать с zip-файлами, созданными ранее 01.01.1980 и позже 31.12.2107

metadata_encoding: применяется для декодирования метаданных zip-файла (например, коментариев)
'''


'''
Создание и закрытие файла
'''
#

myzip = ZipFile("metanit.zip", "w")

#

myzip = ZipFile("metanit.zip", "w")
myzip.close()

#

with ZipFile("metanit.zip", "w") as myzip:
    pass

'''
Запись файлов в архив
write(filename, arcname=None, compress_type=None, compresslevel=None)
'''
#

with ZipFile("metanit.zip", "w") as myzip:
    myzip.write("hello.txt")

#

with ZipFile("metanit.zip", "a") as myzip:
    myzip.write("hello2.txt")
    myzip.write("forest.jpg")

#

with ZipFile("metanit.zip", "w", compression=ZIP_DEFLATED, compresslevel=3) as myzip:
    myzip.write("hello.txt")

#


with ZipFile("metanit.zip", "a") as myzip:
    myzip.write("hello.txt", "hello1.txt")
    myzip.write("hello.txt", "hello2.txt")
    myzip.write("hello.txt", "hello3.txt")

'''
Получение информации о файлах в архиве
'''
#

with ZipFile("metanit.zip", "a") as myzip:
    print(myzip.infolist())

# infolist() - объект ZipInfo

with ZipFile("metanit.zip", "r") as myzip:
    for item in myzip.infolist():
        print(f"File Name: {item.filename} Date: {
              item.date_time} Size: {item.file_size}")

# is_dir()

with ZipFile("metanit.zip", "r") as myzip:
    for item in myzip.infolist():
        if (item.is_dir()):
            print(f"Папка: {item.filename}")
        else:
            print(f"Файл: {item.filename}")

#  namelist()

with ZipFile("metanit.zip", "r") as myzip:
    for item in myzip.namelist():
        print(item)

#  getinfo() - объект ZipInfo


with ZipFile("metanit.zip", "r") as myzip:
    try:
        hello_file = myzip.getinfo("hello.txt")
        print(hello_file.file_size)
    except KeyError:
        print("Указанный файл отсутствует")

'''
Извлечение файлов из архива
extractall(path=None, members=None, pwd=None)
'''

with ZipFile("metanit.zip", "r") as myzip:
    myzip.extractall()
    # Извлечение в определенную папку
    # myzip.extractall(path="metanit")
    # извлекаем файлы  "hello.txt", "forest.jpg" в папку "metanit2"
    # myzip.extractall(path="metanit2", members=["hello.txt", "forest.jpg"])
    # Извлечение одного файла
    # myzip.extract("hello.txt")

'''
Считывание файла
'''

with ZipFile("metanit.zip", "r") as myzip:
    content = myzip.read("hello5.txt")
    print(content)
'''
Открытие файла
open(name, mode='r', pwd=None, *, force_zip64=False)
'''

with ZipFile("metanit.zip", "a") as myzip:
    # записываем в архив новый файл "hello5.txt"
    with myzip.open("hello5.txt", "w") as hello_file:
        encoded_str = bytes("Python...", "UTF-8")
        hello_file.write(encoded_str)

'''
Работа с датами и временем
Модуль datetime

date
time
datetime
'''

'''
Класс date
date(year, month, day)
'''

yesterday = datetime.date(2017, 5, 2)
print(yesterday)      # 2017-05-02

#

today = date.today()
print(today)      # 2017-05-03
print("{}.{}.{}".format(today.day, today.month, today.year))      # 2.5.2017

'''
Класс time
time([hour] [, min] [, sec] [, microsec])
'''


current_time = time()
print(current_time)     # 00:00:00

current_time = time(16, 25)
print(current_time)     # 16:25:00

current_time = time(16, 25, 45)
print(current_time)     # 16:25:45


'''
Класс datetime
datetime(year, month, day [, hour] [, min] [, sec] [, microsec])
'''
#

deadline = datetime(2017, 5, 10)
print(deadline)     # 2017-05-10 00:00:00

deadline = datetime(2017, 5, 10, 4, 30)
print(deadline)     # 2017-05-10 04:30:00

#

now = datetime.now()
print(now)     # 2017-05-03 11:18:56.239443

print("{}.{}.{}  {}:{}".format(now.day, now.month,
      now.year, now.hour, now.minute))  # 3.5.2017  11:21

print(now.date())
print(now.time())

'''
Преобразование из строки в дату

strptime(str, format)

%d: день месяца в виде числа

%m: порядковый номер месяца

%y: год в виде 2-х чисел

%Y: год в виде 4-х чисел

%H: час в 24-х часовом формате

%M: минута

%S: секунда
'''

deadline = datetime.strptime("22/05/2017", "%d/%m/%Y")
print(deadline)     # 2017-05-22 00:00:00

deadline = datetime.strptime("22/05/2017 12:30", "%d/%m/%Y %H:%M")
print(deadline)     # 2017-05-22 12:30:00

deadline = datetime.strptime("05-22-2017 12:30", "%m-%d-%Y %H:%M")
print(deadline)     # 2017-05-22 12:30:00

'''
Операции с датами
'''
# Фоматирование дат и времени
now = datetime.now()
print(now.strftime("%Y-%m-%d"))             # 2017-05-03
print(now.strftime("%d/%m/%Y"))             # 03/05/2017
print(now.strftime("%d/%m/%y"))             # 03/05/17
print(now.strftime("%d %B %Y (%A)"))        # 03 May 2017 (Wednesday)
print(now.strftime("%d/%m/%y %I:%M"))       # 03/05/17 01:36

#
locale.setlocale(locale.LC_ALL, "")

now = datetime.now()
print(now.strftime("%d %B %Y (%A)"))        # 03 Май 2017 (среда)

'''
Сложение и вычитание дат и времени

timedelta([days] [, seconds] [, microseconds] [, milliseconds] [, minutes] [, hours] [, weeks])
'''
#

three_hours = timedelta(hours=3)
print(three_hours)       # 3:00:00
three_hours_thirty_minutes = timedelta(hours=3, minutes=30)  # 3:30:00

two_days = timedelta(2)  # 2 days, 0:00:00

two_days_three_hours_thirty_minutes = timedelta(
    days=2, hours=3, minutes=30)  # 2 days, 3:30:00

#

now = datetime.now()
print(now)                      # 2017-05-03 17:46:44.558754
two_days = timedelta(2)
in_two_days = now + two_days
print(in_two_days)              # 2017-05-05 17:46:44.558754

#

now = datetime.now()
till_ten_hours_fifteen_minutes = now - timedelta(hours=10, minutes=15)
print(till_ten_hours_fifteen_minutes)

'''
Свойства timedelta

days: возвращает количество дней

seconds: возвращает количество секунд

microseconds: возвращает количество микросекунд
'''


now = datetime.now()
twenty_two_may = datetime(2017, 5, 22)
period = twenty_two_may - now
print("{} дней  {} секунд   {} микросекунд".format(
    period.days, period.seconds, period.microseconds))
# 18 дней  17537 секунд   72765 микросекунд

print("Всего: {} секунд".format(period.total_seconds()))
# Всего: 1572737.072765 секунд

'''
Сравнение дат
'''


now = datetime.now()
deadline = datetime(2017, 5, 22)
if now > deadline:
    print("Срок сдачи проекта прошел")
elif now.day == deadline.day and now.month == deadline.month and now.year == deadline.year:
    print("Срок сдачи проекта сегодня")
else:
    period = deadline - now
    print("Осталось {} дней".format(period.days))
