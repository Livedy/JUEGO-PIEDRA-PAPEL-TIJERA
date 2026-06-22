# Mi primer proyecto en GitHub
# Piedra, Papel o Tijera

Juego de consola en Python que permite a un usuario jugar Piedra, Papel o Tijera contra la máquina, con marcador de puntos y validación de entradas.

## Descripción

El programa solicita al usuario que ingrese una jugada (`piedra`, `papel` o `tijera`), valida que el texto ingresado sea correcto, genera una jugada aleatoria para la máquina y determina el resultado de la ronda (empate, victoria del usuario o victoria de la máquina). El marcador se actualiza después de cada ronda y el ciclo se repite hasta que el usuario decide salir.

## Funcionamiento

1. El programa solicita una jugada: `piedra`, `papel`, `tijera` o `salir`.
2. Si el usuario escribe `salir`, el programa finaliza.
3. Si la palabra ingresada no es válida, se muestra un mensaje de error y se vuelve a solicitar la jugada.
4. Si la jugada es válida, la máquina elige una opción aleatoria entre `piedra`, `papel` y `tijera`.
5. Se compara la jugada del usuario contra la de la máquina:
   - Si son iguales, el resultado es empate.
   - Si el usuario gana, se suma un punto a su marcador.
   - Si la máquina gana, se suma un punto a su marcador.
6. Se muestra el marcador actualizado y se vuelve a solicitar una nueva jugada.

## Reglas del juego

| Jugada 1 | Gana a   |
|----------|----------|
| Piedra   | Tijera   |
| Papel    | Piedra   |
| Tijera   | Papel    |
