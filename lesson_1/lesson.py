# коментар

# вивід данних 
print("Hello word!")

# створення змінної
a = 5
print(a)

# назва змінної
fio_stud = ""
fioStud = "ivanov"
cours = 2
ser_bal = 3.7

# табуляції та розриви рядків
# \n з нового рядка
# \t табуляція
# \n\t текст з нового рядка, на початку розташовується
# табуляція.
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# методи string

# перетворює перший символ кожного слова у рядку до верхнього регістру
fioStud.title()

# усі символи рядка можна
# перетворити до верхнього або нижнього регістру
fioStud.upper()
fioStud.lower()

# форматтуваня string
print(f'Студент {fioStud.title()} вчиться на {cours} курсі')

# sep
print("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", sep="-")

# вивід float
print('%.2f'%ser_bal)

# ввід даних
# int
s_r = int(input('Скільки років'))
# float
v = float(input('Яка вага'))
print(s_r)

# математичні обчислення + - * **(ступень) /
print(17 / 3) # виведе 5.66666666667
print(17 // 3) # виведе 5
print(17 % 3) # виведе 2

#бібліотека math
import math

x = math.ceil(4.2)
y = math.ceil(4.8)
print(x)
print(y)

# не потрібно вказувати math 
from math import ceil

x = 7 / 2
y = ceil(x)
print(y)

#Округлення
#int(x)           Округлює число убік нуля. Це стандартна функція, її використовувати не потрібно підключати модуль math.
# round(x)        Округлює число до найближчого цілого. Якщо дробова частина числа дорівнює 0.5, число округляється до найближчого парного числа.
# round(x, n)     Округлює число x до знаків n після точки. Це стандартна функція, її використовувати не потрібно підключати модуль math.
# floor(x)        Округлює число вниз («підлога»), при цьому floor(1.5) == 1, floor(-1.5) == -2
# ceil(x)         Округлює число вгору («стеля»), при цьому ceil(1.5) == 2, ceil(-1.5) == # -1
# abs(x)          Модуль (абсолютна величина). Це стандартна функція.

# Коріння, логарифми
# sqrt(x)         Квадратний корінь
# log(x)          Натуральний логарифм. При виклику у вигляді log(x, b)повертає       логарифм на основі b.

# Тригонометрія
# sin(x)          Синус угла, що задається в радіанах
# cos(x)          Косинус кута, що задається в радіанах
# tan(x)          Тангенс кута, що задається в радіанах
# asin(x)         Арксинус повертає значення в радіанах
# acos(x)         Арккосинус повертає значення в радіанах
# atan(x)         Арктангенс повертає значення в радіанах
# atan2(y, x)     Перетворює кут, заданий у радіанах, градуси
# degrees(x)      Полярний кут (радіани) точки з координатами (x, y).
# radians(x)      Перетворює кут, заданий у градусах, на радіани.
# pi              Константа π = 3.1415...