import re
# www.regex101.com

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
# Expresion para buscar digitos entre corchetes
regex = r'\[(\d+)\]'
result = re.search(regex, log)
print(result[1]) 


# Fill in the code to check if the text passed contains the vowels a, e and i, with exactly one occurrence of any other character in between.
import re
def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True


# Busqueda de coincidencias sin distinguir mayusculas y minusculas
print(re.search(r'p.ng', 'Pangea', re.IGNORECASE))
print(re.search(r'[Pp]angea', 'Pangea'))
# Busqueda de coincidencias incluidas entre [a-z] (todas minusculas).
print(re.search(r'[a-z]way', 'The end of the highway'))
# Busqueda de coincidencias incluidas entre [a-z], [A-Z], [0-9] (todo el abecedario y numeros del 0 al 9).
print(re.search(r'cloud[a-zA-Z0-9]', 'cloudless'))
# Busqueda de coincidencias para cualquier caracter que no sea una letra. Con [^] se niega.
print(re.search('[^a-zA-Z ]', 'This is a sentence with spaces.'))
# Busqueda de coincidencias con alternativas. Se obtiene la primera que se encuentra.
print(re.search(r'cat|dog', 'I have a cat.'))
# Busqueda de coincidencias con alternativas. Se obtienen todas las coincidencias.
print(re.findall(r'cat|dog', 'I have a cat and a dog.'))

# Repeated matches
# Busqueda de coincidencias para palabras enteras. 
# "Py.*n" es una expresion regular que busca palabras que empiecen con P y terminen en "n" y que contengan uno o mas caracteres.
# Se dice que tiene un comportamiento "Greedy" (codicioso) porque busca tomar tantos caracteres como sea posible. 
print(re.search(r'Py.*n', 'Pygmalion'))
print(re.search(r'Py.*n', 'Python is a programming language'))
# Si queremos que el patron coincida con letras, se usan clases de caracteres.
print(re.search(r'Py[a-z]*n', 'Python is a programming language'))

# +: Busqueda de coincidencias para palabras que contengan las letras una seguida de la otra, no importa cuantas veces. 
print(re.search(r'o+l+', 'goldfish'))
print(re.search(r'o+l+', 'woooooooolllllly'))
# ?: Busqueda de coincidencias para palabras que contengan alguna o ninguna ocurrencia.
print(re.search(r'p?each', 'to each their own'))
print(re.search(r'p?each', 'i like peaches'))


# Escaping characters
# Por ejemplo, para buscar una coincidencia que contenga un punto, se usa \. Porque el punto es un caracter especial.
print(re.search(r'.com', 'welcome'))
# Versus:
print(re.search(r'\.com', 'www.google.com'))

# Busqueda de coincidencias que coincidan con letras, numeros y guiones bajos. Para esto se usa \w.
print(re.search(r'\w*', 'this is an example'))
print(re.search(r'\w*', 'welcome_to_the_world'))


#Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.
def check_character_groups(text):
    result = re.search(r"\w\d", text)
    return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False


# Busqueda para palabras que empiecen y terminen con a.
print(re.search(r'^A.*a$', 'Argentina'))
# Busqueda para palabras nombre validos de variables. Puede contener letras, numeros y guiones bajos pero no puede empezar con un numero.
print(re.search(r'^[a-zA-Z_][a-zA-Z0-9_]*$', '_this_is_a_valid_variable_name'))
print(re.search(r'^[a-zA-Z_][a-zA-Z0-9_]*$', 'this isn\'t a valid variable'))
print(re.search(r'^[a-zA-Z_][a-zA-Z0-9_]*$', '232invalid_variable_name'))


# Fill in the code to check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point. 
def check_sentence(text):
    result = re.search(r"[A-Z][a-z| ].*[.?!]$", text)
    return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True