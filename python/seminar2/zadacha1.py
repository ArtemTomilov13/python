# Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.
# Пример:
# 0,56 -> 11

num = float(input("Введите вещественное число: "))
str_num = str(num) 
str_num = str_num.replace('.', '') 
list_num = list(map(int, str_num))
sum = sum(list_num) 
print(sum)

