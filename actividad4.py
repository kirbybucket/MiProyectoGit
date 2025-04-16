# Ejercicio para la clase
mayores, menores = 0, 0
cantidad = int(input("Ingrese la cantidad de estudiantes a registrar: "))

for i in range (cantidad):
    nombre = input("\nNombre: ")
    edad = int(input("Edad: "))

    if edad >= 18:
        print("\nEl estudiante", nombre, "es mayor de edad.")
        mayores += 1
    else:
        print("\nEl estudiante", nombre, "es menor de edad.")
        menores += 1

    print("La edad de", nombre, "dentro de 5 años será: ", edad+5)

print("<---------------------------------------------->")
print("\nTotal de estudiantes registrados: ",cantidad)
print("Estudiantes mayores de edad: ", mayores)
print("Estudiantes menores de edad: ", menores)
print("<---------------------------------------------->")

numero = int(input("\nIntroduce un número para ver su tabla de multiplicar: "))

for i in range(1,11):
    resultado = numero * i
    print(numero, "x", i, "=", resultado)