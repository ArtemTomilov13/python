# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

lst = input("Введите список: ").split()
int_lst = list(map(int, lst))
print(f"Исходный список: {int_lst}")
list_nov = []
for i in int_lst:
    k = 0
    for j in int_lst:
        if i == j:
            k += 1
    if k == 1:
        list_nov.append(i)
print(list_nov)

