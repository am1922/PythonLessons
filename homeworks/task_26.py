# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит 
# число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def sqrd(a, b):
   if b == 0:
        return 1
   elif b < 0:
        return 1 / sqrd(a, -b)
   elif b % 2 == 0:
        temp = sqrd(a, b // 2)
        return temp * temp
   else:
        return a * sqrd(a, b - 1)

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

result = sqrd(a, b)

print(f"{a} в степени {b} равно {result}")