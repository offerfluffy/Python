# 1. Список(масив) — це набір елементів, які йдуть у певному порядку.
bicycles = ["trek", "cannondale", "redline", "specialized"]

# print(bicycles)
# // ['trek', 'cannondale', 'redline', 'specialized']

# 2. Робота з елементами списку
# Індекси починаються з 0

# list[$] - звернення до елементу массива

# print(bicycles[0])
# // trek

# print(bicycles[-1])
# // specialized

# 3. Зміна, додавання та видалення елементів
motorcycles = ["honda", "yamaha", "suzuki"]
# print(motorcycles)
# // ['honda', 'yamaha', 'suzuki']

motorcycles[0] = "ducati"
# print(motorcycles)
# // ['ducati', 'yamaha', 'suzuki']

# 3.1 Приєднання елементів до кінця списку
# .append(data)

# print(motorcycles)
# // ['honda', 'yamaha', 'suzuki']

motorcycles.append("ducati")
# print(motorcycles)
# //['honda', 'yamaha', 'suzuki', 'ducati']

# Динамічне створення масива
motorcyclesEmpty = []

motorcyclesEmpty.append("honda")
motorcyclesEmpty.append("yamaha")
motorcyclesEmpty.append("suzuki")

# print(motorcyclesEmpty)
# // ['honda', 'yamaha', 'suzuki']

# 3.2 Вставлення елементів до списку
# .insert(index, data)

motorcycles.insert(0, "ducati")
# print(motorcycles)
# // ['ducati', 'honda', 'yamaha', 'suzuki']

# 3.3 Видалення елементів зі списку
# 3.3.1 Видалення елемента за допомогою команди del

del motorcycles[0]
# print(motorcycles)
# // ['Yamaha', 'Suzuki']

# 3.3.2 Видалення елемента з використанням методу pop()
# Видаляє елемент та вставляє його у змінну (видаляє останній елемент зі списку)

popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# ['honda', 'yamaha']
# print(popped_motorcycle)
# suzuki

# 3.3.2.1 Вилучення елементів із довільної позиції списку
# .pop(index)

first_mc_in_array = motorcycles.pop(0)
# print(first_mc_in_array)
# // ducati

# 3.3.3 Видалення елементів за значенням
# .remove(dataInArray)

motorcycles.remove("ducati")
# print(motorcycles)
# // ['honda', 'yamaha', 'suzuki']

# remove() також може використовуватись для роботи зі значенням

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
# print("\n " + too_expensive.title() + " це дуже дорого для мене.")
# // ['honda', 'yamaha', 'suzuki']
# // Ducati це дуже дорого для мене.

# 4. Впорядкування елементів списку
# sort() defalut сортує за абеткою або числами 0-$

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
# print(cars)
# // ['audi', 'bmw', 'subaru', 'toyota']

# sort(reverse = True) список сортується у порядку, зворотному алфавітному

cars.sort(reverse=True)
# print(cars)
# // ['Toyota', 'Subaru', 'Bmw', 'Audi']

# 4.1 Визначення довжини списку
# len(list)

# print(len(cars))
# // 4

# ПРИМІТКА
# Python підраховує елементи списку, починаючи з 1, тому при визначенні довжини списку помилка «зміщення на 1» вже не повинно бути.

# 5. Перебирання елементів списку. Цикл for
# У ситуаціях, що вимагають застосування однієї дії до кожного елемент списку, можна скористатися циклами for.
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
  print(magician)
# // alice 
# // david
# // carolina

# 6. Створення числових списків. Метод range
# 6.1 Функція range()
for value in range(1,5):
  print(value)
# // 1 2 3 4

for value in range(1,6):
  print(value)
# // 1 2 3 4 5

# 6.2 Використання range() для створення числового списку
numbers = list(range(1,6))
print(numbers)
# // [1, 2, 3, 4, 5]

even_numbers = list(range(2,11,2))
print(even_numbers)
# // [2, 4, 6, 8, 10]

squares = []
for value in range(1,11):
  squares.append(value**2)
print(squares)
# // [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 6.4 Проста статистика з числовими списками
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
# // 0
print(max(digits))
# // 9 
print(sum(digits))
# // 45

# 6.5 Генератори списків
squares = [value**2 for value in range(1,11)]
print(squares)
# // [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 7. Робота з частиною списку. Зрізи
# list[fist_i : last_i]

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# // [ 'charles', 'martina', 'michael']

print(players[1:4])
# // ['martina', 'michael', 'florence']

print(players[:4])
# // ['charles', 'martina', 'michael', 'florence']

print(players[2:])
# // ['michael', 'florence', 'eli']

print(players[-3:])
# // ['michael', 'florence', 'eli']

# 7.1 Перебір вмісту зрізу
for player in players[:3]:
  print(player.title())
# // Charles Martina Michael