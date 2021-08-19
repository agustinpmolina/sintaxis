def simbolos(cadena):
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
