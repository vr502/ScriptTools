# -*- coding: utf-8 -*-
abcLower = "abcdefghijklmnñopqrstuvwxyz"
digits = "0123456789"
signs = "!#$%&//()=?¡¿¿+*{}[]^`-_;,:.~"

# ingreso de los caracteres
characters = abcLower + abcLower.upper() + digits + signs

def validate_commentary(commentary):
    for letter in commentary:
        if letter in characters:
            pass
        else:
            return False
        return True

# example
text = '¡Bienvenido al mundo virtual!, ¿Cuantos años tienes?'
textNoValid = "<Script>alert('hello')</script>"
if validate_commentary(textNoValid):
    print('Yes')
else:
    print('No')