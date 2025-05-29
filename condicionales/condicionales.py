'''a = 1
b = 2
d = int(input('ingrese un numero del 0 al 1: '))
c = a + b - d


# Comparacion de variables
accion = 'se ejecuto'
if c == 3:
    print(accion,'1')
    
else:
    print(accion,'2')'''
    
edad = int(input('ingrese su edad: '))
pobreza = input('es pobre?: ').lower()

#if anidados, else if y else 

def validar_edad():
    
     if edad < 11:
      print('Eres menor de edad')
      if pobreza == 'si':
          print('bienestar familiar biene por ti')
      else:
          print('no hay problema')
     elif edad <= 17 and edad>=12:
        print('Eres un adolescente')
        if pobreza == 'si':
            print('bienestar familiar biene por ti')
        else:
            print('no hay problema')
     else:
      print('Eres mayor de edad')
      if pobreza == 'si':
            print('mala suerte')
      else:
            print('no hay problema')
      
validar_edad()