"""El Dígito de la Vida
Algunos dicen que el Dígito de la Vida es un dígito calculado usando el cumpleaños de alguien. Es simple: solo necesitas sumar todos los dígitos de la fecha. Si el resultado contiene más de un dígito, se debe repetir la suma hasta obtener exactamente un dígito. Por ejemplo:

1 Enero 2017 = 2017 01 01
2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
1 + 2 = 3
3 es el dígito que buscamos y encontramos.

Tu tarea es escribir un programa que:
Le pregunté al usuario su cumpleaños (en el formato AAAAMMDD o AAAADMM o MMDDAAAA;
en realidad, el orden de los dígitos no importa).
Dé como salida El Dígito de la Vida para la fecha ingresada.
Prueba tu código utilizando los datos que te proporcionamos."""

import re #Lo importamos para hacer uso de expresiones regulares

def calcular_digito_vida(fecha_str):
    todos_los_digitos_str = re.sub(r'\D', '', fecha_str) #Cualquier carácter que NO sea un dígito lo cambia a un caracter vacio.

    if not todos_los_digitos_str: # Si la cadena no tiene dígitos.
        print("Error: La fecha ingresada no contiene dígitos válidos.")
        return None

    # La suma de todos los dígitos de la fecha inicial.
    suma_actual = sum(int(d) for d in todos_los_digitos_str) #iteramos los caracteres de la cadena y los convertimos a enteros
    print(f"\nPaso 1: Suma inicial de todos los dígitos ({todos_los_digitos_str}) = {suma_actual}")

    paso = 2 #consideramos un segundo paso
    while suma_actual > 10: #Se sigue sumando hasta que el numero sea menor a 10
        siguiente_suma = 0

        for digito_char in str(suma_actual): # Convertimos la suma actual a una cadena para iterar sobre sus dígitos
            siguiente_suma += int(digito_char)

        print(f"Paso {paso}: Suma de los dígitos de {suma_actual} = {siguiente_suma}")
        suma_actual = siguiente_suma
        paso += 1
    return suma_actual


#Bucle del programa
if __name__ == "__main__":
    print("--- Calculadora del Dígito de la Vida ---")

    while True:
        fecha_input = input(
            "\nIngresa tu fecha de cumpleaños (AAAAMMDD, MMDDAAAA, con/sin espacios/guiones): "
        ).strip() #strip elimina espacios al inicio o final

        if not fecha_input: #validacion
            print("No se ingresó ninguna fecha. Inténtalo de nuevo.")
            continue

        # llamamos la funcion para calcular el digito de la vida
        resultado = calcular_digito_vida(fecha_input)

        if resultado is not None:
            print(f"EL DIGITO DE LA VIDA PARA LA FECHA {fecha_input} ES: {resultado}")

        #Pregunta para cerrar o seguir en el bucle
        continuar = input("\n¿Calcular otra fecha? (s/n): ").strip().lower()
        if continuar != 's':
            print("¡Gracias por usar la calculadora del Dígito de la Vida! ")
            break