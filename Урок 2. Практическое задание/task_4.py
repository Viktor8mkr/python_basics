"""
4. Пользователь вводит строку из нескольких слов,
разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если слово длинное,
выводить только первые 10 букв в слове.

Пример:
Введите слова через пробел: раз два три
1. раз
2. два
3. три

Введите слова через пробел: раз перерефрижерированность
1. раз
2. перерефриж
"""

#tack_4

my_list = input("Введите через пробел значения списка: ")
my_list = my_list.split()
n = 1
for i in my_list:
    if len(i) > 10:
        print(f"{n}. {i[0:10]}")
    else:
        print(f"{n}. {i}")
    n = n + 1
