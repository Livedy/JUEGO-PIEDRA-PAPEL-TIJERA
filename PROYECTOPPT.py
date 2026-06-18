import random
usuario = input ("escoja piedra papel o tijera: ").lower()
opciones = ["piedra","papel","tijera"]
maquina = random.choice(opciones)
print ("usted eligio", usuario)
print ("la maquina eligio:", maquina)
if usuario == maquina:
 print ("Es un Empate")
elif usuario == "piedra" and maquina == "tijera":
 print ("Ganaste la piedra rompe la tijera")
elif usuario == "papel" and maquina ==  "piedra":
 print ("Ganaste la piedra envolvio al papel")
elif usuario == "tijera" and maquina ==  "papel":
 print ("Ganaste la tijera corto el papel")
else:
 print ("La maquina Gana")
