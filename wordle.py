#Verificador de palabras ingresadas

letras_verificadas = []
cantidad_letras = 5

palabra_usuar = 'ropas'
palabra_s = 'perro'


def verificador_palabra(palabra_ingresada, palabra_secreta):
    for i in range(cantidad_letras):
        las_palabras_son_iguales = palabra_ingresada[i] == palabra_secreta[i] # True o False
        la_letra_existe_en_la_palabra = palabra_ingresada[i] in palabra_secreta 
        
        if las_palabras_son_iguales:
            letras_verificadas.append(f"[{palabra_ingresada[i]}]")
        elif la_letra_existe_en_la_palabra:
            letras_verificadas.append(f"({palabra_ingresada[i]})")
        else:
            letras_verificadas.append(palabra_ingresada[i])
    
    print(letras_verificadas)

verificador_palabra('holas', 'calor')

#Intentos

# definir la cantidad de intentos = variable
def intentos_player():
    intentos = 0

    while intentos < 6:
        print(f"te quedan {6 - intentos} intentos");
        intentos = intentos + 1;
        palabra_ingresada = input("Ingrese una palabra");
        print(f"la palabra ingresada es: {palabra_ingresada}");

# Recorrer lista para mostrar intentos

lista_de_intentos = []

def recorrer_lista(array):
    for i19 in array:
        print(i19)

