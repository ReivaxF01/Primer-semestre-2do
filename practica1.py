#Esto es un comentario
print ("Hola, Mundo")

'''
Comentario en  varias lineas
USO DE VARIABLES 
El nombre de una variable debe empezar por una letra o por el guión bajo.
El nombre de una variable no puede empezar por un número
Un nombre de variable sólo puede contener caracteres alfanuméricos y guiones bajos (A-z, 0-9 y _ )
Los nombres de las variables distinguen entre mayúsculas y minúsculas (edad, Age y AGE son tres variables diferentes)
Un nombre de variable no puede ser ninguna de las palabras clave de Python.
'''

x = 5
y = "John"
#y= "Maria"
print(x)
print(y)

#Declarar y asignar variables
a = str(5)    
b = int(7)    
c = float(9)
d = bool(1)

#Comillas simples o dobles y distingue en minusculas y mayusculas
n="pedro"
N= 'marcelo'
print(n)
print(N)

#Multiples variables 
x, y, z = "pedro", "ana", "Cristian"
print(x)
print(y)
print(z)

#Print puede mostrar varias variables separadas por coma. También se puede usar  el operador + 

x = "Python"
y = "es "
z = "muy bacan"
j= 12
k= 9
print(x, y, z)
print(x + y + z)
print(j + k)     #En numeros suma

# DATOS  NUMERICOS   
a = 1    # int
b = 2.8  # float
c = 1j   # complex
d= -3456   #int
e= 3.1435  #float

#Convertir 
f =float(a)
g= int(e)

nombre= input("Nombre: ")
edad=input("Edad: ")
print(nombre, edad, sep="\t", end=".")
print("nombre ",nombre, " edad : ", edad)
print("nombre " +nombre+ " edad : ", edad)

#print("ingrese una nota")
n1=float(input("ingrese una nota"))
#PYTHON la entrada de datos input la convierte en str (string=cadena)
print("ingrese otra nota")
n2=float(input())
print("ingrese otra nota")
n3=float(input())
prom=(n1+n2+n3)/3
print("el promedio es ",prom)
