TOKEN_CONF = [ ("reservada_para", automata_para),("reservada_desde", automata_desde),("reservada_hasta", automata_hasta),("reservada_sino", automata_sino),
("reservada_si", automata_si),("reservada_entonces", automata_entonces), ("reservada_mostrar", automata_mostrar),("reservada_aceptar", automata_aceptar).
("identificadores", automata_id), ("parentesis", automata_parentesis), ("llaves", automata_llaves), ("simbolos", automata_simbolos)]

def automata_para(cadena):

    estado_actual = 0
    estados_finales = [ 4 ]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "p":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "a" :
                estado_actual = 2
        elif estado_actual == 2 and caracter == "r" :
                estado_actual = 3
        elif estado_actual == 3 and caracter == "a" :
                estado_actual = 4

        else:
                estado_actual = -1
                break

        if estado_actual == -1:
            return ESTADO_TRAMPA
        if estado_actual in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL

def automata_desde(cadena):

    estado_actual = 0
    estados_finales = [ 5 ]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "d":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "e" :
                estado_actual = 2
        elif estado_actual == 2 and caracter == "s" :
                estado_actual = 3
        elif estado_actual == 3 and caracter == "d" :
                estado_actual = 4
        elif estado_actual == 4 and caracter == "e" :
                estado_actual = 5

        else:
                estado_actual = -1
                break

        if estado_actual == -1:
            return ESTADO_TRAMPA
        if estado_actual in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL

def automata_hasta(cadena):

    estado_actual = 0
    estados_finales = [ 5 ]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "h":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "a" :
                estado_actual = 2
        elif estado_actual == 2 and caracter == "s" :
                estado_actual = 3
        elif estado_actual == 3 and caracter == "t" :
                estado_actual = 4
        elif estado_actual == 4 and caracter == "a" :
                estado_actual = 5

        else:
                estado_actual = -1
                break

        if estado_actual == -1:
            return ESTADO_TRAMPA
        if estado_actual in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL

def automata_sino(cadena):

    estado_actual = 0
    estados_finales = [ 4 ]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "s":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "i" :
                estado_actual = 2
        elif estado_actual == 2 and caracter == "n" :
                estado_actual = 3
        elif estado_actual == 3 and caracter == "o" :
                estado_actual = 4

        else:
                estado_actual = -1
                break

        if estado_actual == -1:
            return ESTADO_TRAMPA
        if estado_actual in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL

def automata_si(cadena):

    estado_actual = 0
    estados_finales = [ 2 ]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "s":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "i" :
                estado_actual = 2


        else:
                estado_actual = -1
                break

        if estado_actual == -1:
            return ESTADO_TRAMPA
        if estado_actual in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL

def automata_entonces(cadena):

    estado_actual = 0
    estados_finales = [ 8 ]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "e":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "n" :
                estado_actual = 2
        elif estado_actual == 2 and caracter == "t" :
                estado_actual = 3
        elif estado_actual == 3 and caracter == "o" :
                estado_actual = 4
        elif estado_actual == 4 and caracter == "n" :
                estado_actual = 5
        elif estado_actual == 5 and caracter == "c" :
                estado_actual = 6
        elif estado_actual == 6 and caracter == "e" :
                estado_actual = 7
        elif estado_actual == 7 and caracter == "s" :
                estado_actual = 8

        else:
                estado_actual = -1
                break

        if estado_actual == -1:
            return ESTADO_TRAMPA
        if estado_actual in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL

def automata_mostrar(cadena):

    estado_actual = 0
    estados_finales = [ 7 ]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "m":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "o" :
                estado_actual = 2
        elif estado_actual == 2 and caracter == "s" :
                estado_actual = 3
        elif estado_actual == 3 and caracter == "t" :
                estado_actual = 4
        elif estado_actual == 4 and caracter == "r" :
                estado_actual = 5
        elif estado_actual == 5 and caracter == "a" :
                estado_actual = 6
        elif estado_actual == 6 and caracter == "r" :
                estado_actual = 7

        else:
                estado_actual = -1
                break

        if estado_actual == -1:
            return ESTADO_TRAMPA
        if estado_actual in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL

def automata_aceptar(cadena):

    estado_actual = 0
    estados_finales = [ 7 ]

    for caracter in cadena:
        if estado_actual == 0 and caracter == "a":
            estado_actual = 1
        elif estado_actual == 1 and caracter == "c" :
                estado_actual = 2
        elif estado_actual == 2 and caracter == "e" :
                estado_actual = 3
        elif estado_actual == 3 and caracter == "p" :
                estado_actual = 4
        elif estado_actual == 4 and caracter == "t" :
                estado_actual = 5
        elif estado_actual == 5 and caracter == "a" :
                estado_actual = 6
        elif estado_actual == 6 and caracter == "r" :
                estado_actual = 7

        else:
                estado_actual = -1
                break

        if estado_actual == -1:
            return ESTADO_TRAMPA
        if estado_actual in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL
def automata_id(cadena):
    letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    numeros = [ "0","1","2","3","4","5","6","7","8","9" ]

    estado_actual = 0
    estados_finales = [ 1 ]

        for caracter in cadena:
            if estado_actual == 0 and caracter in letras:
                estado_actual = 1
            elif estado_actual == 1 and caracter in letras or numeros :
                estado_actual = 1
            else:
                estado_actual == -1
                break

        if estado_actual == -1:
            return ESTADO_TRAMPA
        if estado_actual in estados_finales:
            return ESTADO_FINAL
        else:
            return ESTADO_NO_FINAL
def automata_parentesis(cadena):
    simbolos = ["(",")"]

    estado_actual = 0
    estados_finales = [1]

    for caracter in cadena:
        if estado_actual == 0 and caracter in simbolos:
            estado_actual = 1
        else:
                estado_actual = -1
                break
    if estado_actual == -1:
        return ESTADO_TRAMPA
    if estado_actual in estados_finales:
        return ESTADO_FINAL

def automata_llaves(cadena):
    simbolos = ["{","}"]
estado_actual = 0
estados_finales = [1]

for caracter in cadena:
    if estado_actual == 0 and caracter in simbolos:
        estado_actual = 1
    else:
            estado_actual = -1
            break
if estado_actual == -1:
    return ESTADO_TRAMPA
if estado_actual in estados_finales:
    return ESTADO_FINAL

def automata_simbolos(cadena):
    simbolos = ["*","+","=",";"]

    estado_actual = 0
    estados_finales = [1]

    for caracter in cadena:
        if estado_actual == 0 and caracter in simbolos:
            estado_actual = 1
        else:
                estado_actual = -1
                break

if estado_actual == -1:
    return ESTADO_TRAMPA
if estado_actual in estados_finales:
    return ESTADO_FINAL
