def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Parámetros:
    numeros (list): Lista de valores numéricos.

    Retorna:
    float: Promedio de los números ingresados.
    """
    
    if len(numeros) == 0:
        return 0
    
    return sum(numeros) / len(numeros)


# Ejemplo de uso
datos = [8, 9, 10, 7, 6]
promedio = calcular_promedio(datos)

print("El promedio es:", promedio)
