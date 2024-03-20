"""
Output de todos mis conocimientos en python
En este documento querada todo lo que recuerdo y mas.
tipos de datos y variables , listas,diccionarios,tuplas,ciclos y condicionales ,funciones,metodos y clases.

El el documento siguiente quedaran proyectos basicos y avanzados.

(-- TODO QUEDARA DOCUMENTADO, SI ME FALTAN COSAS SOBRE PYTHON ESTE SE IRA ACTUALIZANDO DE FORMA PROGRESIVA. --)

"""

"""
TIPOS DE DATOS
    String(CADENA DE TEXTO) - ESTE SE USA CON "COMILLA DOBLES" O 'COMILLAS SIMPLES'

    int(ENTERO) - ESTE SE DECLARA CON NUMEROS ENTEROS SOLAMENTE = 122 , -10 , 20 , 0, 

    float(NUMEROS DECIMALES O FLOTANTES) - ESTE SE DECLARA CON NUMEROS DECIMALES = 23.34444 , -2.4 , 334.4555

    bool(Condiciones verdad o falso,(1 y 0)) - ESTE SE DECLARA CON LAS PALABRAS CLAVE DE = True o False.
    Se usa para comparar condiciones verdaderas o falsas en el la logica del codigo.

    list(ES UNA LISTA, PUEDE CONTENER TODO TIPO DE DATOS VISTOS, HASTA UNA MISMA LISTA DENTRO DE ELLA), 
    SE DECLARA DE LA SIGUIENTE FORMA var = list(("hola","plata",30,1.3,True)) o como objeto, lista = ["TEXTO", 20.2,-4,True,["LISTA DENTRO DE OTRA" , False,200]]
    "LAS LISTAS SON MUTABLES O MODIFICABLES"

    dict(ESTE ES UN DICCIONARIO, PUEDE CONTENER TODO TIPO DE DATO , LA DIFERENCIA ESQUE SE DECLARA CON CLAVE Y VALOR),
    SE DECLARA DE LA SIGUIENTE FORMA =  var = dict(a= 1, b=2, c=3) o var = dict([('a',1),('b',2),('c',3)]) 
    Y TAMBIEN COMO OBJETO var = {nombre : Jose Daniel , Edad : 28, Vivo: False,hijos:["Javier,Marcela"]}
    "LOS DICCIONARIOS SI SON MUTABLES O MODIFICABLES" 


    tuple(ESTA ES UNA TUPLA , SE CORPORTA PARECIDO A LAS LISTAS , PERO ESTAS NO SON MUTABLES NO SE PUEDEN MODIFICAR ,
    AL MENOS QUE SE LAS TRANSFORMEMOS EN UNA LISTA.) LAS TUPLAS PUEDEN CONTENER TODO TIPO DE DATOS AL IGUAL QUE LISTAS, 
    DICCIONARIOS Y LAS MISMAS TUPLAS DENTRO DE ELLA. SE DECLARA ASI - var = tuple(True,'Soy un texto',-234,34.4412)
    COMO TAMBIEN DENTRO DE LA TUPLA var = ('string',{hola:chao},["lista"]).
 
"""

