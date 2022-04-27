#!/usr/bin/env python3
#1
import shutil
import psutil
from network import *

def check_disk_usage(disk):
    """chequea si el espacio libre es mayor al 20%
    
    Keyword arguments:
    disk -- ruta a chequear
    Return: devuelve true si el espacio libre es mayor al 20%, false en caso contrario
    """
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100 
    return free > 20
    
def check_cpu_usage():
    """chequea el uso de la CPU en un intervalo de 1 segundo.
    
    Return: devuelve true si el uso de la CPU es menor al 75%, false en caso contrario
    """
    usage = psutil.cpu_percent(1)
    return usage < 75


# Si algo esta mal con el disco y la CPU, se imprime "ERROR".
if not check_disk_usage('/') or not check_cpu_usage():
    print('ERROR')
# Si todo esta bien, se imprime "Everything ok".
elif check_localhost() and check_connectivity():
    print("Everything ok")
# Si algo esta mal con check_localhost o check_connectivity, se imprime "Network checks failed".
else:
    print("Network checks failed")