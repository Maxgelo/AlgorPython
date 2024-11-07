nn = int(input("Ingrese número de notas "))
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0
nt = 0

if nn == 1:
    n1 = float(input("Digite la primera nota "))
    nt = (n1) / nn
    print("su nota final es ", nt)
elif nn == 2:
    n1 = float(input("Digite la primera nota "))
    n2 = float(input("Digite la segunda nota "))
    nt = (n1 + n2) / nn
    print("su nota final es ", nt)
elif nn == 3:
    n1 = float(input("Digite la primera nota "))
    n2 = float(input("Digite la segunda nota "))
    n3 = float(input("Digite la tercera nota "))
    nt = (n1 + n2 + n3) / nn
    print("su nota final es ", nt)
elif nn == 4:
    n1 = float(input("Digite la primera nota "))
    n2 = float(input("Digite la segunda nota "))
    n3 = float(input("Digite la tercera nota "))
    n4 = float(input("Digite la cuarta nota "))
    nt = (n1 + n2 + n3 + n4) / nn
    print("su nota final es ", nt)
elif nn == 5:
    n1 = float(input("Digite la primera nota "))
    n2 = float(input("Digite la segunda nota "))
    n3 = float(input("Digite la tercera nota "))
    n4 = float(input("Digite la cuarta nota "))
    n5 = float(input("Digite la quinta nota "))
    nt = (n1 + n2 + n3 + n4 + n5) / nn
    print("su nota final es ", nt)
else:
    print("no se puede ingresar mas de 5 notas")