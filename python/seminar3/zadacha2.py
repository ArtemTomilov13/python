# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

lst = input("Введите список: ").split()
int_lst = list(map(int, lst))
print(f"Исходный список: {int_lst}")
prod = []
l = len(int_lst)//2 + 1 if len(int_lst) % 2 != 0 else len (int_lst)//2
for i in range (l):
    prod.append(int_lst[i] * int_lst[len(int_lst)-i-1])
print(f"Произведения равны: {prod}")

