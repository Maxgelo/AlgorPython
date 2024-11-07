num1 = float(input("Digite el primer número "))
num2 = float(input("Digite el segundo número "))
num3 = float(input("Digite el tercer número "))

if num1 > num2 and num1 < num3 or num1 > num3 and num1 < num2:
    print(num1,"es el número medio")
elif num2 > num1 and num2 < num3 or num2 > num3 and num2 < num1:
    print(num2,"es el número medio")
elif num3 > num1 and num3 < num2 or num3 > num2 and num3 < num1:
    print(num3,"es el número medio")
else:
    print("No hay un número medio")