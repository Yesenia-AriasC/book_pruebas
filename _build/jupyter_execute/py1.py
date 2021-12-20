#!/usr/bin/env python
# coding: utf-8

# (2:py1)=
# 

# # <span style="color:#F72585">Introducción al lenguaje Python</span>

# ## <span style="color:#4361EE">Introducción</span>

# Este es un cuaderno introductorio a Python diseñado en JupyterLab, exploraremos las funciones básicas disponibles de **Python** y la programación básica para su posterior uso en el diplomado. Comencemos con un ambiente de **Python 3**. Para una introducción más extensa, ir [aquí](https://www.w3schools.com/python/).

# ## <span style="color:#4CC9F0">¿Qué es Python?</span>

# ![Logo Python](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)
# 
# 
# 
# Python es un lenguaje de programación (¿Qué es un programa?) popular que se usa normalmente para:
# 
# * Desarrollo web en servidores,
# * Desarrollo de Software,
# * Cálculos Matemáticos,
# * Desarrollo de Scripts.

# ## <span style="color:#4CC9F0">¿Qué puede hacer Python?</span>

# * Puede ser usado en un servidor para crear **aplicaciones web**,
# * Puede conectarse a sistemas de **bases de datos**. Puede leer y modificar archivos.
# * Puede ser usado para manejar **Big Data** y hacer cálculos matemáticos de alta complejidad.
# * **Prototipo rápido** para producción de Software.

# ## <span style="color:#4CC9F0">¿Por qué Python?</span>

# * Funciona en diferentes **plataformas** (Windows, Mac, Linux, etc).
# * Tiene una **sintaxis** (forma de escribir) simple, similar al idioma inglés.
# * Tiene una sintáxis que permite escribir programas en **muy pocas líneas**, comparado con otros lenguajes de programación.
# * Pyhton se ejecuta en un **sistema interpretado**. Es decir, que los códigos se pueden correr **justo después de ser escritos**; en otras palabras, no necesitan compilación previa.
# * Se puede usar como un lenguaje **clásico**, como un lenguaje **orientado a objetos**, o como un lenguaje **funcional**.
# * Es el principal lenguaje de la **Ciencia de Datos**.

# ## <span style="color:#4CC9F0">Hello World!</span>
# 

# El primer ejemplo clásico de programación es saludar, o sea, decirle al computador que muestre un saludo. Para esto, se usa la función de Python llamada **print**. Para colocar un saludo (o un **texto cualquiera**), se debe colocar entre **comillas dobles o sencillas** dentro del comando print. Entonces, para que el computador muestre un saludo, por ejemplo **Hello, World!**, debemos escribir en ambiente de código como sigue
# 

# In[1]:


print("Hello friend. Hello friend?")


# Note que el resultado se muestra sin las comillas dobles. Estas comillas dobles se usan para decirle al computador que vamos a ingresar texto. Si quisieramos escribir con un salto de linea escribimos "\n" así al escribir `print("Hola\nMundo")` tenemos:
# 

# In[2]:


print("Hola\nMundo")


# ### <span style="color:#4CC9F0">Variables en Python</span>
# 
# Escriba un código que le diga a Python que devuelva el texto:
# *****
# >*Sólo sé ...*  
# *... que nada sé.*
#  ***

# In[3]:


# Escriba el código aqui


# # <span style="color:#F72585">Variables en Python</span>

# Una variable sirve para **guardar un valor específico**, ya sea **numérico**, **texto** u otro **tipo de Dato** con el nombre con la que se nombre dicha variable. Observe el siguiente ejemplo.

# In[4]:


# Asignamos 1 a la variable x

x = 1

print("El valor de la variable x es", x)

# Asignamos "¡Vamos a programar!" a la variable y

y = "¡Vamos a programar!"

print("\nEl valor de la variable y es", y)


# ## <span style="color:#4361EE">Asignación dinámica en Python</span>