"""
VARIABLES 

    LAS VARIABLES DE PUEDEN LLAMAR DE CUALQUIER FORMA PERO NO PUEDEN COMENZAR CON UN NUMERO.
    LAS VARIABLES TIENEN UN CICLO DE VIDA YA QUE AL EJECUTAR EL CODIGO ESTE SE EJECUTA DE ARRIBA HACIA ABAJO Y DE IZQUIERA A DERECHA
    LAS VARIABLES QUE ESTAN PRIMERO Y SE EJECUTAN MUEREN O MEJOR DICHO YA NO EXISTEN EN LA MEMORIA RAM DE EL EQUIPO, LAS VARIABLES OCUPAN CIERTA
    CANTIDAD DE ESPACIO EN LA MEMORIA RAM DEL EQUIPO CUANDO SE DECLARAN, ENTONCES LAS VARIABLES QUE SE EJECUTEN PRIMERO VAN A PERDER SU ESPACIO EN LA MEMORIA
    Y VAN A DEJAR DE EXISTR EN EL MOMENTO EN QUE SE PASE A LA VARIABLE DE MAS ABAJO.
EJEMPLO:

# LAS VARIALBES AL EXISTIR YA TIENEN UN ESPACIO EN LA MEMORIA 

# ESTA VARIABLE SE EJECUTARA PRIMERO,AL PASAR EL EJECUTOR A EL RESTO DEL CODIGO LA VARIABLE VA A PERDER SU EXISTENCIA EN LA MEMORIA.
    variable1 = True

    variable2 = ["Curico",'Puertto Montt']

# AHORA Variable2 ES LA QUE EXISTE EN LA MEMORIA AHORA YA QUE EL EJECUTOR PASA HACIA EL RESTO DEL CODIGO 


    POR REGLA DE BUENA PRACTICA DE CODIGO SE DEBE DECLARA O ESCRIBIR CON MINUSCULA AL COMIENZO DE EL NOMBRE DE LA VARIABLE Y NO PUEDE HABER UN ESPACIO DENTRO 
    DE DOS PALABRAS SEPARADAS AL IGUAL QUE SE PUEDE HACER LA DIFERENCIA DE LAS PALABRAS CON COMENZAR LA SIGUIENTE PALABRA CON MAYUSCULAS

EJEMPLO CORRECTO: 

    variable = 

    numero_NotacionCientifica = 

    nombrePersonalSEC20 = 

EJEMPLO INCORRECTO:

    92 = 

    9espacios = 

-- ESTE EJEMPLO PUEDE VARIAR TIENE CORRECTO USO PERO EN LA PRACTICA ES MEJOR COMENZAR CON MINUSCULA EL NOMBRE DE LA VARIABLE
    Lapidas = 
"""

#            --- TIPOS DE DATOS BASICOS--- 
"""
   ANTES DE EMPEZAR CON LOS TIPOS DE DATOS Y SUS FORMAS DE USARLOS , ESTA EL PRINT(DENTRO VAN ARGUMENTOS) QUE ES UNA FUNCION QUE DA LA FORMA DE IMPRIMIR 
   POR LA CONSOLA , EN EL PRINT() PODEMOS CONCATENAR TEXTO Y AGREGAR OTRAS VARIABLES ES MULTIFUNCIONAL, MAS ABAJO VAMOS A 
   MOSTRAR COMO HACER COSAS MAS AVANZADAS CON EL PRINT() .

"""
print("SOY UNA IMPRESION POR CONSOLA")

# TIPO DE DATO , CADENA DE TEXTO O STRING
cadenaTexto = "ESTA ES UNA CADENA DE TEXTO"
print(cadenaTexto) # IMPRIMIMOS LA VARIABLE cadenaTexto QUE CONTIENE UNA CADENA DE TEXTO O STRING

# TIPO DE DATO, ENTERO O INT
numeroEntero = 29
print(numeroEntero) # IMPRIMIMOS numeroEntero

# TIPO DE DATO, DECIMAL O FLOTANTE
numeroDecimal = 23.34000
print(numeroDecimal)

# TIPOS DE DATOS, BOOLEANOS
verdadero = True
print(verdadero)

falso = False
print(falso)

"""
A LAS VARIABLES LES PODEMOS DAR O INGRESARLES UN VALOR ATRAVES DE la FUNCION input(),ESTA FUNCION TRATRA COMO CADENA DE TEXTO
TODO LO QUE SE INGRESE A EN EL INPUT()A CONTINUACION VEMOS COMO FUNCIONA.
"""
rut = input("Ingresa tu rut: ")
cant = input("Ingresa tu cantidad de cuadernos: ")

"""
PARA PODER TRATAR LOS DATOS QUE VAMOS A INGRESAR EN EL INPUT COMO UN NUMERO ENTERO O COMO UN DECIMAL,BOOLEANO SE DEBEN ESCRIBIR 
DE LA SIGUIENTE MANERA. 
"""
nombre = str(input("Ingresa un nombre: "))
edad = int(input("Ingresa tu edad: "))
estatura = float(input("Ingresa tu estatura: "))
eleccion = bool(input("Ingresa un condicion verdadera o falsa: ")) # ACA SI INGRESAMOS ALGO NOS ARROJARA True PERO SI NO SERA False
print(eleccion) # PRINT() PARA COMPROBAR 


