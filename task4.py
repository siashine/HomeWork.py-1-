# Напишите программу, которая по заданному 
# номеру четверти, показывает диапазон 
# возможных координат точек в этой четверти (x и y).

quarter = int(input("Введите номер четверти: "))

if quarter == 1:
 print("x>0, y>0")

if quarter == 2:
 print("x<0, y>0")

if quarter == 3:
 print("x<0, y<0")

if quarter == 4:
 print("x>0, y<0")
 
if quarter > 4:
 print("такой четверти нет")