# En Python, como en R, Julia, Matlab y otros lenguajes no es necesario declarar una variable de antemano, como ocurre en otros lenguajes como C, C++ y muchos otros lenguajes de bajo nivel. 
# La asignación dinámica implica que es posible cambiar el tipo de dato de una variable con tan solo reasignarle un valor. En Python, se delega al programador la responsabilidad de cuidarse de efectos no esperados al cambiar el tipo de una variable. Vea el siguiente ejemplo.

# In[5]:


x = 5.6
print('x es número un real:', x)

x = 3+4j
print('x es ahora un número complejo:', x)

x = '25 de mayo'
print('En cambio ahora x es un string:', x)


# (py1:ej1)=
# ## <span style="color:#4361EE">Reglas para la creación de variables</span>

# * El nombre de una variable **debe comenzar** con una letra ó con _.
# * El nombre de una variable **no puede comenzar** con un número.
# * El nombre de una variable **sólo puede contener** carácteres alfa-numéricos.
# * El nombre de una variable tiene **sensibilidad** a **mayúsculas** y **minúsculas** (x es diferente de X).

# 
# ### <span style="color:#4CC9F0">Ejercicio</span>

# Escriba un código que le diga a Python que devuelva los textos **Tengo** *my_age* **años**, donde *my_age* es una variable que tenga asignada su edad.

# In[6]:


# Escriba aquí


# ## <span style="color:#4361EE">Tipos de datos básicos en Python</span>

# ### <span style="color:#4CC9F0">Enteros (int)</span>

# Considere el siguiente ejemplo:

# In[7]:


x = 1
print(x)
print(type(x))
x = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
print(x)
print(type(x))


# Se observan dos cosas interesantes. Primero, el tipo de dato es una clase 'int'. Todo en Python son objetos, incluidos la variables simples. En otro cuaderno estudiaremos las clases y objetos en detalle. 
# 
# Segundo, En Python puede tener números enteros tan grandes como desee, a diferencia de otros lenguajes. de otros lenguajes.

# Para convertir un tipo de dato diferente a int, siempre que sea posible se usa el *cast* int. Por ejemplo

# In[8]:


# '120' es un string

total = '120'
print(total)
print(type(total))

total = int('120')
print(total)
print(type(total))


# #### Usando input

# La sentencia *input* se utiliza para solicitar información al usuario. *input* siempre regresa un string.

# In[9]:


edad = int(input('Por favor entre su edad:'))
print(edad)
print(type(edad))


# ### <span style="color:#4CC9F0">Punto Flotante (float)</span>

# Lo número reales son representados usando el estándar IEEE 754 double precision.

# In[ ]:


x = 1.56
print(x)
print(type(x))


# ### <span style="color:#4CC9F0">Números complejos (complex)</span>

# Se representan en la forma $a + bj$, en donde $a$ es la parte real y $ b$ la parte imaginaria

# In[ ]:


z = 3.4 + 4j
print(z)
print(type(z))


# ### <span style="color:#4CC9F0">Booleanas (bool)</span>

# El tipo booleano se utiliza para variables que solamente pueden ser 'True' o 'False', es decir, valores booleanos o lógicos. Por ejemplo:

# In[ ]:


t = True 
print(t)
print(type(t))


# ### <span style="color:#4CC9F0">None</span>

# Este es un tipo especial de dato utilizado para indicar que una determinada variable no contiene ningún dato. Es muy útil en el control de muchas situaciones, porque sirve para saber si algún objeto a llegado a ser None. Mire el siguiente ejemplo.

# In[ ]:


b = None
print(b)
print(type(b))

z = 5

b is None


# In[ ]:


# Pruebe: z is None


# ### <span style="color:#4CC9F0">Textos: strings</span>
# 

# 
# Los string son expresiones que representan una cadena de caracteres, útiles para escribir mensajes y combinarlos con valores que generemos en nuestros procesamientos. Para escribir un texto en Python usamos comillas simples: `'...'` o comillas dobles: `"..."`. Combinamos comillas para poner comillas adentro:

# In[ ]:


a='Texto simple escrito entre comillas simples'
print(a)
a


# In[ ]:


b="Texto simple escrito entre comillas dobles"
print(b)
b


# In[ ]:


c='Texto simple escrito entre comillas simples que necesita "adentrico" comillas dobles'
print(c)


# In[ ]:


d="Texto simple escrito entre comillas dobles que necesita 'adentro' comillas simples"
print(d)


# Como vimos, la función print es la que nos permite imprimir estos mensajes. El texto \n indica una nueva linea en el texto:

# In[ ]:


print("Una línea\nOtra línea")


# No obstante, a veces necesitamos escribir  \n en un mensaje:

# In[ ]:


print('La ruta del archivo es C:\nombres\archivo.ipynb')


# En este caso la aparición del símbolo  \  dañó el mensaje. La primera solución es la siguiente. ¿puede explicarla por favor?

# In[ ]:


print('La ruta del archivo es C:\\nombres\\archivo.ipynb')


# Una segunda solución para resolver el problema consiste en escribimos r antes del string, así:

# In[ ]:


# Qué significa la r???
print(r'La ruta del archivo es C:\nombres\archivo.ipynb')


# Finalmente, podemos recorrer los valores de la cadena de texto de la siguiente forma:

# In[ ]:


texto="cuidado_con_el_orden"
texto


# Extrayendo el elemento cero del texto (**primer caracter**):

# In[ ]:


print(texto[0])


# Extrayendo el elemento uno del texto (**segundo caracter**):

# In[ ]:


texto[1]


# Extrayendo el elemento cinco hasta el elemento 9 del texto (**sin incluir el 9**):

# In[ ]:


texto[5:9]


# **También se pueden usar índices negativos** (Python exclusive):

# In[ ]:


texto[3:-1]


# In[ ]:


texto[-1]


# (py1:ej2)=
# ## <span style="color:#4361EE">Asignación múltiple</span>

# Es posible asignar valores a diferentes variables en una línea de código:

# In[ ]:


# Asignación múltiple

w, x, y, z = "Apple", "Watermelon", "Grape", 28;

print(w);
print(x);
print(y);
print(z);
print(w,x,y,z,sep=", ");


# También es posible asignar un **mismo valor** a diferentes variables:

# In[ ]:


# Asignación múltiple del mismo valor

x1 = x2 = x3 = 0.5;
print('x1 =',x1);
print('x2 =',x2);
print('x3 =',x3);


# ### <span style="color:#4CC9F0">Ejercicio</span>

# Explique qué hace el siguiente código. Imprima

# In[ ]:


x, y = 3, 10

y, x = x, y

print(y,x)


# :::{admonition} Cuidado con las variables no asignadas
# :class: warning
# Generan error al usarse sin ser asignadas.
# 
# Observe el siguiente ejemplo:
# :::
# 
# 

# In[ ]:


n # Variable sin asignar


# ## <span style="color:#4361EE">Suma de variables y concatenación de variables</span>

# Python es tan sencillo e intuitivo, que es posible sumar diferentes variables y sumarlas con el símbolo **+**. Cuando las variables son numéricas, se **suman matemáticamente** y cuando es texto se **concatenan**.

# In[ ]:


# Sumar dos textos

x = "Python is "; 
y = "awesome";
z =  x + str(y);
print(z);

# Sumar dos números

n1 = 1;
n2 = 5;
suma = n1 + n2;
print(suma);

# Escribir texto y números
print(x+"the number",n1);


# En el apartado anterior es claro que usamos dos tipos de variables unas textuales y otras numéricas, profundicemos en estos temas.

# ## <span style="color:#4361EE">Operadores Aritméticos y redondeo</span>

# La fortuna de que Python reconozca variables numéricas nos permite usarla como una calculadora simple, podemos ejecutar operaciones muy sencillas teniendo en cuenta la siguiente tabla:
# 
# | **Operador** | **Descripción** |
# | :---: | :---: |
# |`+`|Suma|
# |`-`|Resta|
# |`*`|Multiplicación|
# |`/`|División|
# |`**`|Potencia|
# 

# ### <span style="color:#4CC9F0">Ejemplo</span>

