"""
Escriba una función que tome una única cadena no vacía de letras ascii minúsculas 
y mayúsculas (palabra) como argumento y devuelva una lista ordenada que contenga 
los índices de todas las letras mayúsculas (mayúsculas) de la cadena.

Ejemplo (Entrada --> Salida)
"CodEWaRs" --> [0,3,4,6]

"""

def indiceMayus(word):
    # Opcion 1
    # arr = []
    # for i in range(len(word)):
    #     if word[i].isupper():
    #         arr.append(i)

    # return arr

    # Opcion 2
    print([i for i in range(len(word)) if word[i].isupper()])

indiceMayus("CodeWars")