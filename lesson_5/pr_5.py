# title = "Володар кілець"

# def favourite_book(title):
#   print(f"Одна з моїх улюблених книг {title}")

# favourite_book(title)

# from math import sqrt

# def func(x):
#     return (sqrt(x) + x) / 2

# x = func(6) + func(13) + func(21)

# print(x)

# def count_digits(number):
#     count = 0

#     number_str = str(number)

#     for digit in number_str:
#         if digit.isdigit():
#             count += 1

#     return count

# number1 = 12345
# number2 = 987654

# count1 = count_digits(number1)
# count2 = count_digits(number2)

# if count1 > count2:
#     print(f"{number1} має більше цифр.")
# elif count2 > count1:
#     print(f"{number2} має більше цифр.")
# else:
#     print(f"{number1} та {number2} мають однакову кількість цифр.")

# my_list = list(range(21))


# def calculate_sum(lst):
#     count = 0
#     for i in lst:
#         count += i
#     return count


# if calculate_sum(my_list) % 2 == 0:
#     print("Сума елементів списку є парним числом")


# sum_of_squares = calculate_sum([i**2 for i in my_list])


# def is_five_digit_number(number):
#     if len(str(number)) == 5:
#         print("Число є п'ятизначним")
#     else:
#         print("Число не є п'ятизначним")


# is_five_digit_number(sum_of_squares)

from math import sqrt

list1 = list(range(21))

def sqrt_more_than_10(list):
    for i in range(len(list)):
        if i > 10:
            list[i] = sqrt(list[i])

sqrt_more_than_10(list1)

print(list1)


list2 = list(range(21))

def double_change_abs(list):
    for i in range(len(list)):
        if i % 2 == 0:
            list[i] = abs(list[i])

double_change_abs(list2)

print(list2)
