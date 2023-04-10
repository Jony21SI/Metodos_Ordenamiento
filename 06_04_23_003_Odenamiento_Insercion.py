# Jonatan Sanchez Ibarra 20310417

# Se importa un Método de la biblioteca random para generar listas aleatorias
from random import sample 


lista = list(range(100)) # Se crea la lista base con números del 1 al 100


numeros = sample(lista,8) # Se crea una lista aleatoria con sample (8 elementos aleatorios de la lista base)

"""Esta función ordenara el vector que le pases como argumento con
    el Método Insertion Sort"""
def insercion(numeros): 
    
    
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("Los numeros a ordenar son:", numeros)
    
    largo = 0 # Establecemos un contador del largo
     
    for i in numeros:
        largo += 1 # Obtenemos el largo del vector
    
    # Recorremos la lista de 1 hasta el largo del vector
    for i in range(1, largo): 
    
        elemento = numeros[i] 
  
        # Movemos los elementos de numeros[0...i-1], que son mayores que el elemento
        # a una posición adelante de su posición actual
        j = i-1
        while j >= 0 and elemento < numeros[j] : 
                numeros[j+1] = numeros[j] 
                j -= 1
        numeros[j+1] = elemento 
    print("Los numeros ordenados son: ", numeros)

insercion(numeros)