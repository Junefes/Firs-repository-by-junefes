cadena1 = 'Hola junefes'.lower()
cadena2 = 'hola fes'
cadena3 = '10'
cadena4 = 'holajune'
#print(dir(cadena1))
#print(dir(1))

def letras():
    #convierte a mayusculas
    mayus = cadena1.upper()

    #convierte a minusculas
    minus = cadena1.lower()

    #primera letra en mayuscula
    cap = cadena1.capitalize()
    
    print(mayus, minus, cap)
letras()

def encuentra():
    #buscamos una cadena dentro de otra cadena, si no hay coincidencias devuelve -1
    busqueda = cadena1.find('10')

    #buscamos una cadena en otra cadena, si no hay coincidencias devuelve un error
    busqueda2 = cadena1.index('h')
    
    print(busqueda, busqueda2)
encuentra()

def num():
    #si es numero devuelve True, si no False
    cuenta = cadena3.isnumeric()

    #si es alfanumerico devuelve True, si no False
    cuenta2 = cadena4.isalpha()
    
    print(cuenta, cuenta2)
num()

def caracteres():
    #contamos la cantidad de cadenas dentro de otra cadena, devuelve la cantidad de coincidencias
    concoin = cadena1.count('hola')
    
    #contamos cuantos caracteres tiene la cadena
    contarcar = len(cadena1)
    
    print(contarcar, concoin)
caracteres()

def empieza():
    #verificamos si una cadena empieza con otra cadena, devuelve True o False
    emp = cadena1.startswith('hola')
    
    #verificamos si una cadena termina con otra cadena, devuelve True o False
    term = cadena1.endswith('fes')
    
    print(emp, term)
empieza()

def reemplazar():
    #reemplazamos una cadena por otra, devuelve la cadena modificada
    reem = cadena1.replace(' ',',')
    
    #separar cadena con la cadena que le pasamos, devuelve una lista
    separar = cadena1.split(' ')
    
    print(reem, separar)
    print(separar[1])
reemplazar()

print('\n fin del codigo')