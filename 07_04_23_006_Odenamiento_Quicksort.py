# Jonatan Sanchez Ibarra 20310417


# Se importa un Método de la biblioteca random para generar listas aleatorias
from random import sample 

lista = list(range(100)) # Creamos la lista base con números del 1 al 100


numeros = sample(lista,8)# Se crea una lista aleatoria con sample (8 elementos aleatorios de la lista base)
"""Esta función ordenara el vector que le pases como argumento 
    con el Método Quick Sort"""
def quicksort(numeros, start = 0, end = len(numeros) - 1 ):
    # Imprimimos la lista aleatoria obtenida al principio 
    print("Los numeros a ordenar son:", numeros)
    def orden(numeros, start = 0, end = len(numeros) - 1):
        
        
        if start >= end:
            return

        def particion(numeros, start = 0, end = len(numeros) - 1):
            pivot = numeros[start]
            menor = start + 1
            mayor = end

            while True:
                # Si el valor actual es mayor que el pivot está en el lugar correcto (lado derecho del pivot) y podemos movernos hacia la izquierda, al siguiente elemento.
                # También debemos asegurarnos de no haber superado el puntero bajo, ya que indica que ya hemos movido todos los elementos a su lado correcto del pivot
                while menor <= mayor and numeros[mayor] >= pivot:
                    mayor = mayor - 1
                # Proceso opuesto al anterior            
                while menor <= mayor and numeros[menor] <= pivot:
                    menor = menor + 1
                # Encontramos un valor sea mayor o menor y que este fuera del arreglo
                # ó menor es más grande que mayor, en cuyo caso salimos del ciclo
                if menor <= mayor:
                    numeros[menor], numeros[mayor] = numeros[mayor], numeros[menor]
                    # Continua el bucle
                else:
                    # Salimos del bucle
                    break
            numeros[start], numeros[mayor] = numeros[mayor], numeros[start]
            return mayor
        p = particion(numeros, start, end)
        orden(numeros, start, p-1)
        orden(numeros, p+1, end)
    orden(numeros)
    print("Los numeros ordenados son:", numeros)

quicksort(numeros)