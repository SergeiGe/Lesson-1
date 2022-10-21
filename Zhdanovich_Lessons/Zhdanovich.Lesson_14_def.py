# 1. Калькулятор. Каждая операция - это отдельная функция. Сам калькулятор оформить через while True
# Обработать деление на ноль. Для выхода из калькулятора использовать знак 'e'.
# print("Вы работаете в калькуляторе, введите числа, \nесли хотите выйти из калькулятора введите латинскую 'e'.")


def factorial(chislo1):
    if chislo1 == 0: return 1
    return factorial(chislo1-1) * chislo1


def addition(chislo1, chislo2):
    summa = chislo1 + chislo2
    return summa


def subtraction(chislo1, chislo2):
    raznost = chislo1 - chislo2
    return raznost


def multiplication(chislo1, chislo2):
    proizvedenie = chislo1 * chislo2
    return proizvedenie


def division(chislo1, chislo2):
    chastnoe = chislo1 / chislo2
    return chastnoe

def whole_part(chislo1, chislo2):
    w = chislo1 // chislo2
    return w

def remainder(chislo1, chislo2):
    r = chislo1 % chislo2
    return r


def exponentiation(chislo1, chislo2):
    expon = chislo1 ** chislo2
    return expon


while True:
    chislo1 = float(input('Введите число: '))
    sign = input('Введите операцию (+ - * / // % ** n!) или e для выхода: \n')
    if sign == 'n!':
        chislo1 = int(chislo1)
        print('Факториал: ', factorial(chislo1))
        continue
    if sign == 'e':
        print('Выход из калькулятора')
        break
    chislo2 = float(input('Введите число: '))
    if sign == '+':
        print('Сумма: ', addition(chislo1, chislo2))
    elif sign == '-':
        print('Разность: ', subtraction(chislo1, chislo2))
    elif sign == '*':
        print('Произведение: ', multiplication(chislo1, chislo2))
    elif sign == '/':
        if b == 0:
            print('Нельзя делить на 0!')
            continue
        print('Частное: ', division(chislo1, chislo2))
    elif sign == '//':
        if b == 0:
            print('Нельзя делить на 0!')
            continue
        print('Целая часть от деления: ', whole_part(chislo1, chislo2))
    elif sign == '%':
        if b == 0:
            print('Нельзя делить на 0!')
            continue
        print('Остаток от деления: ', remainder(chislo1, chislo2))
    elif sign == '**':
        print(chislo1, ' в степени ', chislo2, ' равняется: ', exponentiation(chislo1, chislo2))
    else:
        print('Ошибка!')



# 2. С помощью генератора создать список десяти чисел от 0 до 1000. Функция принимает этот список как аргумент
# и вычисляет среднее значение.

# import random
# s = [random.randint(0, 1000) for i in range(10)]
# #s = [1, 2, 3, 4, 5]
# print(s)
#
# def average(spisok):
#     a = sum(spisok)/len(spisok)
#     return a
#
# print('Среднее значение списка: ',average(s))