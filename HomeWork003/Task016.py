# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

n = int(input("Введите количество элементов: "))
list_a = []

for i in range(n):
    list_a.append(int(input("Введите целое число: ")))
    
x = int(input("Введите число X: "))
count = 0

for i in range(len(list_a)):
    if list_a[i] == x:
        count += 1

print(count)