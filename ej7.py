nom = input("Ingrese su nombre ")
ed = int(input("Digite su edad "))
sex = input("Ingrese su sexo (hombre o mujer) ")
ec = input("Ingrese su estado civil (soltero o casado) ")

if sex == "hombre" and ec == "casado" and ed > 40:
    print(nom)
elif sex == "mujer" and ec == "soltero" and ed < 40:
      print(nom)