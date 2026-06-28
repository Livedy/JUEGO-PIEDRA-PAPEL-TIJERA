# Piedra, Papel o Tijera

Juego de consola en Python que permite a un usuario jugar Piedra, Papel o Tijera contra la máquina, con marcador de puntos y validación de entradas. El proyecto está organizado en una **librería propia** que separa la lógica del juego del programa principal.

## Estructura del proyecto

```
JUEGO-PIEDRA-PAPEL-TIJERA/
├── PROYECTOPPT.py                        # Programa principal (importa la librería)
├── logica_ppt.py                         # Librería propia con la lógica del juego
├── flujograma_piedra_papel_tijera.png    # Diagrama de funcionalidad (flujo)
├── arquitectura.png                      # Diagrama de arquitectura del sistema
└── README.md
```

- **`logica_ppt.py`**: librería creada por el estudiante. Contiene las funciones del juego (validación, jugada de la máquina, determinación del ganador y mensajes) y las reglas en un diccionario.
- **`PROYECTOPPT.py`**: programa principal. Importa la librería con `import logica_ppt as juego`, por lo que el código principal queda corto y solo maneja el bucle y el marcador.

## Descripción

El programa solicita al usuario que ingrese una jugada (`piedra`, `papel` o `tijera`), valida que el texto ingresado sea correcto, genera una jugada aleatoria para la máquina y determina el resultado de la ronda (empate, victoria del usuario o victoria de la máquina). El marcador se actualiza después de cada ronda y el ciclo se repite hasta que el usuario decide salir.

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

El diagrama (`flujograma_piedra_papel_tijera.png`) representa fielmente la lógica del código. La rama de validación, cuando la jugada **no es válida**, regresa directamente a "Ingresar jugada" (equivalente al `continue` del código), sin continuar al turno de la máquina.

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

El desarrollo del juego Piedra, Papel o Tijera permitió aplicar de forma práctica las estructuras lógicas fundamentales de la programación: el bucle `while` para mantener el juego activo, los condicionales para evaluar las reglas y la validación de entradas para controlar errores del usuario. Comprobé que un programa, por simple que parezca, requiere anticipar todos los caminos posibles que puede tomar el usuario —incluyendo entradas incorrectas— para comportarse de forma robusta.

Al separar la lógica en una librería propia (`logica_ppt.py`) e importarla desde el programa principal, entendí el valor de la modularidad: el código principal se vuelve más corto y legible, las funciones se pueden reutilizar y mantener por separado, y las reglas del juego quedan centralizadas en un diccionario fácil de ampliar. Esta organización refleja cómo se estructura el software real, donde la lógica se distribuye en módulos en lugar de concentrarse en un único archivo.

Una implicación importante del proyecto fue comprender que el diagrama de flujo y el código deben corresponderse exactamente: un diagrama que no refleja la lógica real del programa pierde su utilidad como herramienta de diseño y documentación. Como logro, conseguí un programa funcional con marcador acumulado, manejo de errores y una estructura modular, reforzando la importancia de planificar la lógica antes de codificar.

## Integrantes

- Darwin Alexis Pilaguano Toapanta

**Docente:** Heredia Jiménez Estefanía Vanessa
**Asignatura:** Lógica de Programación
**Carrera:** Ingeniería en Sistemas — Universidad Internacional del Ecuador (UIDE)
**Fecha:** Junio 2026
