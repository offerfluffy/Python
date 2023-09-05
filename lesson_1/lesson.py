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

# математичні обчислення
