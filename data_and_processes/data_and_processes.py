#!/usr/bin/env python3

# COMANDOS DE CONSOLA:
# - wc: número de lineas, palabras y caracteres en un archivo.
# - $?: devuelve el valor de la última operación ejecutada. 0 si esta todo ok, cualquier otro numero si hay algún error.

import os
import sys

# Obtienen las variables de entorno especificadas.
print(f'HOME: {os.environ.get("HOME", "")}')
print(f'SHELL: {os.environ.get("SHELL", "")}')
# La variable de abajo no esta definida en el entorno actual.
# Hay que definirla en el shell escribiendo:
# export FRUIT=Pineapple
print(f'FRUIT: {os.environ.get("FRUIT", "")}')

# Imprime los parametros de la linea de comandos.
# Cuando llamamos al script desde la linea de comandos,
# los parametros que le pasamos al script se almacenan en la variable sys.argv.
# Ejemplo: ./data_and_processes.py param1 param2 param3
print(sys.argv)