import random

#Sorteo un número aleatorio entre 1 y 100
numero_secreto = random.randint(1,101)

adivinado = False

print ("¡Bienvenido al juego de adivinar el número secreto!")

contador = 0
intentos = 6

while not adivinado:

    #Con esta variable voy a contabilizar la cantidad de intentos
    contador +=1
    intentos -=1 

    #Solicita que se ingrese un número
    num = int (input ("Introduce un número del 1 al 100: "))
    
    if num == numero_secreto:
        print ("GANASTE! Felicitaciones, el número indicado es el correcto. Acertaste en", contador, "intentos.")
        adivinado = True
    elif intentos == 0: 
        print ("PERDISTE! El número secreto era", numero_secreto)
        adivinado = True
    elif num < numero_secreto:
        print ("PERDISTE! El número correcto es mayor al que ingresaste, intentalo otra vez. Te quedan ", intentos, "intentos.")
    else:
        print ("PERDISTE! El número correcto es menor al que ingresaste, intentalo otra vez. Te quedan ", intentos, "intentos.")