#juego de 21
'''
Problema numero 1

juego de 21

+ sumar lo mas cerca posible a 21, sin pasarse
+ el usuario decide su quiere otra carta o platarse
+ la pc saca cartas automaticamente hasta que llegue a 17 o mas
+ gana quien este mas cerca de 21 sin pasarse

ayuda

+ cree una funcion para sacarCarta()
+ cree una funcion para turnoJugador()
+ cree una funcion para turnoPc()
+ cree una funcion para ganador()
+ cree una funcion para programaPricipal()
'''

primera = 0
suma = 0
dealer = 0
otra = 0

cartas = [1,2,3,4,5,6,7,8,9,10]
print(f"bienvenido a 21, las cartas que le pueden salir son {cartas}")



while primera<3 :
 
  from random import choice
  carta1 = choice(cartas)
  carta2 = choice(cartas)
  print(f"su carta es {carta1}")
  primera += 1
  suma += carta1
  dealer += carta2
     
print(f"su baraja es {suma} ")

a = input("desea otra carta? (s/n) ")
while a == "s" or a == "S":
    carta1 = choice(cartas)
    carta2 = choice(cartas)
    print(f"su carta es {carta1}")
    primera += 1
    suma += carta1
    dealer += carta2
    print(f"su baraja es {suma} ")
    a = input("desea otra carta? (s/n) ")
    if a == "n" or a == "N":
        print("se planto")
        break
     
    
print(f"las cartas del dealer son {dealer} ")
 
if suma <= dealer and dealer <= 21: 
    print("gano el dealer")
elif suma > dealer and suma <= 21:
    print("gano el jugador")
elif suma > 21:
    print("gano el dealer")
elif suma < dealer and dealer > 21:
    print("gano el jugador")
else:
    print("gano el dealer")

print("gracias por jugar")