#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
#является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет



D = int(input('Введите день недели: '))
if D == 5:
    print('Выходной')
elif D == 6:
    print('Выходной')
else:
    print('будний')
    
    
    
#2. Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

a = 0
b = 1
for x in range (a, b):
   for y in range (a, b):
       for z in range (a, b):
           print ((not x or not y or not z) == (not x and not y and not z))


#3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

x_point = int (input ('Введите координату x: '))
y_point = int (input ('Введите координату y: ')) 
if x_point == 0 and y_point == 0:
    print('Error')
elif (x_point < 0 and y_point > 0):
    print ('1 четверть')
elif (x_point > 0 and y_point > 0):
    print ('2 четверть')
elif (x_point > 0 and y_point < 0):
    print ('3 четверть')
elif (x_point < 0 and y_point < 0):
    print ('4 четверть')

#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат
# точек в этой четверти (x и y).
quater = int(input('Введите номер четверти: '))
if (quater > 4):
    print('Error')
elif quater == 1:
    print('Возможные координаты точек: x > 0, y > 0')
elif quater == 2:
    print('Возможные координаты точек: x < 0, y > 0')
elif quater == 3:
    print('Возможные координаты точек: x < 0, y < 0')
elif quater == 4:
    print('Возможные координаты точек: x > 0, y < 0')

# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит растояние между ними в 2D пространстве
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math
x1 = int(input('x1 - '))
y1 = int(input('y1 - '))
x2 = int(input('x2 - '))
y2 = int(input('y2 - '))
distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
print('{:.2f}'.format(distance), sep='')

