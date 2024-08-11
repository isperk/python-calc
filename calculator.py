# -*- coding: utf-8 -*-
def add(x, y):
    """Suma x e y y devuelve el resultado."""
    return x + y

def subtract(x, y):
    """Resta y de x y devuelve el resultado."""
    return x - y

def multiply(x, y):
    """Multiplica x por y y devuelve el resultado."""
    return x * y

def divide(x, y):
    """Divide x por y y devuelve el resultado. Asegúrate de que y no sea cero."""
    if y == 0:
        return "Error! División por cero."
    return x / y

if __name__ == "__main__":
    while True:
        print("Operaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        choice = input("Elige una operación (1/2/3/4/5): ")
        print(choice)
        if choice == '5':
            print("Saliendo del programa...")
            break

        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if choice == 1:
            print("Resultado:", add(num1, num2))
        elif choice == '2':
            print("Resultado:", subtract(num1, num2))
        elif choice == '3':
            print("Resultado:", multiply(num1, num2))
        elif choice == '4':
            print("Resultado:", divide(num1, num2))
        else:
            print(choice)
            print("Opción no válida, por favor intenta de nuevo.")

        # Opcional: agregar un espacio entre las operaciones para mejor legibilidad.
        print("\n")
