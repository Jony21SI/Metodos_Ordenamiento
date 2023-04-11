# Jonatan Sanchez Ibarra 20310417

# Se importa un Método de la biblioteca random para generar listas aleatorias
from random import sample 

lista = list(range(100)) # Creamos la lista base con números del 1 al 100


numeros = sample(lista,8) # Se crea una lista aleatoria con sample (8 elementos aleatorios de la lista base)

 #Esta función ordenara el vector que le pases como argumento con el Método de Cocktail Sort"""
def cocktail(numeros):
   
    # Imprimimos la lista aleatoria obtenida al principio 
    print("El vector a ordenar con cocktail es:",numeros)
    largo = 0 # Establecemos un contador del largo
    for _ in numeros:
        largo += 1 # Obtenemos el largo del vector
    for i in range(largo//2): # Comenzamos desde la mitad aprox
        bandera = False 
        # Declaramos la variable que inidica si es necesario intercambiar o no 
        for j in range(1+i, largo-i):
            # Probar si los dos elementos están en el orden incorrecto
            if numeros[j] < numeros[j-1]:
                # Entonces ambos elementos cambian de lugar
                numeros[j], numeros[j-1] = numeros[j-1], numeros[j]
                bandera = True
        # Si no ocurren cambios salimos del bucle
        if not bandera:
            break
        bandera = False
        for j in range(largo-i-1, i, -1):
            # Probar si los dos elementos están en el orden incorrecto
            if numeros[j] < numeros[j-1]:
                # Entonces ambos elementos cambian de lugar
                numeros[j], numeros[j-1] = numeros[j-1], numeros[j]
                bandera = True
        if not bandera:
            break
    print("Los numeros oredenados son: ",numeros)

cocktail(numeros)