#        --- MANEJO DE LAS CADENAS DE TEXTO --- 
"""
    EN LAS CADENAS DE TEXTOS PODEMOS , CONCATENAR OTRAS VARIABLES QUE CONTENGAN CADENAS DE TEXTO
    PODEMOS MUTARLAS Y CAMBIARLAS A NUESTRO GUSTO.

    upper(): Convierte una cadena a mayúsculas.
    lower(): Convierte una cadena a minúsculas.
    strip(): Elimina los espacios en blanco al principio y al final de una cadena.
    split(): Divide una cadena en una lista de subcadenas utilizando un separador especificado.
    capitalize(): Devuelve una copia de la cadena con el primer carácter en mayúscula y el resto en minúscula.
    replace(): Reemplaza todas las ocurrencias de una subcadena con otra subcadena.
    find(): Encuentra la primera ocurrencia de una subcadena en la cadena y devuelve su índice.
    join(): Concatena una lista de cadenas utilizando la cadena actual como separador.
    format(): Formatea una cadena utilizando valores pasados como argumentos.
    len(): Devuelve la longitud de una cadena (número de caracteres).
    index(): Devuelve el índice de la primera ocurrencia de una subcadena en la cadena.
    count(): Cuenta el número de ocurrencias de una subcadena en la cadena.

"""
# upper() y lower()
texto = "Hola Mundo"
print(texto.upper())  # Salida: HOLA MUNDO
print(texto.lower())  # Salida: hola mundo

# strip()
texto = "-   Hola Mundo  -"
print(texto.strip())   # Salida: "Hola Mundo"

# split()
texto = "Hola, Mundo, Python"
lista_palabras = texto.split(", ")
print(lista_palabras)  # Salida: ['Hola', 'Mundo', 'Python']

# capitalize()
texto = "hola mundo"
resultado = texto.capitalize()
print(resultado)  # Salida: "Hola mundo"

# replace()
texto = "Hola Mundo"
nuevo_texto = texto.replace("Mundo", "Python")
print(nuevo_texto)  # Salida: "Hola Python"

# find()
texto = "Hola Mundo"
print(texto.find("Mundo"))    # Salida: 5

# Join()
nuevo_texto = " - ".join(lista_palabras)
print(nuevo_texto)  # Salida: "Hola - Mundo - Python"

# format()
nombre = "Juan"
edad = 30

mensaje = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)
print(mensaje)  # Salida: "Hola, mi nombre es Juan y tengo 30 años."

# len()
texto = "Hola Mundo"
longitud = len(texto)
print(longitud)  # Salida: 10

# index()
texto = "Hola Mundo"
indice = texto.index("Mundo")
print(indice)  # Salida: 5

# count()
texto = "Hola Mundo, Hola Python, Hola Mundo"
ocurrencias = texto.count("Hola")
print(ocurrencias)  # Salida: 3

#                               OPERADORES BASICOS
# OPERADORES ARITMETICOS
"""
UN OPERADOR ARITMETICO TOMA 2 OPERANDOS COMO ENTRADA, REALIZA UN CALCULO Y DEVUELVE EL RESULTADO

CONSIDERAR LA EXPRECION, a = 2 + 3. EL 2 Y EL 3 SON LOS OPERANDOS Y + ES EL OOPERADOR ARITMETICO. 
EL RESULTADO DE LA OPERACION SE ALMACENA EN LA VARIABLE a.

OPERADOR|              DESCRIPCION                  |      USO
    +	  Realiza Adición entre los operandos	        12 + 3 = 15
    -	  Realiza Substracción entre los operandos	    12 - 3 = 9
    *	  Realiza Multiplicación entre los operandos	12 * 3 = 36
    /	  Realiza División entre los operandos	        12 / 3 = 4
    %	  Realiza un módulo entre los operandos	        16 % 3 = 1
    **	  Realiza la potencia de los operandos	        12 ** 3 = 1728
    //	Realiza la división con resultado de número entero	18 // 5 = 3

"""
#               EJEMPLOS:
# SUMA
a = 5
b = 3
resultado = a + b
print(resultado) 
#RESTA
a = 7
b = 2
resultado = a - b
print(resultado)
# MULTIPLICACION
a = 4
b = 6
resultado = a * b
print(resultado)
# DIVISION
a = 10
b = 3
resultado = a / b
print(resultado)
# DIVISION ENTERA
a = 10
b = 3
resultado = a // b
print(resultado)
# MODULO O RESTO DE LA DIVISION
a = 10
b = 3
resultado = a % b
print(resultado)
# POTENCIA
a = 2
b = 3
resultado = a ** b
print(resultado)

