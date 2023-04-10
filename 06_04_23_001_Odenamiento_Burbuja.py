#Jonatan Sanchez Ibarra 20310417

# Se Importa un Método de la biblioteca random para generar listas aleatorias
from random import sample 


lista = list(range(100)) # Creamos la lista base con números del 1 al 100


numeros = sample(lista,8) # Creamos una lista aleatoria con sample, (8 elementos aleatorios de la lista base)


def bubblesort(numeros):
    """Esta función ordenara el vector que le pases como argumento con el Método de Bubble Sort"""
    
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("Los numeros a ordenar son:",numeros)
    n = 0 # Establecemos un contador del largo del vector
    
    for _ in numeros:
        n += 1 #Contamos la cantidad de caracteres dentro del vector
    
    for i in range(n-1): 
    # Le damos un rango n para que complete el proceso. 
        for j in range(0, n-i-1): 
            # Revisa la matriz de 0 hasta n-i-1
            if numeros[j] > numeros[j+1] :
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
            # Se intercambian si el elemento encontrado es mayor 
            # Luego pasa al siguiente
    print ("Los numeros ordenados son: ",numeros)

bubblesort(numeros)