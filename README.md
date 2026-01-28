# worlde
# Este juego costó 1m de dolares.

## que necesitamos

En las variables necesitamos `una lista de palabras` `la palabra a adivinar` `palabra que ingresa la persona`

En las funciones necesitamos `una que controle que la palabra agregada solo tengo 5 letras`
otra que `elija la palabra` otra que `controle o compare la palabra secreta con la agregada por el usuario`

### pseudocodigo

* creamos la lista de palabras
* creamos la variable palabra secreta
* creamos la variable que el usuario va a cargar
* creamos la variable de intentos
* creamos variable bandera_seguir

* `creamos la funcion de elegir palabra
    el usuario ingresa un numero
    a ese numero se le resta 1
    ese numero-1 se carga en la lista de palabras controlando con el indice para elegir la palabra
    se transforma la palabra secreta en lista
    se carga la palabra secreta y se avisa al usuario`

* `creamos la funcion intentos
    controlamos que los intentos  no sean 0
    retornamos la variable bandera_seguir como True o false dependiendo del resultado`

* `creamos una funcion que pida la palabra al usuario
    controlamos que la palabra sea de 5 letras
    realizamos palabra.lower() para pasarlas todas a minusculas.
    transformamos la palabra en lista
    llamamos a la funcion de controlar y enviamos la palabra como argumento`

* creamos la funcion de comparar la palabra que carga el ususario con palabra secreta
    llamamos a la funcion intentos
    con un for controlamos que las letras de la palabra agregada sean iguales a cada letra de la palabra secreta
    con un if si la letra esta en el mismo indice en las 2 listas marcamos como en su lugar
    pero si las letras no estan en el mismo lugar marcamos como en la palabra
    restamos un intento

