#!/usr/bin/env python
# coding: utf-8

# (2:py4)=
# 
# # <span style="color:#F72585">Inspección, Instalación y Carga de Módulos y Paquetes</span>
# 
# Dependiendo del ambiente de trabajo usado, tenemos diferente cantidad de **paquetes** instalados.
# 
# Hay una **forma** de ver qué paquetes existen en el ambiente actual sin salir del Notebook.
# 
# Basta con colocar ```!<comando>``` en una celda de código.
# 
# Dicho esto, ¿Qué es mejor, hacer todo desde el Prompt o el Notebook?
# 
# *La elección si depende del gusto :)*
# 
# ### <span style="color:#4CC9F0">Ejemplo</span>
# 
# Verifiquemos que versión de Python estamos usando, qué ambientes disponibles existen, cuál es el activo y qué paquetes están instalados, todo esto **sin salir del Notebook**.

# In[1]:


# Recuerda que # es para usar comentarios
# Versión Actual de Python siendo usada
get_ipython().system('python --version')
# Función print para dar un salto de línea
print(" ")
# Lista de Ambientes Disponibles y Activo en el Notebook
get_ipython().system('conda env list')


# In[2]:


get_ipython().system('conda list')


# Dentro de cada uno de estos paquetes se encuentran **modulos**, que juntos forman la librería de módulos disponibles en el ambiente de trabajo.
# ## <span style="color:#4361EE">¿Qué es un módulo?</span>
# 
# 
# Un módulo es un archivo que tiene extensión *.py*, es decir, es un archivo de texto que tiene adentro código de python que se puede ejecutar. Un módulo puede definir funciones, clases y variables.
# 
# Cabe resaltar lo siguiente: **Python es un lenguaje de programación orientado a objetos**.
# 
# Para términos de visualización, imagínese una caja que tiene muchas cajas por dentro y dentro de cada caja existen herramientas de trabajo distintas.
# 
# ### <span style="color:#4CC9F0">Ejemplo</span>
# 
# Mi maleta. Mi maleta tiene dentro lo siguiente:
# 
# - Una cartuchera.
# - Un computador.
# - Un cuaderno.
# 
# Los roles serían los siguientes:
# 
# - Maleta     $\rightarrow$ Paquete
# - Cartuchera $\rightarrow$ Módulo
# - Cuaderno   $\rightarrow$ Módulo
# 
# Entonces, si queremos usar la cartuchera, debemos primero abrir la maleta y tomarla.
# 
# **O sea, del paquete, vamos a usar un módulo**.
# 
# Dentro de la cartuchera tengo marcadores, lápices, y borrador.
# 
# Estos toman el rol de **atributos**, objetos que hacen tareas específicas.
# 
# Por tanto, si quiero usar un borrador, debería hacer lo siguiente
# 
# Abrir maleta $\rightarrow$ Tomar cartuchera $\rightarrow$ Abrir Cartuchera $\rightarrow$ Tomar Borrador
# 
# En Python, estas acciones se pueden **traducir** a lo siguiente:
# 
# ```import Maleta```
# 
# ```Maleta.Cartuchera.Borrador()```
# 
# Para saber qué módulos están disponibles en el ambiente de trabajo, basta con usar el siguiente comando:

# In[3]:


help("modules")


# Parece que es una lista bastante larga...
# 
# Veamos alguna documentación de alguno de los módulos y sus atributos.
# 
# Por ejemplo random.

# In[ ]:


#help("random") # Muestra toda la documentación

import random

#?random # Muestra una pequeña documentación


# Para acceder a los atributos del módulo, basta colocar ```dir(modulo)```

# In[ ]:


dir(random)


# Vaya que la lista sigue siendo larga...
# 
# Sigamos metiendo dentro de cada cosa (algún día llegaremos al fin...no?)

# In[ ]:


get_ipython().run_line_magic('pinfo', 'random.random')


# **¡Bingo!** Al fin algo que podemos usar:

# In[ ]:


x = random.random()
print("Número aleatorio en [0,1]: ",x)


# In[ ]:


get_ipython().run_line_magic('pinfo', 'random.randint')


# In[ ]:


y=random.randint(3,6)
print("Número entero aleatorio entre 3 y 6: ",y)


# # <span style="color:#4361EE">Alias para módulos</span>
# 
# Otra propiedad genial de Python es su capacidad para reducir la cantidad de código escrito usando unos secretos milenarios: aliases.
# 
# Por ejemplo, si me llamo Daniel, mi **alias** puede ser Dani.
# 
# Entonces, cada vez que me digan Dani, yo miraré en respuesta.
# 
# Traducir a Python luce así:
# 
# ```import modulo as alias```
# 
# ### <span style="color:#4CC9F0">Ejemplo</span>

# In[ ]:


import math as m

# Una vez nombrado el alias, siempre se debe referir a ese alias y no al nombre principal

#dir(math) genera error
dir(m)


# ## <span style="color:#4361EE">Aplicación</span>
# 
# 
# Una pequeña aplicación de Matemáticas:
# 
# **Área de una circunferencia de radio r:**
# 
# $A = \pi r²$

# In[ ]:


# Aplicación: Área de un círculo de radio 10 cm 

r = 10;          # Declarar el radio
z = m.pi*(r**2)  # Escribir la fórmula matemática
print("El Área del círculo es: ",z,"cm²")


# Como pueden observar, los módulos son el **alma de Python**.
# 
# ## <span style="color:#4361EE">Tareas</span>
# - Conocer los 10 módulos de Python más usados.
# - Hacer un ejercicio práctico con cada módulo investigado.
# - Investigar si es posible crear un módulo de Python. En caso afirmativo, crear uno simple.
# - Explicar la lógica subyacente de la siguiente línea:

# In[ ]:


# You Must Reset Kernel 0,0

from math import pi

A = pi*r**2

print(A)


# In[ ]:


math.pi


# # <span style="color:#F72585">Bonus: Fractales</span>
# Usando un módulo llamado ```turtle``` podemos crear un arbolito bonito.

# :::{admonition} Importante
# :class: tip
# Por favor, para poder visualizar la salida del siguiente código abra el cuaderno en Binder
# :::

# In[1]:


import turtle

def tree(length,n):
    if length < (length/n):
        return
    turtle.forward(length)
    turtle.left(45)
    tree(length * 0.5,length/n)
    turtle.left(20)
    tree(length * 0.5,length/n)
    turtle.right(75)
    tree(length * 0.5,length/n)
    turtle.right(20)
    tree(length * 0.5,length/n)
    turtle.left(30)
    turtle.backward(length)
    return

turtle.left(90)
turtle.backward(30)
tree(200,4)


# Y también formas que tienen forma de pedazos de copitos de nieve (Koch Curve):

# In[ ]:


from turtle import *

def Recursive_Koch(length, depth):
    if depth == 0:
        forward(length)
    else:
        Recursive_Koch(length, depth-1)
        right(60)
        Recursive_Koch(length, depth-1)
        left(120)
        #Recursive_Koch(length, depth-1)
        Recursive_Koch(length, depth-1)
        right(60)
        Recursive_Koch(length, depth-1)
        
# ----------
Recursive_Koch(3, 6)


# ## <span style="color:#4361EE">Autores</span>
# 

# 1. Alvaro Mauricio Montenegro Díaz, ammontenegrod@unal.edu.co
# 1. Daniel Mauricio Montenegro Reyes, dextronomo@gmail.com 

# ## <span style="color:#4361EE">Bibliografía </span>
# 

# ## <span style="color:#4361EE">Comentarios</span>
# 