# OPERADORES RELACIONALES
"""
UN OPERADOR RELACIONAL SE EMPLEA PARA COMPARAR Y ESTABLECER LA RELACION ENTRE ELLOS.
DEVUELVE UN VALOR BOOLEANO(True o False)BASADO EN LA CONDICION.

OPERADOR|              DESCRIPCION                           |      USO
    >	     Devuelve True si el operador de la izquierda       12 > 3 devuelve True

             es mayor que el operador de la derecha	           
    <	    Devuelve True si el operador de la derecha es 
            mayor que el operador de la izquierda	            12 < 3 devuelve False

    ==	    Devuelve True si ambos operandos son iguales	    12 == 3 devuelve False

    >=	    Devuelve True si el operador de la izquierda es 
            mayor o igual que el operador de la derecha	        12 >= 3 devuelve True

    <=	    Devuelve True si el operador de la derecha es 
            mayor o igual que el operador de la izquierda	    12 <= 3 devuelve False

    !=	    Devuelve True si ambos operandos no son iguales	    12 != 3 devuelve True
                        
"""
#                   EJEMPLOS:
a = 5
b = 3

print(a == b)  # False, 5 no es igual a 3
print(a != b)  # True, 5 es diferente de 3
print(a > b)   # True, 5 es mayor que 3
print(a < b)   # False, 5 no es menor que 3
print(a >= b)  # True, 5 es mayor o igual que 3
print(a <= b)  # False, 5 no es menor o igual que 3


# CONDICIONALES if - elif y else

"""
NORMALMENTE SE USA PARA COMPARAR DATOS , if SIEMPRE VA A TENER UN CONTEXTO VERDADERO Y else SIEMPRE UN CONTEXTO FALSO Y 
elif SE TRATA COMO = SI if ES UNA CONDICION FALSA ENTONCES elif PASA A SER LA VERDADERA COMO PUEDE SER FALSA IGUALMENTE.
PARA SABER MAS SOBRE LAS CONDICIONALES = https://www.freecodecamp.org/espanol/news/sentencia-if-else-de-python-explicacion-de-las-sentencias-condiciones/
"""
a = 10
b = 5
c = 7

if a < b:
    print(f"{b} es menor a {a}")
elif a > c:
    print(f"{a} es mayor a {c}")
elif c > b:
    print(f"{c} es mayor a {b}")
else:
    print(f"{a} es mayor a {b}")


