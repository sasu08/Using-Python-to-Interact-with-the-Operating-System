#!/usr/bin/env python

# Como regla general, deberiamos usar raise para verificar las condiciones que esperamos que ocurran durante la ejecucion normal de nuestro codigo, y assert para verificar situaciones que no se esperan, pero que podrian causar que nuestro codigo se comporte mal.

def validate_user(username, minlen):
    # Verifica que el tipo de dato de username sea string, sino lanza una excepcion.
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True