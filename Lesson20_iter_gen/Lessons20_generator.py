"""
Генераторы
"""


def get_pow(from_num: int, to_num: int):
    # result = []
    while from_num <= to_num:
        # result.append(from_num ** 2)
        yield from_num ** 2
        from_num += 1
    # return  result


g = get_pow(1, 10)  # создание генераторного объекта
print(g)

sq1 = next(g)
sq2 = next(g)
sq3 = next(g)

print(f"Sq1 = {sq1}, sq2 = {sq2}, sq3 = {sq3}")

#


def gen_number(from_num: int, to_num: int):

    while from_num <= to_num:
        yield from_num
        from_num += 1


def gen_pow(from_num: int, to_num: int):

    for i in gen_number(from_num, to_num):
        if i % 2 == 0:
            yield i ** 2


g = gen_pow(1, 10)
sq1 = next(g)
sq2 = next(g)
sq3 = next(g)

print(f"Sq1 = {sq1}, sq2 = {sq2}, sq3 = {sq3}")

#


def gen_number(from_num: int, to_num: int):

    while from_num <= to_num:
        yield from_num
        from_num += 1


def gen_pow(number_iterator):

    for i in number_iterator:
        if i % 2 == 0:
            yield i ** 2


g = gen_pow(gen_number(1, 10))
sq1 = next(g)
sq2 = next(g)
sq3 = next(g)

print(f"Sq1 = {sq1}, sq2 = {sq2}, sq3 = {sq3}")
#

# Пример шифрования через генераторы


def gen_file_parts(path: str):
    with open(path, 'rb') as f:
        data = f.read()
        pos = 0
        while pos < len(data):
            # data = f.read(1)
            yield data[pos: pos + 8]
            pos += 8


def gen_crypted(file_parts_iter):
    for ch in file_parts_iter:
        yield int.to_bytes(int.from_bytes(ch, byteorder='little') ^ 0xfe, length=8, byteorder='little')


def gen_write_encrypted(result_path, encrypted_paths_iter):
    with open(result_path, 'wb') as f:
        for ch in encrypted_paths_iter:
            f.write(ch)


file_parts_gen = gen_file_parts('.\Lesson20_iter_gen\Screenshot_1.jpg.enc')
crypt_gen = gen_crypted(file_parts_gen)
encrypted_write_gen = gen_write_encrypted(
    '.\Lesson20_iter_gen\dec_Screenshot_1.jpg', crypt_gen)
print('done')
