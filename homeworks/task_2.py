# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input("Введите трех значное число, сумму цифр которого вы хотите узнать: "))
print(int((number // 100) + (number // 10) % 10) + (number % 10))
