
#crea una lista con el constructor list()
lista = list(['hola','junefes',2025])
lista2 = list([10, 11, 12])

# dictamina cuantos elementos tiene la lista
resultado = len(lista)


def agregando():
    print('agregando')
    # agrega un elemento al final de la lista
    lista.append('master dev')

    #agregando un elemento a la lista en una posicion especifica
    lista.insert(2, 'lista')

    #agregamos varios elementos a la lista
    lista.extend(['agregando','elementos'])
    
    print(lista,'\n')   
agregando()

def eliminando():
    print('eliminando')
    #eliminando un elemento de la lista por su indice
    lista.pop(-1) #menos uno para eliminar el ultimo elemento y sigue eliminando hacia atras
    
    #removemos un elemento de la lista por su valor
    lista.remove('junefes') #si no existe el elemento, lanza un error
    
    #eliminamos todos los elementos de la lista
    #lista.clear() #descomentar para eliminar todos los elementos de la lista
    
    print(lista,'\n')    
eliminando()

def ordenando():
    print('ordenando')
    #no poner atencion los siguientes metodos
    lista2.append(52)
    
    lista2.insert(3,9)
    
    lista2.extend([True,5,False,67])
    
    print(f'lista numerica: {lista2}')
    
    #ordenamos la lista de forma ascendente
    lista2.sort() #esto solo funciona con numeros y cadenas
    print(lista2)
    
    #ordenamos la lista de forma descendente
    lista2.sort(reverse=True) #esto solo funciona con numeros y cadenas
    print(lista2)
    
    #invertimos el orden de la lista
    lista.reverse()
    
    print(f'lista 1: {lista}\n')
ordenando()

def index():
    print('index')
    #buscamos el indice de un elemento en la lista
    elemento_encontrado = lista.index('master dev')
    
    print(elemento_encontrado,'\n')
index()

#print(dir('dwas'))