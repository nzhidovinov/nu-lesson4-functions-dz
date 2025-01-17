"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""


def get_year():
    return input('Ввведите год рождения А.С.Пушкина:')


def get_day():
    return input('В какой день июня родился Пушкин?')


def ask_until(q_fn, exit_val):
    val = q_fn()
    while val != exit_val:
        print("Не верно")
        val = q_fn()


ask_until(get_year, '1799')
ask_until(get_day, '6')
print('Верно')


'''
year = input('Ввведите год рождения А.С.Пушкина:')
while year != '1799':
    print("Не верно")
    year = input('Ввведите год рождения А.С.Пушкина:')

day = input('Ввведите день рождения Пушкин?')
while day != '6':
    print("Не верно")
    day = input('В какой день июня родился Пушкин?')
print('Верно')
'''

