

s = int(input("Cuantas palabras quiere verificar si es palindroma? "))
con = 0
while con < s:  
    # Pedimos al usuario que introduzca una cadena
    cadena = input("Introduce una palabra o frase: ")
    # Convertimos la cadena a minúsculas y eliminamos los espacios en blanco
    cadena = cadena.lower().replace(" ", "")

    # Comprobamos si es palíndroma y mostramos un mensaje adecuado
    if cadena == cadena[::-1]:
        print("¡es palíndroma la palabra {0}!".format(cadena))
    else:
        print("La cadena no es palíndroma.")
    con+=1