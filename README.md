# Piedra, Papel o Tijera

Juego de consola en Python donde el usuario juega Piedra, Papel o Tijera contra la máquina. Lleva un marcador de puntos y valida lo que el usuario escribe. La lógica del juego está separada en una **librería propia** que el programa principal importa.

## Estructura del proyecto

```
JUEGO-PIEDRA-PAPEL-TIJERA/
├── PROYECTOPPT.py                        # Programa principal (importa la librería)
├── logica_ppt.py                         # Librería propia con la lógica del juego
├── flujograma_piedra_papel_tijera.png    # Diagrama de funcionalidad (flujo)
├── arquitectura.png                      # Diagrama de arquitectura del sistema
└── README.md
```

- **`logica_ppt.py`**: contiene las funciones del juego (validar la jugada, jugada de la máquina, decidir el ganador y los mensajes) y las reglas guardadas en un diccionario.
- **`PROYECTOPPT.py`**: programa principal. Importa la librería con `import logica_ppt as juego`, así que el código principal queda corto y solo se encarga del bucle y el marcador.

## Descripción

El programa pide al usuario que escriba una jugada (`piedra`, `papel` o `tijera`), revisa que lo escrito sea correcto, la máquina elige una opción al azar y se compara para ver quién gana (o si hay empate). Después de cada ronda se actualiza el marcador y se vuelve a pedir una jugada, hasta que el usuario escribe `salir`.

## Funcionamiento

1. El programa solicita una jugada: `piedra`, `papel`, `tijera` o `salir`.
2. Si el usuario escribe `salir`, el programa muestra el marcador final y finaliza.
3. Si la palabra ingresada no es válida, se muestra un mensaje de error y se vuelve a solicitar la jugada (sin que juegue la máquina).
4. Si la jugada es válida, la máquina elige una opción aleatoria entre `piedra`, `papel` y `tijera`.
5. Se compara la jugada del usuario contra la de la máquina:
   - Si son iguales, el resultado es empate.
   - Si el usuario gana, se suma un punto a su marcador.
   - Si la máquina gana, se suma un punto a su marcador.
6. Se muestra el marcador actualizado y se vuelve a solicitar una nueva jugada.

## Reglas del juego

| Jugada  | Gana a   |
|---------|----------|
| Piedra  | Tijera   |
| Papel   | Piedra   |
| Tijera  | Papel    |

## Diagrama de flujo

El diagrama (`flujograma_piedra_papel_tijera.png`) muestra la lógica del código. Cuando la jugada **no es válida**, el flujo vuelve a "Ingresar jugada" (igual que el `continue` del código), sin pasar al turno de la máquina.

## Cómo ejecutar

Ambos archivos `.py` deben estar en la misma carpeta. Luego:

```
python PROYECTOPPT.py
```

## Ejemplo de uso

```
Escoja piedra, papel o tijera (o 'salir'): piedra
Usted eligió: piedra
La máquina eligió: tijera
Ganaste: la piedra rompe la tijera
Marcador -> Usuario: 1 | Máquina: 0

Escoja piedra, papel o tijera (o 'salir'): salir
Juego finalizado
Marcador final -> Usuario: 1 | Máquina: 0
```

## Conclusiones

Con este juego pude aplicar las estructuras básicas de programación: el bucle `while` para que el juego siga corriendo, los condicionales para revisar las reglas y la validación para controlar lo que escribe el usuario. Me di cuenta de que aunque el programa sea sencillo, hay que pensar en todos los casos posibles, incluso cuando el usuario escribe algo mal.

Al separar la lógica en una librería aparte y llamarla desde el programa principal, el código quedó más corto y ordenado, las funciones se pueden volver a usar y las reglas están todas en un solo lugar. Esto se parece a como se organiza el código en proyectos más grandes, donde no todo va en un solo archivo.

Otra cosa que aprendí es que el diagrama de flujo y el código tienen que coincidir; si el diagrama no representa lo que hace el programa, deja de servir. Al final logré un juego que funciona, lleva el marcador, controla los errores y está dividido en módulos.

## Integrante

- Darwin Alexis Pilaguano Toapanta

**Docente:** Heredia Jiménez Estefanía Vanessa
**Asignatura:** Lógica de Programación
**Carrera:** Ingeniería en Sistemas — Universidad Internacional del Ecuador (UIDE)
**Fecha:** Junio 2026

