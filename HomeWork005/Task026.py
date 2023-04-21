# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

def power(a, b):
    if b == 0:
        return 1
    return power(a, b-1) * a

num = int(input("Введите число: "))
pow = int(input("Введите степень: "))

print(power(num, pow))