#  Si queremos operar:
#  
#  $$ 5\times(3-5)^2-\cfrac{6}{(9)^{1/2}}$$
#  
#  tenemos que escribir:

# In[ ]:


5*(3-5)**2-(6)/(9**(1/2))


# *Recuerde oprimir [Shift]+[Enter]*.
# 
# El orden en que se interpretan las expresiones es como en todos los demás lenguajes comunes de programación.

# ### <span style="color:#4CC9F0">Ejercicio</span>

# Es muy importante usar bien los paréntesis, el uso o desuso puede generar problemas graves en las cuentas, encuentre el error y describa lo que hizo la máquina en los siguientes casos respecto a la operación anterior:

# In[ ]:


5*3-5**2-(6)/(9**(1/2))


# In[ ]:


5*(3-5)**2-6/(9**1/2)


# In[ ]:


5*(3-5)**2-6/9**1/2


# In[ ]:


5*3-5**2-6/9**1/2


# ### <span style="color:#4361EE">Divsión y residuo entre enteros</span>

# La división es una operación bien especial pues la mayoría de ocasiones produce un número con parte fraccionaria. Sin embargo, cuando estábamos pequeños nos enseñaron a dividir enteros dando como respuesta un entero llamado cociente y lo que hacia falta para completar la división, un número llamado residuo. En Python podemos calcular esos valores con `\\` para el cociente y `%`para el residuo. Por ejemplo, sabemos que:
# 
# $$ 20 \div 3 = 6 \ \ \ \text{ con residuo } 2$$
# tenemos:

# In[ ]:


20//3


# In[ ]:


20%3


# In[ ]:


3+(-4)**(1/2) # Recordemos un poquito de nuestras matemáticas


# Finalmente, una función elemental y útil para el tratamiento de números decimales es `round`. Lo usamos para redondear los valores a uno con el decimal que escojamos. Tenemos:

# In[ ]:


n1=47/3
n1


# In[ ]:


n2=round(n1)
n2


# In[ ]:


n3=round(n1,3)
n3


# ### <span style="color:#4CC9F0">Ejercicio</span>

# Use la función ```round()``` para redondear el número $\pi$ hasta 5 cifras decimales.
# 
# **Pista:** Para poder usar el número $\pi$, use el siguiente código:

# In[ ]:


# importando el número pi

from math import *

# visualizar pi
print(pi)

# Your code here
round(pi,5)


# # <span style="color:#F72585">Estructuras de control</span>
# 

# En cualquier lenguaje de programación existen tres estructuras de control básicas que corresponden a 
# 
# - Secuencia
# - Selección (o decisión)
# - Iteración (repetición)

# ## <span style="color:#4361EE">Secuencia</span>
# 

# La ejecución de cualquier programa (algoritmo codificado en algún lenguaje de programación) se realiza en orden de aparición de las sentencias. Una **sentencia** puede ser **simple** (solamente una instrucción) o **compuesta** (varias instrucciones).

# ### <span style="color:#4CC9F0">Ejemplo</span>

# Observe el siguiente código Python:

# In[ ]:


x = 1; 
y = 2;

print(x,y)


# En el ejemplo hay tres sentencias. Dos sentencias de asignación de valores y una sentencia de impresión. Se ejecuta una después de la otra.

# ## <span style="color:#4361EE">Selección (if)</span>

# Esta estructura de control está diseñada para que un programa pueda seguir diferentes caminos de ejecución, dependiendo de la evaluación de una expresión lógica. Observe el siguiente ejemplo.

# In[ ]:


# ejemplo if
x = 5
y = 3

if x>y:
    print("Cinco es mayor que Tres")
    print("lunes")


# La estructura empieza con la palabra clave **if**. Luego aparece una condición lógica que es evaluada (x>y). Si la condición es verdadera, como en este caso, se ejecutan las instrucciones escritas dentro de la estructura.
# 
# Ahora observe el siguiente cambio

# In[ ]:


# ejemplo if
x = 3
y = 5

