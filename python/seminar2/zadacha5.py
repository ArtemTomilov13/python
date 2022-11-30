# Реализуйте алгоритм перемешивания списка.
import random
lst = input("Введите список: ").split()
int_lst = list(map(int, lst))
print(f"Исходный список: {int_lst}")
random.shuffle(int_lst)
print(f"Перемешанный список: {int_lst}")
