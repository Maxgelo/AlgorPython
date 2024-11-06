v = int(input("ingrese cantidad de victorias "))
d = int(input("ingrese cantidad de derrotas "))
e = int(input("ingrese cantidad de empates "))
g = v * 3
p = d * 0
j = e * 1
t = g + p + j

print("por cada victoria el equipo obtuvo ", g, "puntos")
print("por derrota obtuvo ", p, "puntos")
print("por empate obtuvo ", j, "puntos")
print("puntos totales ", t)