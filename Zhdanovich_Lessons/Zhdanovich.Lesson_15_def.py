# 1. Написать функцию, которая считает сколько гласных и согласных в строке.
# Строку вводить с клавиатуры.

# stroka = input('Введите строку \n')
#
# def count_glas_soglas(str_):
#     glas = 0
#     soglas = 0
#     for i in str_:
#         if i.lower() in 'аоиыеёэуюяaeiou':
#             glas += 1
#         elif i.isalpha(): soglas += 1
#     return 'Количество гласных:', glas, '\nКоличество согласных:',soglas
#
#
# print(*count_glas_soglas(stroka))
#
# 2. Функцию которая при заданном целом числе n посчитает n + nn + nnn.

# def count_summ(n):
#     return n + n*n + n*n*n
#
# print(count_summ(3))
#
#
# # Рекурсивная функция
# def count_sum_posled(n, st=2):
#     if st == 0:
#         return n
#     else:
#         return n + n * count_sum_posled(n, st-1)
#
# print(count_sum_posled(3))

#
# 3. Вычислить значения нижеприведенной функции в диапазоне значений x от -10 до 10 включительно с шагом, равным 1.
# y = 𝑥 ^2 при -5 <= x <= 5;
# y = 2*|x|-1 при x < -5;
# y = 2x при x > 5.
# Вычисление значения функции оформить в виде программной функции, которая принимает значение x,
# а возвращает полученное значение функции (y).
#
#
# def vychislyayet_funct(x):
#     if -5 <= x <= 5: y = x ** 2
#     elif x < -5: y = 2 * abs(x) - 1
#     elif x > 5: y = 2 * x
#     else: print('Ошибка!')
#     return y
#
# for s in range(-10,11):
#     print('при x =', s, ': y = ', vychislyayet_funct(s))


# 4. Если в функцию передается кортеж, то посчитать, сколько в кортеже строк
#    Если передается список, то посчитать, сколько в нем строк и отдельно сколько чисел
#    Если передается число, то посчитать, сколько нечетных цифр в этом числе
#    Если строка - количество букв
#    Если другой тип данных, то вывести сообщение "Error"
#
# def multi_funct(item):
#     if type(item) == tuple:
#         return 'Количество строк в кортеже:', len(item)
#     elif type(item) == list:
#         number_strok = 0
#         number_chisel = 0
#         for i in item:
#             if type(i) == str: number_strok += 1
#             elif type(i) == int or float: number_chisel += 1
#             return f'Количество строк в списке: {number_strok} \nКоличество чисел в списке: {number_chisel}'
#     elif type(item) == int or float: return f'Количество цифр в числе: {len(str(item))}'
#     elif type(item) == str: return f'Количество букв в строке: {len(item)}'
#     else: return 'Error!'
#
#
#
#
# print(multi_funct([1, 1.23, 'abc', 'ABC', 6.45, 2, 3, 4, 4.98]))
# print(multi_funct(12.3))

# print(type((1,)))
# sp = ['hjhjhj', 1, '2', 4, 'лоолл', 5]
# a = [1, 1.23, 'abc', 'ABC', 6.45, 2, 3, 4, 4.98]
# print(list(map(type, a)).count(int))


# 5. Написать декоратор, который считает, сколько раз в него отправили функцию

# def decorator_count(func):
#     def wrapper(*args, **kwargs):
#         wrapper.count += 1
#         res = func(*args, **kwargs)
#         print(f'В декоратор функция {func.__name__} отправлялась {wrapper.count} раз')
#         return res
#     wrapper.count = 0
#     return wrapper
# @decorator_count
# def add(a, b):
#     return(f'Сумма чисел {a} и {b} равна: {a + b}')
#
# print(add(2, 3))
# print(add(20, 3))
# print(add(20, 30))