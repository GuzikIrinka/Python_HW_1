#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
#является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет



#D = int(input('Введите день недели: '))
#if D == 5:
 #   print('Выходной')
#elif D == 6:
    #print('Выходной')
#else:
  #  print('будний')
    
    
    
#Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

#a = 0
#b = 1
#for x in range (a, b):
 #   for y in range (a, b):
  #      for z in range (a, b):
   #         print ((not x or not y or not z) == (not x and not y and not z))


#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

#x_point = int (input ('Введите координату x: ')) 
#y_point = int (input ('Введите координату y: ')) 
#if ((x_point == 0) or (y_point == 0)):
 #   print ('ошибка!')
#elif (x_point < 0 and y_point > 0):
 #   print ('1 четверть')
#elif (x_point > 0 and y_point > 0):
 #   print ('2 четверть')
#elif (x_point > 0 and y_point < 0):
 #   print ('3 четверть')
#elif (x_point < 0 and y_point < 0):
 #   print ('4 четверть')
 
x_point = int (input ('Введите координату x: ')) 
y_point = int (input ('Введите координату y: ')) 
if ((x_point == 0) or (y_point == 0)):
    print ('ошибка!')
elif (x_point < 0 and y_point > 0):
    print ('1 четверть')
elif (x_point > 0 and y_point > 0):
    print ('2 четверть')
elif (x_point > 0 and y_point < 0):
    print ('3 четверть')
elif (x_point < 0 and y_point < 0):
    print ('4 четверть')