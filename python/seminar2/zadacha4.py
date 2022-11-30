# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной 
# строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

n = int(input("Введите целое число: "))
lst = [i for i in range (-n, n+1)]
print(lst)
index = input("Введите индексы: ").split()
int_index = list(map(int, index))
prod = 1
for i in range(len(int_index)):
    int_index[i] = int(int_index[i])
    k = int_index[i]
    prod = prod * lst[k]
print(int_index)
print(prod)

