import subprocess

# Devuelve un objeto del tipo CompletedProcess. Incluye informacion relacionada con la ejecucion del comando.
subprocess.run(['date'])

# Espera un numero determinado de segundos y luego regresa al programa.
subprocess.run(['sleep', '1'])

result = subprocess.run(['host', '8.8.8.8'], capture_output=True)
print(result.returncode)
# Almacena la salida generada.
print(result.stdout)
# Hay que utilizar decode para convertir el resultado de stdout a string.
print(result.stdout.decode().split())