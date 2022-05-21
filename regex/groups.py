import re

# Busqueda de texto en el formato "Palabra, palabra"
# \w coincide con letras, numeros y guiones bajos.
result = re.search(r'^(\w*), (\w*)$', 'Lovelace, Ada')
print(result)
# Devuelve una tupla con los elementos
# [0] devuelve el grupo
# [1] El primer elemento
# [2] El que le sigue, y asi...
print(result.groups())

# Fix the regular expression used in the rearrange_name function so that it can match middle names, middle initials, as well as double surnames.
def rearrange_name(name):
    #result = re.search(r'^(\w*), (\w*)$', name)
    result = re.search(r'^([\w \.-]*), ([\w \.-]*)$', name)
    if result is None:
        return name
    return f'{result[2]} {result[1]}'

print(rearrange_name('Lovelace, Ada'))
print(rearrange_name('Kennedy, John F.'))

# Busca palabras que tengan hasta 5 letras
print(re.search(r'[a-zA-Z]{5}', 'a ghost'))
print(re.findall(r'[a-zA-Z]{5}', 'a scary ghost appeared'))

# Busca palabras que tengan al menos 5 letras
print(re.findall(r'\w{5,}', 'I really like strawberries'))

# Busca palabras con exactamente 5 letras
# \b coincide con los limites de palabras para indicar que queremos palabras completas
print(re.findall(r'\b[a-zA-Z]{5}\b', 'A scary ghost appeared'))

# Busca palabras con 5 a 10 letras.
print(re.findall(r'\w{5,10}', 'I really like strawberries'))

# Busca palabras que empiecen con s y hasta 20 letras
print(re.search(r's\w{,20}', 'I really like strawberries'))



# split method
# Fill in the code to split the text passed into a list of words.
print(re.split(r'[.?!]', 'One sentence. Another one? And the last one!'))
# Fill in the code to split the text passed into a list of words including punctuation.
print(re.split(r'([.?!])', 'One sentence. Another one? And the last one!'))

# sub method
# Reemplaza el correo por [REDACTED]
print(re.sub(r'[\w.%+-]+@[\w.-]+', '[REDACTED]', 'Received an email from yella@example.com'))

# Busca palabras en el formato apellido, nombre y lo reemplaza por nombre, apellido.
# \2 y \1 son los grupos de captura.
print(re.sub(r'^([\w .-]*), ([\w .-]*)$', r'\2 \1', 'Lovelace, Ada'))