'''
No cambies las definiciones (nombres y argumentos) de las funciones dadas aquí.
Por ahora, abordar las excepciones (p.ej., comprobar si el argumento es un número, 
    no una cadena cuando la función es para sumar los argumentos) es opcional.
'''

# Ejercicio 1
def contar_vocales(palabra):
    vocal = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    cuentavocales=0
    i = 0
    while i < len(palabra):
        x = 0
        while x < len(vocal):
            if palabra[i] == vocal[x]:
                cuentavocales = cuentavocales + 1
            x += 1
        i +=1
    print("la cant de vocales de la palabra", palabra, "son: ", cuentavocales)


# Ejercicio 2
def calcular_suma_digitos(numero):
    ...

# Ejercicio 3
def calcular_palabras(cadena):
    ...

# Ejercicio 4
def obtener_max_min(lista):
    ...
    


# Para llamar y comprobar tus funciones
def main():
    palabra1="paralelepipedo"
    contar_vocales(palabra1)

# No elimines esta parte que es para evitar que se ejecute el código cuando sea importado como un módulo.
if __name__ == "__main__":
    main()