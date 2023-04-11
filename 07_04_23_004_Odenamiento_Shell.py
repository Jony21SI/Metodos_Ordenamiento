# Jonatan Sanchez Ibarra 20310417

# Se importa un Método de la biblioteca random para generar listas aleatorias
from random import sample 

lista = list(range(100)) # Se crea la lista base con números del 1 al 100

numeros = sample(lista,8)# Se crea una lista aleatoria con sample (8 elementos aleatorios de la lista base)

"""Esta función ordenara el vector que le pases como argumento 
    con el Método Shell Sort"""
def shell(numeros):
    
    print("Los numeros a ordenar con shell es:", numeros)
    largo = 0
    for i in numeros:
        largo += 1
    distancia = largo // 2
    
     # Creamos un bucle según las distancias
    while distancia > 0:
        # Utilizamos el Insertionsort
        for i in range(distancia, largo):
            val = numeros[i]
            j = i
            while j >= distancia and numeros[j - distancia] > val:
                numeros[j] = numeros[j - distancia]
                j -= distancia
            numeros[j] = val
        distancia //= 2 # Acotamos la distancia nuevamente y continua el ciclo
    print("Los numeros orednados son: ", numeros)
shell(numeros)
    