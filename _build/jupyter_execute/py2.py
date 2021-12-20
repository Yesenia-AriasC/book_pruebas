#!/usr/bin/env python
# coding: utf-8

# (2:py2)=
# 

# # <span style="color:#F72585">Funciones en Python</span>

# 
# 
# Para entender funciones en Python (Paquetes dentro de módulos de Python), debemos pensar en actos reales para poder hacer una **analogía** en el ambiente de programación.
# 
# Imagínese cuando se levanta.
# 
# Lo que ocurre primero, es que uno se siente vivo, se abren los ojos (no siempre), se hace pereza un rato, se levanta de la cama y luego se inicia el día (cada persona tiene sus maneras diferentes de lograrlo).
# 
# Esta serie de **pasos consecutivos** conforman lo que se llama una **función**.
# 
# En el común, una **función es en realidad una acción** o una serie de acciones que generan un resultado a través de un proceso intermedio.
# 
# Para poder distinguir funciones, unas de otras, se le dan dotado de nombres diferentes.
# 
# Por ejemplo, la función antes descrita podría nombrarse como **Levantarse**:
# 
# Está función se compone de los siguientes pasos:
# 
# 1. **Sentirse vivo.**
# 2. **Abrir los ojos.**
# 3. **Hacer pereza.**
# 4. **Levantarse.**
# 
# En el lenguaje de programación, ésto se podría escribir como
# 
# ```Levantarse(x)```
# 
# donde $x$ representa el individuo que hace la acción y los paréntesis significan que se habla de una función, y por lo tanto, **no se confunde** con una variable.
# 
# **Ejemplo:**
# 
# Función ```CortarManzana(x)```:
# 
# Esta función se puede ilustrar de la siguiente manera:
# 
# 
# ![Manzanita](https://photos1.blogger.com/blogger/1290/1572/1600/Apple_slicing_function.png)
# 
# Como podemos ver, una función es realmente es una **"Caja Negra"**:
# 
# La podemos usar, sin importar qué hay dentro de ella.
# 
# Ya hemos visto algunas **funciones básicas** de Python (Built-in):
# 
# - ```print()```
# - ```len()```
# - ```list()```
# 
# En [este link](https://docs.python.org/3/library/functions.html), se encuentra un manual de todas las funciones **básicas** de Python.
# 
# Veamos algunas de ellas:
# 
# **Ejercicio**
# 
# Viendo la entrada y salida del código, infiera qué hace la función correspondiente:

# In[1]:


# Your Code Here
x = -5
y = abs(x)
print("\nx =", x)
print("y = ", y,"\n")

# Your Code Here

d = dict({"Saludo": "Hola", "Despido": "Adiós", "Palabra": "Extraño"})
print("Dicionario: ",d,"\n")

# Suma
v = [1,2,3,4,5,6]
s = sum(v)
print("resultado:", s,"\n")

# Your Code Here

a1=max(v)
a2=min(v)

print("a1:",a1,", a2:",a2)


# ## <span style="color:#4361EE">Parámetros y Variables en Funciones:</span>

# Las funciones pueden tener uno o más parámetros asociados.
# 
# Por ejemplo la función $f(x,y,z)=w$, recibe los argumentos $x,y,z$ y produce el resultado $w$.
# 
# **Ejemplo:**

# In[2]:


get_ipython().system('pip install numpy matplotlib')


# In[3]:


# Comente adecuadamente las siguientes líneas de código

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,2*np.pi,30)
y=np.sin(x)

print("x=\n",x,"\n")
print("y=\n",y,"\n")
plt.plot(x,y)
plt.show()


# **Ejercicio:**
# 
# 1. Investigue las funciones y atributos internos de matplotlib para hacer una matriz 3x1 que contengan:
# 
# - Una función matemática.
# - Una foto.
# - Una esfera con puntos aleatorios en su frontera.
# 
# 2. Investigue sobre 5 funciones de Python que acepten al menos 3 parámetros.
# 
# 3. Use la libreria ```pandas``` para hacer gráficos útiles sobre el ```Predio_206.csv```.

# ## <span style="color:#4361EE">Creación de Funciones</span>

# También es posible crear funciones para generar rutinas específicas.
# 
# Hay dos maneras de generar funciones en Python:
# 
# 1. **def**
# 2. **lambda**
# 
# **Ejemplo:**

# In[4]:


# Explicar las siguientes líneas de código
def mysum_prod(x,y):
    s=x+y
    p=x*y
    return s,p


# In[5]:


suma, prod = mysum_prod(3,4)
print("El suma es:", suma)
print("El producto es:", prod)


# In[6]:


#  Use la función correspodiente de forma inteligente
def mysum_prod(x,y):
    s=x+y
    p=x*y
    return [s,p]


# In[7]:


# Explique qué diferencias hay entre éste método y el anterior

sumita = lambda arg1,arg2: arg1+arg2

a=6
b=65
s = sumita(a,b)
print("la suma es:", s)


# ## <span style="color:#4361EE">¿Cuál es la diferencia y utilidad de la función lambda?</span>
#  
# 
# **Pista:**

# In[8]:


# Explicar adecuadamente

def myfunc(n):
    return lambda a : a * n 


mydoubler = myfunc(2)
#print(mydoubler)
print(mydoubler(11))


# ## <span style="color:#4361EE">Programación Funcional</span>
# 

# Esta sección es una adaptación de [geeksforgeeks](https://www.geeksforgeeks.org/functional-programming-in-python/#:~:text=Functional%20programming%20is%20a%20programming,is%20%E2%80%9Chow%20to%20solve%E2%80%9C.).

