# Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = int(input("Введите координату x точки A: "))
y1 = int(input("Введите координату y точки A: "))
x2 = int(input("Введите координату x точки B: "))
y2 = int(input("Введите координату y точки B: "))
import math
l = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
print(l)
