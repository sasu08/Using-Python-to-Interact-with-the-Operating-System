#!/usr/bin/env python3

import sys
import re

# Por razones de rendimiento, cuando los archivos son grandes, generalmente es una buena practica leerlos linea por linea en lugar de cargar todo el contenido en la memoria.
"""
# First version
logfile = sys.argv[1]
with open(logfile) as f:
    for line in f:
        if 'CRON' not in line:
            continue
        print(line.strip())
        """

# Final version
logfile = sys.argv[1]
usernames = {}

with open(logfile) as f:
    for line in f:
        if 'CRON' not in line:
            continue
        pattern = r'USER \((\w+)\)$'
        result = re.search(pattern, line)
        if result is None:
            continue
        name = result[1]
        usernames[name] = usernames.get(name, 0) + 1
    
print(usernames)