# ### <span style="color:#4CC9F0">Funciones puras</span>

# Las funciones puras tienen dos propiedades.
# 
# - Siempre produce la misma salida para los mismos argumentos. Por ejemplo, 3 + 7 siempre será 10 pase lo que pase.
# - No cambia ni modifica la variable de entrada.
# 
# La segunda propiedad también se conoce como inmutabilidad. El único resultado de la función pura es el valor que devuelve. Son deterministas. Los programas realizados mediante programación funcional son fáciles de depurar porque las funciones puras no tienen efectos secundarios ni E / S ocultas. Las funciones puras también facilitan la escritura de aplicaciones paralelas / concurrentes. Cuando el código está escrito en este estilo, un compilador inteligente puede hacer muchas cosas: puede paralelizar las instrucciones, esperar a evaluar los resultados cuando los necesite y memorizar los resultados, ya que los resultados nunca cambian mientras la entrada no cambie.
# 
# Revise el siguiente ejemplo. Recibe una lista de número y regresa una nueva lista con los valores elevado al cuadrado.

# In[9]:


# Ejemplo de una función pura

# Una función pura que no
# cambia la lista de entrada y
# devuelve la nueva lista

def pure_func(List):
    New_List = []
    for i in List:
        New_List.append(i**2)
    return New_List

# La función en acción
Original_List = [1, 2, 3, 4]
Modified_List = pure_func(Original_List)

print("Lista original:", Original_List)
print("Lista modifciada:", Modified_List)


# ### <span style="color:#4CC9F0">Recursión</span>

# En la programación funcional, no existe el concepto de bucle for o bucle while, sino que se utiliza la recursividad. La recursividad es un proceso en el que una función se llama a sí misma directa o indirectamente. En el programa recursivo, se proporciona la solución al caso base y la solución al problema mayor se expresa en términos de problemas menores. Puede surgir una pregunta ¿cuál es el caso base? El caso base puede considerarse como una condición que le dice al compilador o intérprete que salga de la función.
# 
# Ejemplo: consideremos un programa que encontrará la suma de todos los elementos de una lista sin usar ningún bucle for.

# In[10]:


# Ejemplo de recursión

# Función recursiva para encontrar
# suma de una lista

def Sum(L, i, n, count):

    # Caso base
    if n <= i:
        return count

    count += L[i]

    # Proceso recursivo
    count = Sum(L, i + 1, n, count)

    return count

# Ejemplo de uso
L = [1, 2, 3, 4, 5]
count = 0
n = len(L)
print(Sum(L, 0, n, count))


# ### <span style="color:#4CC9F0">Las funciones son de primera clase y pueden ser de orden superior</span>

# ####  Objetos de primera clase

# Los objetos de primera clase se manejan uniformemente en todo momento. Pueden almacenarse en estructuras de datos, pasarse como argumentos o usarse en estructuras de control. Se dice que un lenguaje de programación admite funciones de primera clase si trata las funciones como objetos de primera clase.

# #### Propiedades de las funciones de primera clase:

# - Una función es una instancia del tipo de objeto.
# - Puede almacenar la función en una variable.
# - Puede pasar la función como parámetro a otra función.
# - Puede devolver la función desde una función.
# - Puede almacenarlos en estructuras de datos como tablas hash, listas,…
# 
# Ejemplo:

# In[11]:


# Programa Python program para ilustrar
# funciones de orden mayor


def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    # almacena la función en una variable
    greeting = func("Hola, soy creada por una función pasada como argumento.")
    print(greeting)

greet(shout)
greet(whisper)


# ### <span style="color:#4CC9F0">Funciones integradas de orden superior</span>
# 

# Para facilitar mucho el procesamiento de objetos iterables como listas e iteradores, Python ha implementado algunas funciones de orden superior de uso común. Estas funciones devuelven un iterador que ahorra espacio. Algunas de las funciones integradas de orden superior son:
# 
# * *map()*: la función *map()* devuelve una lista de los resultados después de aplicar la función dada a cada elemento de un iterable dado (lista, tupla, etc.)
# * *filter()*: El método *filter()* filtra la secuencia dada con la ayuda de una función que prueba que cada elemento de la secuencia sea verdadero o no.
# 
# Veamos los siguientes dos ejemplos que ilustran *map()* y *filter()*.

# In[12]:


# Ejemplo del uso de map()

# Retorna el doble de n
def addition(n):
    return n + n

# doblamos todos los valores de una lista usando map
numbers = (1, 2, 3, 4)
results = map(addition, numbers)

#  Print no imprime los resultados
# porque se recibe un iterable
print(results)

# Asi recuperamos del iterable los valores e imprimimos
for result in results:
    print(result, end = " ")


# In[13]:


# Ejemplo de uso de filter()

# función que filtra las vocales en una lista
def fun(variable):

    letters = ['a', 'e', 'i', 'o', 'u']

    if (variable in letters):
        return True
    else:
        return False


# secuencia
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'i', 'r']

# uso de la función filter
filtered = filter(fun, sequence)

print('Las letras filtradas son:')

for s in filtered:
    print(s)


# ## <span style="color:#4361EE">Autores</span>

# 1. Alvaro Mauricio Montenegro Díaz, ammontenegrod@unal.edu.co
# 1. Daniel Mauricio Montenegro Reyes, dextronomo@gmail.com 

# ## <span style="color:#4361EE">Comentarios</span>
# 
