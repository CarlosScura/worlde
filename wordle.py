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