# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

def index_in_range(numbers, min, max):
    index = []
    for i in range(len(numbers)):
        if min <= numbers[i] <= max:
            index.append(i)
    print(index)

numbers = [4, 5, 6, 10, -9, 23, 78, -98, 78, 125, 2, 0, 79, -45]
min = -50
max = 50

index_in_range(numbers, min, max)


