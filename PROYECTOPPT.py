#Variables del contador de ganadas o perdidas
maquinaG= 0
usuarioG= 0
#variables del piedra papel o tijera para la maquina
opciones = ["piedra","papel","tijera"]
#modulo para la seleccion random realizada por la maquina
import random
#bucle en el cual entra el usuario para el juego 
while True:
    usuario = input("Escoja piedra, papel o tijera (o 'salir'): ").lower()
    if usuario == "salir":
        print("juego finalizado ")
        print("Marcador Usuario:", usuarioG, ", Máquina:", maquinaG)
        break
    if usuario not in opciones:
        print("ingrese correctamente la palabra")
        continue

    maquina = random.choice(opciones) #Eleccion random de la maquina y el usuario

    print("usted eligio", usuario)
    print("la maquina eligio:", maquina)

    if usuario == maquina: #Comparacion de la opcion del usuario y reglas del juego 
        print("Es un Empate")
    elif usuario == "piedra" and maquina == "tijera":
        print("Ganaste la piedra rompe la tijera")
        usuarioG += 1
    elif usuario == "papel" and maquina == "piedra":
        print("Ganaste el papel envolvió a la piedra")
        usuarioG += 1
    elif usuario == "tijera" and maquina == "papel":
        print("Ganaste la tijera cortó el papel")
        usuarioG += 1
    else:
        print("La maquina Gana")
        maquinaG += 1

    # Resultado del Juego
    print("Marcador: usuario:", usuarioG, ", maquina:", maquinaG)