edad = int(input("Ingresa la edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad")


nota = int(input("Ingresa tu nota: "))

if nota >= 90:
    print("Tienes una A.")
elif nota >= 80:
    print("Tienes una B.")
elif nota >= 70:
    print("Tienes una C.")
elif nota >= 60:
    print("Tienes una D.")
else:
    print("Tienes una F.")

edad = 25
ingresos = 30000

if edad >= 18 and ingresos >= 25000:
    print("Eres elegible para el préstamo.")
else:
    print("No eres elegible para el préstamo.")


# Ciclos for y while


"""
El ciclo for se utiliza para iterar sobre una secuencia (como una lista, una tupla, un diccionario, etc.) 
y ejecutar un bloque de código una vez para cada elemento de la secuencia.
"""
# Ciclo for()

nombres = ["Juan", "María", "Pedro"]

for nombre in nombres:
    print(nombre)


for i in range(1, 6):# recorre desde la primera posicion hasta 6 hiteraciones
    print(i) # 

# Ciclo while

"""
El bucle while en Python se utiliza para repetir un bloque de código mientras una condición específica sea verdadera.
Esto significa que el bloque de código dentro del bucle while se ejecutará repetidamente hasta que la condición 
se evalúe como falsa.

while condicion:
    # Bloque de código
    # que se ejecuta
    # mientras la condición sea verdadera

En este ejemplo, el bloque de código dentro del bucle while se ejecutará repetidamente mientras la variable contador 
sea menor que 5. 
En cada iteración del bucle, se imprime el valor actual del contador y luego se incrementa en 1. 
El bucle se detiene cuando la condición contador < 5 se evalúa como falsa.
Es importante tener cuidado al usar bucles while, ya que si la condición nunca se vuelve falsa, 
el bucle continuará ejecutándose indefinidamente, lo que podría llevar a un bucle infinito y hacer que el programa 
se bloquee o se vuelva no receptivo. Por lo tanto, es esencial asegurarse de que la condición en un bucle while 
eventualmente se vuelva falsa para evitar bucles infinitos.
"""
contador = 0

while contador < 5:
    print("El contador es:", contador)
    contador += 1

# LISTAS - DICCIONARIOS - TUPLAS
    

# LISTAS BASICA

"""RECORDAR QUE LAS LISTAS PUEDEN CONTENER TODOS LOS TIPOS DE DATOS DENTRO DE ELLAS Y LAS LISTAS SON MODIFICABLES
    En una lista, los elementos se almacenan secuencialmente en una estructura de datos contigua. 
    Cada elemento tiene un índice asociado que representa su posición dentro de la lista. 
    Los índices comienzan en 0 para el primer elemento, 1 para el segundo elemento, y así sucesivamente. 

                  mi_lista = ["a", "b", "c", "d"]
    # Índices u posiciones:    0    1    2    3 ........
    
    
    EJEMPLO:
    listaConbinada = ["Valentina",20,True,["PODEMOS ESPECULAR QUE ESTA ES UNA LISTA DENTRO DE OTRA"]]  

"""


nombres_Alumnos = ["Javiera","Carolina","Manuel","Lucas","Pablo","Natalia"] # CADENA DE TEXTO
listaSueldos = [1000000,23003440,32000000,4000000] # NUMEROS ENTEROS
estaturaTrabajadores = [1.60,1.45,1.83,2.10,1.91] # NUMEROS DECIMALES
binario = [True,False,False,True] # BOOLEANOS - 2 ESTADOS SON = VERDADERO Y FALSO
print(nombres_Alumnos)


"""
METODOS PARA LAS LISTAS:

append(): Agrega un elemento al final de la lista.
extend(): Extiende la lista agregando todos los elementos del iterable pasado como argumento.
insert(): Inserta un elemento en una posición específica de la lista.
Métodos de Eliminación:
remove(): Elimina la primera aparición de un elemento específico en la lista.
pop(): Elimina y devuelve el elemento en la posición especificada de la lista.
clear(): Elimina todos los elementos de la lista.
Métodos de Búsqueda y Ordenamiento:
index(): Devuelve el índice de la primera aparición de un elemento en la lista.
count(): Devuelve el número de veces que un elemento aparece en la lista.
sort(): Ordena los elementos de la lista en su lugar.
reverse(): Invierte el orden de los elementos en la lista.
Otros Métodos Útiles:
copy(): Devuelve una copia superficial de la lista.
len(): Devuelve la longitud (número de elementos) de la lista.
any(): Devuelve True si al menos un elemento de la lista es verdadero.
all(): Devuelve True si todos los elementos de la lista son verdaderos.

"""

"""
nombres_Alumnos = ["Javiera","Carolina","Manuel","Lucas","Pablo","Natalia"]
RECUERDA USAR EL print() PARA IMPRIMIR POR CONSOLA LAS LISTAS O DATOS QUE TENGAS
 LA LISTA nombres_Alumnos,ESTA SE VA A IMPRIMIR DE ESTA FORMA : [Javiera,Carolina,Manuel,Lucas,Pablo,Natalia]
    PARA RECORRER UNA LISTA SE USA EL CICLO for que significa(se usa para declarar la duración de una acción, el periodo de una acción o un evento)
PARA SABER MAS SOBRE EL CICLO for ve al siguiente enlace = https://j2logo.com/bucle-for-en-python/
"""

# LA FORMA CORRECTA DE RECORRER UNA LISTA Y MOSTRAR SUS DATOS: 
for nombres in nombres_Alumnos:
    print(nombres)

# FORMA MAS "PROFESIONAL" DE ENLISTAR LOS ELEMENTOS O DATOS DE LA LISTA"
contador = 0 
for nombres in range(contador,len(nombres_Alumnos)):
    contador += 1
    print(f"{contador}._{nombres_Alumnos[nombres]}")
# SALIDA POR CONSOLA:
"""
    1._Javiera
    2._Carolina
    3._Manuel
    4._Lucas
    5._Pablo
    6._Natalia
"""
# LISTAS COMPLEJAS
# CREAMOS LISTA PRODUCTOS 

productos = ["Gaseosas",["Coca-Cola","Fanta"],"Pastas",["Tallarines","Corbatas"],]

for elementos in productos: # PRIMER RECORRIDO NOS ARROJA LOS VALOES QUE ESTAN FUERA DE LAS LISTAS QUE CONTIENE LA PRIMERA LISTA, NOS ARROJARA = Gaseosas y Pastas   
    if isinstance(elementos,list):# EN ESTA LINEA DE CODIGO SE VERIFICA SI EL OBJETO DE LA PRIMERA LISTA ES LISTA O NO ES UNA LISTA.
        for bebidas in elementos: # SEGUNDO RECORRIDO QUE NOS MOSTRARA LAS LISTAS CON DE LAS GASEOSAS Y LAS PASTAS = Coca-Cola - Fanta Y Tallarines - Corbatas
            print(" -",bebidas)
    else:
        print(elementos)# IMPRIME LOS OBJETOS DE LA PRIMERA LISTA = Gaseosas y Pastas 
# SALIDA POR CONSOLA: 
"""
Gaseosas
 - Coca-Cola
 - Fanta
Pastas
 - Tallarines
 - Corbatas

"""

# DICCIONARIOS
"""
Un diccionario en Python es una estructura de datos que permite almacenar pares clave-valor. 
Cada elemento en un diccionario consiste en una clave y su valor correspondiente. Los diccionarios son mutables, 
lo que significa que puedes modificar, agregar o eliminar elementos después de su creación.

Cada elemento consiste en una clave y un valor asociado. Internamente, Python utiliza una función de hash para 
calcular la ubicación de almacenamiento de cada clave en la memoria. Esto significa que no hay un concepto directo de 
posición o índice en un diccionario, ya que los elementos no están ordenados secuencialmente. 
Sin embargo, puedes acceder a los valores asociados a las claves utilizando las claves correspondientes. Por ejemplo:

mi_diccionario = {"nombre": "Juan", "edad": 30}
    # Claves:     "nombre"          "edad"
    # Valores:              "Juan"          30
"""

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

"PARA ACCEDER A LOS VALORES SE USA LOS CORCHETES []"
print(mi_diccionario["nombre"])  # Salida: Juan
print(mi_diccionario["edad"])    # Salida: 30
print(mi_diccionario["ciudad"])  # Salida: Madrid

"PARA MUTAR O MODIFICAR UN DICCIONARIO"
mi_diccionario["edad"] = 35
mi_diccionario["ciudad"] = "Lima"

"""
METODOS UTILES PARA LOS DICCIONARIOS:

get(): Devuelve el valor asociado a una clave específica. Si la clave no existe, devuelve un valor predeterminado opcional.
keys(): Devuelve una vista de todas las claves en el diccionario.
values(): Devuelve una vista de todos los valores en el diccionario.
items(): Devuelve una vista de todos los pares clave-valor en el diccionario.
Métodos de Agregado y Actualización:
update(): Agrega los pares clave-valor de otro diccionario o de una secuencia de pares clave-valor al diccionario.
setdefault(): Devuelve el valor asociado a una clave específica. Si la clave no existe, la agrega con el valor predeterminado opcional.
Métodos de Eliminación:
pop(): Elimina y devuelve el valor asociado a una clave específica.
popitem(): Elimina y devuelve un par clave-valor arbitrario del diccionario.
clear(): Elimina todos los elementos del diccionario.
Otros Métodos Útiles:
copy(): Devuelve una copia superficial del diccionario.
len(): Devuelve la cantidad de pares clave-valor en el diccionario.
"""

# EJEMPLOS DE USO:

mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}

