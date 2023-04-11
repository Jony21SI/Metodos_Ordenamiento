# Jonatan Sanchez Ibarra 20310417


# Se importa un Método de la biblioteca random para generar listas aleatorias
from random import sample 

lista = list(range(100)) # Se crea la lista base con números del 1 al 100
numeros = sample(lista,8) # Se crea una lista aleatoria con sample (8 elementos aleatorios de la lista base)

#Esta función ordenara el vector que le pases como argumento con el Método Heap Sort
def heapsort(numeros):
    
    print("Los numeros a ordenar son:", numeros) # Imprimimos la lista aleatoria obtenida al principio 
    largo = 0 # Establecemos un contador del largo
    for _ in numeros:
        largo += 1 # Obtenemos el largo del vector

    # Para amontonar la subparte a partir de i. n es el tamaño del montón.
    def amontonar(numeros, n, i): 
        mas_largo = i # Se toma i como el más grande 
        izq = 2 * i + 1      
        der = 2 * i + 2    
        if izq < n and numeros[i] < numeros[izq]: 
            mas_largo = izq 
    
        # Ver si existe la subparte de i correctamente y si es mayor que i
        if der < n and numeros[mas_largo] < numeros[der]: 
            mas_largo = der 
        if mas_largo != i: 
            numeros[i],numeros[mas_largo] = numeros[mas_largo],numeros[i] 
            # Cambiar el origen, si es necesario, amontonar el origen. 
            amontonar(numeros, n, mas_largo)
            
    def heap(numeros):
        n = largo
        # Crear un montón maximo 
        for i in range(n//2 - 1, -1, -1): 
            amontonar(numeros, n, i) 
        # Extraer elementos uno a uno
        for i in range(n-1, 0, -1): 
            numeros[i], numeros[0] = numeros[0], numeros[i] 
            # Intercambio 
            amontonar(numeros, i, 0)
        
    heap(numeros)
    print("Los numeros ordenados son:", numeros)

heapsort(numeros)