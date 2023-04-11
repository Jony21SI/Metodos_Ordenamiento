# Jonatan Sanchez Ibarra 20310417


# Se IMPORTA un Método de la biblioteca random para generar listas aleatorias
from random import sample 

lista = list(range(100)) # Se crea la lista base con números del 1 al 100
numeros = sample(lista,8) #Se Crea una lista aleatoria con sample (8 elementos aleatorios de la lista base)

"""Esta función ordenara el vector que le pases como argumento 
    con el Método Merge Sort"""
def mezcla(numeros): 
   
    
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("Los numeros a ordenar son:", numeros)
    
    def ordenamiento(numeros):
    
        def largo(vec):
                largovec = 0 # Establecemos un contador del largo del vector
                for _ in vec:
                    largovec += 1 # Se obtiene el largo del vector
                return largovec
        
        
        if largo(numeros) >1: 
            medio = largo(numeros)//2 # Se busca
            
            # Se divide en 2
            izq = numeros[:medio]  
            der = numeros[medio:]
            ordenamiento(izq) # Primera parte
            ordenamiento(der) # Segunda parte
            i = j = k = 0
            # Copiamos los datos a los vectores temporales izq[] y der[] 
            while i < largo(izq) and j < largo(der): 
                if izq[i] < der[j]: 
                    numeros[k] = izq[i] 
                    i+= 1
                else: 
                    numeros[k] = der[j] 
                    j+= 1
                k += 1
            # Nos fijamos si quedaron elementos en la lista tanto a la derecha como izquierda 
            while i < largo(izq): 
                numeros[k] = izq[i] 
                i+= 1
                k+= 1
            while j < largo(der): 
                numeros[k] = der[j] 
                j+= 1
                k+= 1
    ordenamiento(numeros)
    print("Los numeros ordenados son: ", numeros)
mezcla(numeros)