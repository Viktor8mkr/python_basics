"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""

#tack_2

def user_param(**param):
    print(f"{param['name']}, {param['last_name']}, {param['brith_year']} года рождения,"
          f" проживающий в городе {param['city']}, email: {param['email']}"
          f" телефон: {param['telepfon']}")

user_param(
    name='Александр',
    last_name='Усик',
    brith_year='1987',
    city='Симферополь',
    email='Alex.usyk@gmail.com',
    telepfon='+79652222145'
)
