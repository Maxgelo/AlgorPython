num1 = float(input("Digite el primer número "))
num2 = float(input("Digite el segundo número "))
num3 = float(input("Digite el tercero número "))
if num1 > num2 and num1 > num3:
    print(num1, "es el número mayor ")
elif num2 > num1 and num2 > num3:
    print(num2, "es el número mayor ")
else:
    print(num3, "es el número mayor ")
if num1 < num2 and num1 < num3:
    print(num1, "es el número menor")
elif num2 < num1 and num2 < num3:
    print(num2, "es el número menor")
else:
    print(num3, "es el número menor")
if num1 == num2:
    print(num1, "y", num2, "son iguales")
elif num1 == num3:
     print(num1, "y", num3, "son iguales")
elif num2 == num3:
     print(num2, "y", num3, "son iguales")
elif num1 == num3 and num2 == num3:
     print("todos son iguales")
else:
    print("todos son distintos")
     