# Acceder al valor asociado a una clave
print(mi_diccionario.get("nombre"))

# Obtener todas las claves
print(mi_diccionario.keys())

# Obtener todos los valores
print(mi_diccionario.values())

# Obtener todos los pares clave-valor
print(mi_diccionario.items())

# Actualizar el diccionario con otro diccionario
mi_diccionario.update({"profesion": "Ingeniero"})

# Eliminar un par clave-valor
mi_diccionario.pop("edad")

# Copiar el diccionario
copia_diccionario = mi_diccionario.copy()

# Obtener la cantidad de pares clave-valor
print(len(mi_diccionario))


# DICCIONARIOS COMPLEJOS

"""
El método items() es útil cuando necesitas acceder tanto a las claves como a los valores de un diccionario al mismo tiempo. 
Puedes utilizarlo en bucles for para iterar sobre todos los pares clave-valor, o para convertir el contenido del diccionario 
en una lista de tuplas para realizar operaciones adicionales.

Por ejemplo, puedes utilizar items() para:

Imprimir todos los pares clave-valor.
Realizar búsquedas o filtrar elementos específicos del diccionario.
Convertir el diccionario en una lista de tuplas para su posterior procesamiento o manipulación.
"""

alumnos = {
    "grupo1": ["Juan", "María", "Pedro"],
    "grupo2": ["Ana", "Luis", "Eva"]
}
# RECORREMOS EL DICCIONARIO CON LAS LISTAS DENTRO
for grupo,lista_Alumnos in alumnos.items():
    print(f"Grupo:{grupo}")
    for alumno in lista_Alumnos:
        print(f"- {alumno}")


