#!/usr/bin/env python
# coding: utf-8

# (2:py6)=

# 
# # <span style="color:#F72585">Introducción a Decoradores (Decorators) en Python</span> 
# 

# ## <span style="color:#4361EE">Introducción</span>

# Los decorators constituyen un patrón de programación que se utiliza cuando es necesario incluir un comportamiento adicional a objetos específicos. Una forma de agregar tal comportamiento adicional es decorar los objetos creados con tipos que aportan la funcionalidad extra.
# 
# Estos decoradores envuelven el objeto original pero presentan exactamente la misma interfaz para
# el usuario de ese objeto. Por lo tanto, el patrón de diseño del decorador extiende el comportamiento
# de un objeto sin utilizar subclassing. La decoración de un objeto es transparente a los clientes de los decoradores.
# 
# En Python, los decoradores son funciones que toman otra función (u otro objeto invocable
# como un método) y devuelve una tercera función que representa el 
# comportamiento decorado.

#  ## <span style="color:#4361EE">Decoradores</span>

# ### <span style="color:#4CC9F0">Definición de un decorador</span>

# Para definir un decorador, debe definir un objeto invocable, como una función que
# toma otra función como parámetro y devuelve una nueva función. A continuación se da un ejemplo de la definición de una función decoradora de registro (logger) muy simple
# 

# In[1]:


def logger(func):
    def inner():
        print('llamando ', func.__name__)
        func()
        print('llamada', func.__name__)
        
    return inner


# Observe que la función *logger* retorna una función, *inner*, la cual a su vez llamará a una tercera función *func*.

# ### <span style="color:#4CC9F0">Usando el decorador</span>

# Veamos ahora el efecto del decorador en acción. Usaremos la función *target* como la función que vamos a decorar.

# In[2]:


def target(): 
    print('Dentro de la función target')


# In[3]:


t1 = logger(target)

t1()


# ### <span style="color:#4CC9F0">Suavizando el trabajo</span>

# Python proporciona algo de azúcar sintáctico que permite decorar directamente la función desde su definición. Este es el uso más practico de los decoradores.

# In[4]:


@logger
def target():
    print('Dentro de la función target')

target()


# ## <span style="color:#4361EE">Funciones con parámetros</span>

# En este caso la función decoradora debe incluir los parámetros. Veamos el ejemplo.

# In[5]:


def logger(func):
    def inner(x, y):
        print('llamando ', func.__name__, 'con ',x , 'y',y)
        func(x, y)
        print('regresando de ',func.__name__)
    return inner


# In[6]:


@logger
def mi_funcion(x, y):
    print('x + y = ', x+y)

mi_funcion(5,6)


# ## <span style="color:#4361EE">Decoradores apilados (stacked decorators)</span>

# Es posible apilar decoradores. Veamos el ejemplo. Vamos a imprimir un texto. Los decoradores agregaran negrilla (bold) e itálica (italic) al texto impreso.

# In[7]:


# decoradores
def make_bold(fn):
    def makebold_wrapper():
        return "<b>" + fn() + "</b>"
    return makebold_wrapper

def make_italic(fn):
    def makeitalic_wrapper():
        return "<i>" + fn() + "</i>"
    return makeitalic_wrapper

# aplica los decoradores

@make_bold
@make_italic
def hello():
    return 'hola mundo'

print(hello())


# ## <span style="color:#4361EE">Decoradores para métodos de clases</span>

# En este caso,  es importante recordar que los métodos toman el 
# parámetro especial *self* como el primer parámetro que se utiliza para hacer referencia al objeto del que
# se está aplicando el método. Por lo tanto, es necesario que el decorador tome este parámetro en cuenta; es decir, la función envuelta interna debe tomar al menos un parámetro que representa a *self*. Veamos el ejemplo.

# In[8]:


def pretty_print(method):
    def method_wrapper(self):
        return "<p>{0}</p>".format(method(self))
    return method_wrapper


# In[9]:


class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def print_self(self):
        print('Persona - ', self.nombre, ', ', self.edad)
        
    @pretty_print
    def get_nombre_completo(self):
        return self.nombre + " " + self.apellido


# In[10]:


print('Comenzamos')
p = Persona('Alvaro', 'Montenegro', 61)
p.print_self()
print(p.get_nombre_completo())
print('Hecho!')


# ### <span style="color:#4CC9F0">Decoradores para métodos de clases con parámetros</span>

# Aquí combinamos lo hecho en las dos subsecciones anteriores. Veamos.

# In[11]:


def trace(method): 
    def method_wrapper(self, x, y):
        print('Llamando', method.__name__, 'con', x, y)
        method(self, x, y)
        print('Se llamó', method.__name__, 'con', x, y)
    return method_wrapper


# In[12]:


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @trace
    def move_to(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point - ' + str(self.x) + ',' + str(self.y)


# In[13]:


p = Point(1, 1)
print(p)
p.move_to(5,5)
print(p)


# ## <span style="color:#4361EE">Autores</span>

# 1. Alvaro Mauricio Montenegro Díaz, ammontenegrod@unal.edu.co
# 1. Daniel Mauricio Montenegro Reyes, dextronomo@gmail.com 

# ## <span style="color:#4361EE">Comentarios</span>
