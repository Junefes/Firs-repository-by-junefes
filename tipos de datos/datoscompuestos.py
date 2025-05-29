"se puede modificar a lista (perimite repetir datos)"
lista = [1,2,3,4]
"no se puede modificar a tupla (permite repetir datos)"
tupla = (1,2,3,4)

'esto se puede'
lista[3] += 1
lista[2] = 'axl'

'''esto no se puede
tupla[3] += 1
'''

print(lista[3], lista[2])

#conjunto (no repite datos)
conjunto = {1, 2, 3, 4, 4}
print(conjunto)

#no se puede acceder a un elemento por su indice 
conjunto = {'hola', 'mundo', 45, 45}

print(conjunto)

#creando un diccionario (dict)
diccionario = {
    'nombre': 'June',
    'edad' : 99,
    'lenguaje': 'Python',
    'es mujer?': False,
}

print(diccionario['nombre'])

#asi sucesivamente
#la estructura de un diccionario es key:value