'''
    VARIABLES
'''

# variable para la cantidad de intentos dentro del juego
intentos = 6

letras_verificadas = []
cantidad_letras = 5

palabra_secreta = "gatos"

palabra_ingresada = ''

numero = 5

ganaste = False

'''
    FUNCIONES
'''

# definir la cantidad de intentos = variable
def fun_intentos():
    global palabra_ingresada
    global numero
    global intentos
    if intentos > 0:
        print(f"tienes {intentos} intentos")
        intentos -= 1
        palabra_ingresada = input("Ingrese una palabra")
        print(f"la palabra ingresada es: {palabra_ingresada}")
        tamano_palabra(palabra_ingresada,numero)
    else:
        print("Perdiste :(\nMejor suerte la proxima")


# controla el tamaño de la palabra
def tamano_palabra(palabra,numero):
    global palabra_secreta
    global intentos
    if len(palabra) == numero:
        print(f"Palabra tiene {numero} letras")
        verificador_palabra(palabra,palabra_secreta)
    else:
        print(f"{palabra} no tiene {numero} letras")
        intentos+=1
        fun_intentos()

# transforma la palabra a una lista
def transformar(palabra):
    palabras_ingresadas = []
    for i in range(3):
        # palabra = input("ingresa una palabra")
        palabra_convertida = list(palabra)
        palabras_ingresadas.append(palabra_convertida)
        return palabras_ingresadas

# Controlar palabras

def verificador_palabra(palabra_ingresada, palabra_secreta):
    global numero
    global ganaste
    for i in range(numero):
        las_palabras_son_iguales = palabra_ingresada[i] == palabra_secreta[i]   # True or False
        la_letra_existe_en_la_palabra = palabra_ingresada[i] in palabra_secreta # True or False
        if las_palabras_son_iguales:
            letras_verificadas.append(f"[{palabra_ingresada[i]}]")
            ganaste = True # si esto pasa ultimo se gana igual
        elif la_letra_existe_en_la_palabra:
            letras_verificadas.append(f"({palabra_ingresada[i]})")
            ganaste = False
        else:
            letras_verificadas.append(palabra_ingresada[i])
            ganaste = False
    if not ganaste:
        imprimir_matriz(letras_verificadas)
    else:
        ganador(palabra_ingresada)

# imprimir listas

def imprimir_matriz(lista):
    x=0
    for i in lista:
        print(lista[x])
        x+=1
    
def ganador(palabra_ingresada):
    print(f"Felicidades GANASTE!\nLa palabra era {palabra_ingresada}!!")
