"se puede modificar  (perimite repetir datos)"
lista = [1,2,3,4]
"no se puede modificar (perimite repetir datos)"
nomod = (1,2,3,4)

'esto se puede'
lista[3] += 1

'''esto no se puede
nomod[3] += 1
'''

print(lista[3])

#conjunto (no repite datos)
conjunto = {1, 2, 3, 4}

conjunto = {'hola', 'mundo', 45, 45}
#no se puede acceder a un elemento por su indice

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