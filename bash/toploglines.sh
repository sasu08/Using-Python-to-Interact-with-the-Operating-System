#!/bin/bash

# Procesa todos los archivos en var/log que terminan en log.
# Imprime el nombre del archivo que estamos procesando.
# Imprime las cinco lineas principales de cada archivo.

for logfile in /var/log/*log; do
    echo "Processing: $logfile"
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done