if x>y:
    print("Cinco es mayor que Tres")
    print("lunes")


# En este caso,  no se imprime nada, debido a que la condición es falsa. Ahora observe el siguiente ejemplo

# In[ ]:


# ejemplo if
x = 3
y = 5

if x>y:
    print("La condición es verdadera")
    print("Lunes")
else:
    print('La condición es falsa')
    print('Martes')


# ::: {admonition} Pregunta
# :class: question
# De acuerdo al script anterior, ¿cuál es la función de la clúsula **else**?
# :::

# ### <span style="color:#4CC9F0">Ejercicio</span>

# Cambie el código anterior para que corra el otro camino de ejecución.

# In[ ]:


# Consigne su respuesta aquí.


# ### <span style="color:#4CC9F0">Ejercicio</span>

# El siguiente código calcula la longitud del nombre y escribe una frase acorde a la longitud. Observe que en el comando `print()` , `sep=` es un parámetro que separa los valores ingresados dentro de la función print. Como vemos, escribimos `N='Tu_nombre'` eso asigna a la letra N el texto *Tu_nombre*.  La función *len* devuelve la longitud de la cadena.

# In[ ]:


N='Daniel'# cambiar 'Tu_nombre' por su verdadero nombre
if len(N)>10:
    A="es un nombre muy largo"
else:
    A="es un nombre muy corto"

print(N,A,sep=" ")


# In[ ]:


N='Alvaro Mauricio Montenegro Díaz' #cambiar 'Tu_nombre_completo' por su verdadero nombre completo
if len(N)>10:
    A="es un nombre muy largo"
else:
    A="es un nombre muy corto"

print(N,A,sep="/")


# In[ ]:


N='El nombre'
if len(N)>10:
    A="es un nombre muy largo"
else:
    A="es un nombre muy corto"

print(N,A,sep="         ")


# ## <span style="color:#4361EE">Indentación en Python</span>

# Indentar significa **mover un bloque de texto hacia la derecha**, dejando una serie de espacios o un tabulador para distinguirlo del texto alineado a la izquierda. 
# 
# Por ejemplo:
# 
# > Este texto está indentado.
# 
# En **Python**, la identación es obligatoria para indica el alcance de una estructura. Además solamente debe usarse para tal fín.

# ### <span style="color:#4CC9F0">Ejemplo: Identación en Python</span>

# En este ejemplo

# In[ ]:


# ejemplo if
x = 3
y = 5

if x>y:
    print("Five is greater than Three")
    print("lunes")
    
# por fuera del if
x = 9.6
print(x)
    


# ```{admonition} Nota
# **Sin la indentación**, el código produce un **error**.
# ```

# In[ ]:


x = 3
y = 5
print(x,y)

if x>y:
print("Five is greater than Three")


# ## <span style="color:#4361EE">Operadores de comparación</span>

# | **Operador** | **Descripción** |**Ejemplo**|
# | :---: | :---: |:---: |
# |`==`|Prueba si dos valores son iguales| 3==3|
# |`!=`|Prueba si dos valores no son iguales entren si| 2!=3|
# |`<`|Prueba si el valor de la izquierza es menor que el de la derecha|4<3|
# |`>`|Prueba si el valor de la izquierza es mayor que el de la derecha|4<3|
# |`<=`|Prueba si el valor de la izquierza es menor o igual que el de la derecha|4<=3|
# |`>=`|Prueba si el valor de la izquierza es mayor igual que el de la derecha|4<=3|

# ## <span style="color:#4361EE">Operadores Lógicos</span>

# | **Operador** | **Descripción** |**Ejemplo**|
# | :---: | :---: |:---: |
# |`and`|Regresa verdadero si el valor de las izquierda y el de la derecha son verdaderos| (3<4) and (5>1)|
# |`or`|Regresa verdadero si uno de los dos valores a(izquierda o derecha es verdadero, o ambos| (3<4) or (5<1)|
# |`not`|Regresa verdadero si el valor que se esta evaluado es falso|not 3>2|

# ### <span style="color:#4CC9F0">Ejercicio</span>

