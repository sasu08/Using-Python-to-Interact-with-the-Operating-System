#!/bin/bash

# Rename the files that ends with .HTM to .html inside the current directory.
for file in *.HTML; do
    name=$(basename "$file" .HTM)
    # Para evitar mandarnos cagadas, poner echo delante de los comandos, imprimira lo que se ejecuta. Asi comprobamos que es correcto.
    mv "$file" "$name.html"
done
