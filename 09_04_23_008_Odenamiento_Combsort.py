# Jonatan Sanchez Ibarra 20310417

# Se importa un Método de la biblioteca random para generar listas aleatorias
from random import sample 

lista = list(range(100)) # Se crea la lista base con números del 1 al 100

# Se crea una lista aleatoria con sample (8 elementos aleatorios de la lista base)
numeros = sample(lista,8)

#Esta función ordenara el vector que le pases como argumentocon el Método de Comb Sort
def combsort(numeros):
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar con comb es:",numeros)
    largo = 0 # Establecemos un contador del largo del vector
    for _ in numeros:
        largo += 1
    
    # Comenzamos con la diferencia o distancia igual al largo del vector
    diferencia = largo
    # Establecemos la variable que define si es necesario o no intercambiar los numeros que se están comparando
    cambiar = True
    
    while diferencia > 1 or cambiar:
        diferencia = max(1, int(diferencia / 1.25))  
        # La diferencia minima es 1 y en cada iteración vamos bajando la diferencia
        cambiar = False
        for i in range(largo - diferencia):
            j = i+diferencia 
            # Ubicamos el número que está a la distancia x de i
            if numeros[i] > numeros[j]:
                numeros[i], numeros[j] = numeros[j], numeros[i]
                # Hacemos el intercambio de los numeros
                cambiar = True
    print("Los numeros ordenados son: ",numeros)

combsort(numeros)