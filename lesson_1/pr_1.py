# ПРИМИЧАНИЕ! код нужно разкоментировать и вставить его в свой файл

# ЗАДАНИЕ 5-8

# ПРИМЕР КИРИЛЛА

# your_first_name = input('Ваше ім`я: ')
# your_last_name = input('Ваше прізвище: ')

#   виводимо прізвищем та ім'ям з привітанням з заглавної букви
# print(f'Вітаю, {your_last_name.title()} {your_first_name.title()}')

# ПРИМЕР МАКСИМА

# в переменную full_name получаем имя и фамилию
# full_name = input("Введите ваше имя и фамилию:")

# выводим в консоль приветсвие, а затем имя и фамилию с большой буквы
# print(f'Hello! {full_name.title()}')


# ЗАДАНИЕ 9

# ПРИМЕР КИРИЛЛА

#   Ця програма зчитує три числа і виводить їхню суму:

# a = int(input())
# b = int(input())
# c = int(input())
# print(a + b + c)


# ПРИМЕР МАКСИМА

# эти переменные сохраняються числа, которые мы ввели в консоли

# first_value = int(input("Введите первое число:"))
# second_value = int(input("Введите второе число:"))
# thirth_value = int(input("Введите третье число:"))

# числа, которые мы вписали строчка 38,39,40 складываем

# print(f'Ответ:{first_value + second_value + thirth_value}')


# ЗАДАНИЕ 10

# ПРИМЕР КИРИЛЛА

# num = 3.0678
# remainder = num % 1
# print(remainder)
# print(f'0.{int(remainder * 1000)}')

# ПРИМЕР МАКСИМА (с функцией, сложнее)

# def print_remainder(num):   <-- название функции "print_remainder" поменяйте на другое
#     remainder = num % 1  <-- название переменной "remainder" поменяйте на другое
#     print(f'0.{int(remainder * 1000)}')

# print_remainder(3.0678) <-- как поменяете название функции "print_remainder" на 58 строчке, измените на этой строчке функцию на ту которую поменяли на 58 строке

# ЗАДАНИЕ 11

# ПРИМЕР КИРИЛЛА 10 ВАРИАНТ 

import math

x = float(input("Your number:"))

z_1 = (x ** 2 + (2 * x) - 3 + (x + 1) * math.sqrt((x ** 2) - 9)) / (x ** 2 - (2 * x) - 3 + (x - 1) * math.sqrt((x ** 2) - 9))

z_2 = math.sqrt(
  (x + 3) / (x - 3)
)

print(f"z1 = {z_1}, z2 = {z_2}")

