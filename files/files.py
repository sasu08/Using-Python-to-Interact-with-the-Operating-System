#!/usr/bin/env python3

# ---- Read & Write Files ---- #
file = open('./textfile.txt', "w")
"""
#open-use-close
print(file.read())
file.close()

#with-use
with open('./textfile.txt') as file:
    print(file.read())

with open('./textfile.txt', 'a') as file:
    file.write("\nThis is a new line")
"""

import os

#---- Archivos ---- #
# Elimina un archivo
#os.remove('textfile.txt')
# Renombra un archivo
#os.rename('textfile.txt', 'newtextfile.txt')
# Verifica si un archivo existe en la ruta actual
print(os.path.exists('newtextfile.txt'))
# Obtiene el tamaño de un archivo en bytes en la ruta actual
print(os.path.getsize('newtextfile.txt'))
# Obtiene la ruta absoluta de un archivo
abspath = os.path.abspath('newtextfile.txt')
print(abspath)

# ---- Directorios ---- #
# Obtiene la ruta actual.
print(os.getcwd())
# Crea un nuevo directorio
os.mkdir('newdir')
# Cambia de directorio
#os.chdir('newdir')
# Elimina un directorio, solo funciona si el directorio esta vacio.
#os.rmdir('newdir')
# Lista los archivos en un directorio
print(os.listdir('.'))
# Identifica si un archivo es un directorio
for file in os.listdir('.'):
    fullname = os.path.join('.', file)
    print(f"{file} es un directorio") if os.path.isdir(file) else print(f"{file} es un archivo")
