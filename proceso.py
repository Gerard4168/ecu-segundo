a = int(input("Introduce el valor de a: "))
b = int(input("Introduce el valor de b: "))
c = int(input("Introduce el valor de c: "))

# Calcula el discriminante
d = b**2 - 4*a*c

# Verifica si hay soluciones reales
if d < 0:
    print("No hay soluciones reales")
elif d == 0:
    # Si el discriminante es cero, solo hay una solución
    sol = -b / (2*a)
    print("La solución es:", sol)
else:
    # Si el discriminante es positivo, hay dos soluciones
    sol1 = (-b + d**0.5) / (2*a)
    sol2 = (-b - d**0.5) / (2*a)
    print("Las soluciones son:", sol1, "y", sol2)