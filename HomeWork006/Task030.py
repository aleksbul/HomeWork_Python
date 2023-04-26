# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def progression(start, d, amount):
    numbers = []
    for n in range(1, amount + 1):
        numbers.append(start + (n - 1)*d)
    print(numbers)


start = int(input("Введите первый элемент: "))
difference = int(input("Введите разность: "))
amount = int(input("Введите количество элементов: "))
progression(start, difference, amount)