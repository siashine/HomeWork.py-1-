# Напишите программу для проверки 
# истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.
# ⋀ - and
# ¬ - not
# ⋁ - or

x = int(input("Введите значение X, где 0 - ложь, 1 - истина: "))
y = int(input("Введите значение Y, где 0 - ложь, 1 - истина: "))
z = int(input("Введите значение Z, где 0 - ложь, 1 - истина: "))


left = not (x or y or z)
right = not x and not y and not z

if left == right:
  print("True")
else:
  print("False")