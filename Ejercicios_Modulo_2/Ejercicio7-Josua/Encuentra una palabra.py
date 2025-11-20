#Ejercicio 7 - Joshua
def verificar_caracteres_ocultos(cadena_buscada, cadena_principal):
    primera = cadena_buscada.lower()
    segunda = cadena_principal.lower()
    indice_inicio_busqueda = 0

    for letra in primera:
        posicion_encontrada = segunda.find(letra, indice_inicio_busqueda)
        if posicion_encontrada == -1:
            return "No"
        else:
            indice_inicio_busqueda = posicion_encontrada + 1
    return "Sí"

cadena_principal_usuario = input("Ingresa la cadena en donde deseas buscar: ")
cadena_buscada_usuario = input("Ingresa la palabra que deseas encontrar: ")
resultado = verificar_caracteres_ocultos(cadena_buscada_usuario, cadena_principal_usuario)

print(f"{resultado}")