TC = float(input("Digite la temperatura "))
K = TC + 273.15
if  type(TC) == int:
    print(TC, "grados centigrados es igual a: ", K)
if type(TC) == float and TC > 10.5:
    print(TC, "es mayor a 10.5")
elif TC < 10.5:
    print(TC, "es menor a 10.5")   