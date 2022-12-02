# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

lst = input("Введите список вещественных чисел: ").split()
float_lst = list(map(float, lst))
print(f"Исходный список: {float_lst}")
drob_lst = []
for i in range (len(float_lst)):
    drob_lst.append(float_lst[i] - int(float_lst[i]))
drob_lst.sort()
max = max(drob_lst)
min = min(drob_lst)
result = max - min
print(f"Разница равна: {round(result, 3)}")


