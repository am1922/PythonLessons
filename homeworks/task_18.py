# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному 
# числу X. Пользователь в первой строке вводит натуральное число N – количество элементов 
# в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит 
# число X.

a = [1, 2, 3, 4, 5, 23, 10, 8, 12]

x = 6

minDiff = float('inf')
closestNum = None

for num in a:
    absDiff = abs(num - x)
    if absDiff < minDiff or (absDiff == minDiff and num < closestNum):
        minDiff = absDiff
        closestNum = num

print(closestNum)