def obtenerAccion(esObligatorio: str, esDocente: bool, esExterno: bool, tipoPersonaDestino: str,  estadoRegistro: str):
    if esObligatorio == "si" and esDocente:
        return "actualizar"
    elif esObligatorio == "no" and esDocente:
        return "matricular"
    elif esExterno and estadoRegistro == "Por confirmar":
        return "actualizar"
    elif esExterno and tipoPersonaDestino == "externo":
        return "registrar"
    elif esExterno and estadoRegistro == "vigente":
        return "actualizar"
    else:
        return "null"