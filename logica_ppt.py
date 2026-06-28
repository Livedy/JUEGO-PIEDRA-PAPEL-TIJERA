# =====================================================================
# logica_ppt.py
# Librería propia con la lógica del juego Piedra, Papel o Tijera.
# Se importa desde el programa principal (PROYECTOPPT.py) para
# reducir y ordenar el código principal.
# =====================================================================

import random

# Opciones válidas del juego
OPCIONES = ["piedra", "papel", "tijera"]

# Reglas: cada jugada (clave) le gana a la jugada (valor).
# Se usa un diccionario en lugar de una cadena de if/elif.
GANA_A = {
    "piedra": "tijera",
    "papel": "piedra",
    "tijera": "papel",
}

# Mensajes de victoria del usuario según su jugada
MENSAJE_VICTORIA = {
    "piedra": "Ganaste: la piedra rompe la tijera",
    "papel": "Ganaste: el papel envolvió a la piedra",
    "tijera": "Ganaste: la tijera cortó el papel",
}


def es_valida(jugada):
    """Devuelve True si la jugada ingresada es válida."""
    return jugada in OPCIONES


def jugada_maquina():
    """Devuelve una jugada aleatoria para la máquina."""
    return random.choice(OPCIONES)


def determinar_ganador(usuario, maquina):
    """
    Compara las jugadas y devuelve el resultado de la ronda.
    Retorna uno de estos textos: 'empate', 'usuario' o 'maquina'.
    """
    if usuario == maquina:
        return "empate"
    elif GANA_A[usuario] == maquina:
        return "usuario"
    else:
        return "maquina"


def mensaje_resultado(resultado, usuario):
    """Devuelve el mensaje que se mostrará según el resultado."""
    if resultado == "empate":
        return "Es un empate"
    elif resultado == "usuario":
        return MENSAJE_VICTORIA[usuario]
    else:
        return "La máquina gana"
