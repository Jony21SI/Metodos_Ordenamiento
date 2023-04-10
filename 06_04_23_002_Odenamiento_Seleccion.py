# Jonatan Sanchez Ibarra 20310417

# Se importa un Método de la biblioteca random para generar listas aleatorias
from random import sample 

lista = list(range(100)) # Se crea la lista base con números del 1 al 100

# Creamos una lista aleatoria con sample (8 elementos aleatorios de la lista base)
Numeros = sample(lista,8) 


"""Esta función ordenara el vector que le pases como argumento con el Método Selection Sort"""
def seleccion(Numeros):
    
    # Imprimimos la lista aleatoria obtenida al principio 
    print ("Los numeros a ordenar son:",Numeros)
    largo = 0
    
    for _ in Numeros:
        largo += 1 # Obtenemos el largo del vector
        
    for i in range(largo): 
        # Se encuentra el valor menor
        minimo = i 
        for j in range(i+1, largo): 
            if Numeros[minimo] > Numeros[j]: 
                minimo = j      
        # Cambiamos el elemento minimo encontrado con el primer elemento de la matriz
        Numeros[i], Numeros[minimo] = Numeros[minimo], Numeros[i]
        # Repetimos el proceso hasta terminar
    print("Los valores ordenados son: ",Numeros)
seleccion(Numeros)