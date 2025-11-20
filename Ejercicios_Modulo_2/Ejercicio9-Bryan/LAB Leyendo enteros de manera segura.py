# EJERCICIO 9 : BRYAN
("""Así es como la función debería reaccionar ante la entrada del usuario:

Ingresa un numero entre -10 a 10: 100
Error: el valor no está dentro del rango permitido (-10..10)
Ingresa un número entre -10 a 10: asd
Error: entrada incorrecta
Ingresa un número entre -10 a 10: 1
El número es: 1 """)



def pedir_numero(mensaje, minimo, maximo):

    while True:
        entrada = input(mensaje)

        # Validar si es número entero (permitir signo negativo)
        if not entrada.lstrip("-").isdigit():
            print("Error: entrada incorrecta")
            continue

        numero = int(entrada)

        # Validar rango
        if numero < minimo or numero > maximo:
            print(f"Error: el valor no está dentro del rango permitido ({minimo}..{maximo})")
            continue

        # Si llegó aquí, ya es válido
        return numero

# Ejemplo de uso:
n = pedir_numero("Ingresa un número entre -10 a 10: ", -10, 10)
print("El número es:", n)