# Verifique que entiende qué hace el siguiente código. ¿Cuál es la salida?

# In[ ]:


edad = 15
status = None

if (edad >12) and (edad<20):
    status = 'adolescente'
else:
    status = 'no adolescente'

print(status)


# ## <span style="color:#4361EE">Estructura de repetición [ciclos]</span>
# 

# Este tercer tipo de estructura de control se usa para los casos en los cuales es necesario correr un proceso varas veces en forma continua.

# ### <span style="color:#4CC9F0">Ciclo while</span>

# Al comienzo del ciclo se evalúa una condición. Si la condición es verdadera se ejecuta de nuevo el ciclo. En otro caso, termina. Corra y analice el siguiente fragmento (snippet) de código

# In[ ]:


contador = 0

print('Starting')
while contador < 10:
    #Instrucciones útiles
    print(contador,' ', end='')
    contador = contador + 1
    
print()
print('Done')


# ### <span style="color:#4CC9F0">Ejercicio</span>

# ¿Qué hace el parámetro  *end* en el *print* anterior? 

# ### <span style="color:#4CC9F0">Ciclo for</span>

# En este caso se usa una variable de salto que va recorriendo un conjunto de valores hasta terminar. Revise el siguiente snippet.

# In[ ]:


print('\nStart:')
for i in range(20):
    # Instrucciones útiles
    print(i, ' ', end='')

print('\nDone.')


# ::: {admonition} Pregunta
# :class: question
# ¿Cuál es la diferencia entre while y for?
# :::

# #### Break

# Se usa para terminar la ejecución de un ciclo while o for. Corra el siguiente ejemplo dadno difentes valores.

# In[ ]:


for  i in range(10):
    print(i)
    if i==5:
        break


# ## <span style="color:#4361EE">Estructuras de control anidadas</span>

# Es posible incluir (o anidar) estructuras de control dentro de otras estructuras de control.
# 
# Esto es de gran utilidad para realizar programas de mayor complejidad.
# 
# **Ejemplo:**

# In[ ]:


x = 5
y = 3
print(x,y)


# In[ ]:


if x>y:
    print("Cinco es mayor que tres")
    for i in range(10):
        print(i)
    x = 9.9

y = 2
print(x, y)


# No importa cuántos espacios en blanco se dejen, siempre y cuando sea **al menos uno**:

# In[ ]:


if 5 > 3:
    print("Five is greater than Three")  
if 5 > 3:
       print("Five is greater than Three")


# ### <span style="color:#4CC9F0">Ciclos anidados</span>

# Un ejemplo de ciclos anidados, por ejemplo crear las tablas de multiplicar, puede ser de gran utilidad para realizar procesos iterativos.
# 
# **Ejemplo:**

# In[ ]:


print("\nAlgunas Tablas de Multiplicar:")
for i in range(1,5): # i va aumentado desde 1, luego va a 2,3,...
    print(f'\nTabla del {i}\n')
    for j in range(1,13): # Recorre desde el 1 hasta el 12
        print(i,"x",j," = ",i*j,sep='')


# **Ejemplo 2:**

# In[ ]:


for i in range(0,11):             #line 1
    for j in range(i):            #line 2
        print('*', end='')        #line 3
    print('')                     #line 4


# ### <span style="color:#4CC9F0">Ejercicio</span>

# Escriba un código que le diga al computador que devuelva los textos **I'm ready to code!** si su nombre tiene más de diez caracteres o **Hello, World!** si pasa lo contrario, para medir la longitud de su nombre utilice la función `len()`.

# In[ ]:


len("Tu_nombre") #pruebe la funcion len. Cambia Tu_nombre por su nombre real.


# In[ ]:


# Ingrese aquí el condicional


# ## <span style="color:#4361EE">Autores</span>

# 1. Alvaro Mauricio Montenegro Díaz, ammontenegrod@unal.edu.co
# 1. Daniel Mauricio Montenegro Reyes, dextronomo@gmail.com 

# ## <span style="color:#4361EE">Comentarios</span>
# 
