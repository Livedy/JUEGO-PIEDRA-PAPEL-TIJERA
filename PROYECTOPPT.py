# =====================================================================
# PROYECTOPPT.py
# Programa principal del juego Piedra, Papel o Tijera.
# Importa la librería propia "logica_ppt" para reducir el código
# principal: aquí solo queda el flujo del juego y el marcador.
# =====================================================================

# Importamos nuestra librería propia con la lógica del juego
import logica_ppt as juego

# Marcadores de puntos
usuarioG = 0
maquinaG = 0

# Bucle principal del juego
while True:
    usuario = input("Escoja piedra, papel o tijera (o 'salir'): ").lower()

    # Opción para terminar el juego
    if usuario == "salir":
        print("Juego finalizado")
        print("Marcador final -> Usuario:", usuarioG, "| Máquina:", maquinaG)
        break

    # Validación de la jugada usando la librería
    if not juego.es_valida(usuario):
        print("Ingrese correctamente la palabra")
        continue

    # La máquina elige y se determina el ganador (lógica en la librería)
    maquina = juego.jugada_maquina()
    resultado = juego.determinar_ganador(usuario, maquina)

    print("Usted eligió:", usuario)
    print("La máquina eligió:", maquina)
    print(juego.mensaje_resultado(resultado, usuario))

    # Se actualiza el marcador
    if resultado == "usuario":
        usuarioG += 1
    elif resultado == "maquina":
        maquinaG += 1

    print("Marcador -> Usuario:", usuarioG, "| Máquina:", maquinaG)
