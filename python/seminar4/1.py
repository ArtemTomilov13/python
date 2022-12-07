# 1 Вычислить числить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141   
# Ввод: 0.01
#     Вывод: 3.14
#     Ввод: 0.001
#     Вывод: 3.141

import math
print(math.pi)
num = float(input("Введите число: "))

def schet_znakov(number_to_count):
    count = 0
    while number_to_count % 1 != 0:
        number_to_count *= 10
        count += 1
    return count
kol_znakov= schet_znakov(num)

print(round(math.pi, kol_znakov))