"""
4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо
выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень!
ВНИМАНИЕ: использование встроенной функции = задание не принято
Постараться придумать свой алгоритм без **
"""

#tack_4

def my_func(x, y):
    my_degree = x
    for i in range(-y-1):
        my_degree *= x
    return 1/my_degree

try:
    x = float(input("Введите действительное положительное число х: "))
    y = int(input("Введите целое отрицательное число y: "))
    print(f"Возведение числа {x} в степень {y} дает результат {my_func(x, y)}")
except ValueError:
    print("Неверной ввод")
