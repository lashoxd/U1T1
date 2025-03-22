'''
No cambies las definiciones (nombres y argumentos) de las funciones dadas aquí.
Por ahora, abordar las excepciones (p.ej., comprobar si el argumento es un número, 
    no una cadena cuando la función es para sumar los argumentos) es opcional.
'''

# Ejercicio 1
def calcular_puntaje(N, C):
    puntaje = N * 10 + C**2 *10
    print(puntaje)

# Ejercicio 2
# Asumimos que x dado es un número positivo.
def es_primo(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
    

# Ejercicio 3
def imprimir_parejas(nombres):
    for i in range(len(nombres)):
        for x in range(i + 1, len(nombres)):
                print(nombres[i], "y", nombres[x])

# Ejercicio 4
def obtener_asiento(nombre):
    #Parte 1 : Crear matriz  2x3 con nombres unicos
    asientos = [
        ["Diego", "Ana", "Eliana"],
        ["Daniel", "Juan", "Pablo"]
    ]
    filas = ["F", "G"]
    columnas = ["8", "9", "10"]

    #Parte 2 : Crear codigo para encontrar el nombre en la matriz
    for i in range(len(asientos)):
        for x in range(len(asientos[i])):
            if asientos[i][x] == nombre:
                return print(nombre,"esta en :",filas[i], columnas[x])
    print("Nombre no encontrado")

# Ejercicio 5
def comprobar_minuto(tiempo, minuto):
    tiempo2 = tiempo.split(":")
    horas = int(tiempo2[0])
    minutos = int(tiempo2[1])
    segundos = int(tiempo2[2])
    if minutos == minuto:
        print(True)
    else:
        print(False)


# Ejercicio 6
def es_palindromo(cadena):
    palindromo1 = cadena.replace(" ", "")
    print(palindromo1)
    palindromo=""
    for i in palindromo1:
        palindromo = i+ palindromo
    if palindromo == palindromo1:
        print(True)
    else:
        print(False)

# Ejercicio 7
def generar_fibonacci(N):
    if N < 1:
        print([])
    else:
        if N < 2:
            print([0])
        else:
            if N == 2:
                print([0, 1])
    fibonacci=[0, 1]
    for i in range(N-2):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    print(fibonacci)


# Para llamar y comprobar tus funciones
def main():
    import random
    X = random.randint(0, 99)
    Y = random.randint(0, 99)
    calcular_puntaje(X, Y)

    x=3
    print(es_primo(x))

    lista_nombres=["juan", "pepe","ana","flor"]
    imprimir_parejas(lista_nombres)

    obtener_asiento("Ana")

    comprobar_minuto("17:34:12", 12)
    comprobar_minuto("17:34:12", 34)

    caden1 = "anita lava la tina" 
    es_palindromo(caden1)

    cant=10
    generar_fibonacci(cant)

# No elimines esta parte que es para evitar que se ejecute el código cuando sea importado como un módulo.
if __name__ == "__main__":
    main()