productos = {
    "producto1": {"nombre": "Laptop", "precio": 1000},
    "producto2": {"nombre": "Teléfono", "precio": 500},
    "producto3": {"nombre": "Tablet", "precio": 300}
}

# RECORREMOS EL DICCIONARIO
for clave, valor in productos.items():
    print(f"Clave: {clave}")
    print(f"Nombre: {valor['nombre']}, Precio: {valor['precio']}")


# TUPLAS
    
"""
Las tuplas en Python son estructuras de datos similares a las listas, pero son inmutables, 
lo que significa que no se pueden modificar una vez creadas. 
Se utilizan para almacenar una colección ordenada de elementos y son útiles cuando quieres garantizar 
que los datos no cambien accidentalmente. 

ejemplos: 
"""

mi_tupla = (1, 2, 3, 4, 5)

# IMPRIMIR POR POSICION EN LA TUPLA
print(mi_tupla[0])  # Salida: 1

# REASIGNAR VALORES DE LA TUPLA A DISTINTAS VARIABLES
tupla = (1, "dos", 3.0)
a, b, c = tupla
print(a)  # Salida: 1
print(b)  # Salida: dos
print(c)  # Salida: 3.0

# ITERACIONES
for elemento in mi_tupla:
    print(elemento)

# LONGITUD DE LA TUPLA
print(len(mi_tupla))  # Salida: 5

# CONCATENAR 2 TUPLAS
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)  # Salida: (1, 2, 3, 4, 5, 6)

# CONDICIONAL
if 5 in mi_tupla:
    print("5 está en la tupla")
else:
    print("5 no existe en la tupla")

# CONVERTIR UNA LISTA EN UNA TUPLA
lista = [1, 2, 3]
tupla = tuple(lista)









