#!/usr/bin/env python3
#2
import requests
import socket

def check_localhost():
    """chequea si el hostname es localhost (127.0.0.1)
    
    Keyword arguments:
    Return: devuelve true si el hostname es localhost, false en caso contrario
    """
    localhost = socket.gethostbyname('localhost')
    
    return True if localhost == '127.0.0.1' else False

def check_connectivity():
    """chequea si hay conexion con el sitio de Google.
    
    Keyword arguments:
    Return: devuelve true si hay conexion, false en caso contrario
    """
    request = requests.get('http://www.google.com')
    response = request.status_code
    
    return True if response == 200 else False