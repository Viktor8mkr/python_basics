"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна
    выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова
    нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если
    вместо числа вводится специальный символ, выполнение программы завершается. Если специальный
    символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
"""

#tack_5


def my_func(my_summ = 0):

    list = input('Введите числа через пробел, q - выход: ').split()
    for i in range(len(list)):
        if list[i] != "q":
            my_summ = my_summ + int(list[i])
        else:
            break
    print('Cумма чисел равна:', my_summ)
    if "q" in list:
        print("Расчет завершен")
    else:
        my_func(my_summ)
my_func()
