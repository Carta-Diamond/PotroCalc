print("Bienvenido al menú de opciones")
print("1. Multiplicar")
print("2. Dividir")
print("3.Sumar")
print("4.Restar")
ocpion = int(input("Ingrese la opción deseada: "))
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if ocpion == 1:

    print("El resultado de la multiplicación es: ", Multiplication(num1, num2))
elif ocpion == 2:
    print("El resultado de la división es: ", division(num1, num2))
elif ocpion == 3:
    print("El resultado de la suma es: ", addition(num1, num2))
elif ocpion == 4:
    print("El resultado de la resta es: ", rest(num1, num2))

else:
    print("Opción inválida. Por favor, seleccione una opción válida.")
