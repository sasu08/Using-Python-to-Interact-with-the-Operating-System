#!/usr/bin/env python3

# Pipeline:
# Ejecutar en consola cat haiku.txt | ./capitalize.py
# o ./capitalize.py < haiku.txt (Operador de redireccion)
import sys

for line in sys.stdin:
    print(line.strip().capitalize())