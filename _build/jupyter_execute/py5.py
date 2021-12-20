#!/usr/bin/env python
# coding: utf-8

# (2:py5)=

# # <span style="color:#F72585">Introducción a Clases en Python</span> 

# ## <span style="color:#4361EE">Introducción</span>
#  

# Python es un lenguaje de programación orientado a objetos.
# 
# **Todo** en Python es un objeto, con sus propiedades y métodos.

# ## <span style="color:#4361EE">Clases</span>
# 

# Podemos imaginarnos **una clase** como una plantilla o un plano para construir objetos.
# 
# Para crear una clase, usa el la palabra clave ```class:```
# 
# Supongamos, por ejemplo, que queremos crear una plataforma para recolectar toda la información personal que podamos de nuestros usuarios (nada parecido con la realidad) porque... sí.
# 
# Creemos una clase que no haga nada.

# In[1]:


class Usuario:
    pass


# La razón de ```pass``` es debido a que una clase necesita al menos una línea para poder existir.
# 

# :::{admonition} Consejo
# :class: tip
# 
# Para crear los nombres de las clases, comience con mayúsculas.
# :::

# Ok. Ahora creemos un usuario:

# In[2]:


u1=Usuario()
u2=Usuario()


# In[3]:


u1


# Como podemos ver, parece que estuvieramos llamando un método (o función), y en efecto es algo parecido
# 
# ```u1``` es una **instancia** de la clase Usuario.
# 
# También podemos llamar a ```u1``` un objeto.
# 
# Podemos adjuntar datos a este objeto, usamos la notación punto:

# In[4]:


#Adjuntando datos a el objeto u1 de la clase Usuario

u1.nombre="Aprendizaje"
u1.apellido="Profundo"
u2.edad =15

print(u1.nombre)
print(u1.apellido)
print(u2.edad)


# Los datos adjuntados a un objeto se les llaman **atributos**
# 

# :::{admonition} OJO
# :class: warning
# 
# Nombre y apellido no son variables existentes en el ambiente de trabajo.
# :::

# :::{admonition} Consejo
# :class: tip
# 
# Se recomienda usar minúsculas para los nombres de los campo (Tradición Pythonica).
# :::

# Es común diferenciar entre atributos de clase y atributos de instancia de clase. Por lo pronto nos referimos a los atributos de instancia de clase qu refieren a la información incluida en una instancia de clase.

# In[5]:


u1.nombre


# Una bonita consecuencia, es que podemos crear muchos objetos con campos del mismo nombre sin tener que definir una variable diferente para cada dato adjuntado del objeto.
# 
# Hagamos otro objeto:

# In[6]:


u2=Usuario()
u2.nombre="Francisco"
u2.apellido="Talavera"
u2.edad=34


# In[7]:


#edad de u2
u2.edad


# In[8]:


# u1 no tiene edad asginada
u1.edad


# Se estarán preguntando...
# 
# ### <span style="color:#4CC9F0">¿Para qué tomarnos la molestia si pudimos hacer todo un diccionario?</span>
# 
# La respuesta la encontraremos en características adicionales de las clases. Estas contienen:
# 
# -  Métodos 
# - Inicialización 

#  ## <span style="color:#4361EE">La función \_\_init\_\_()</span>
# 

# Una función dentro de una clase de llama **método**.
# 
# \_\_init\_\_ es el abreviado de **initialization** (inicialización).
# 
# También se le conoce como el **constructor**.
# 
# **Note los dos guiones bajos antes y despues de init**.

# In[ ]:


class Usuario:
    def __init__(self, nombre_completo, cumple):
        self.nombre = nombre_completo
        self.cumple = cumple

u3 = Usuario("Thomas Anderson", '19620311')

print(u3.nombre)
print(u3.cumple)


# ```{admonition} Nota
#  _self_ es el parámetro que referencia la instancia actual de la clase y se usa para acceder a los atributos de dicha clase. No tiene que llamarse self.
# ```

# In[ ]:


class Usuario:
    def __init__(mi_objeto, nombre_completo, cumple):
        mi_objeto.nombre = nombre_completo
        mi_objeto.cumple = cumple

u3 = Usuario("Thomas Anderson", '19620311')

print(u3.nombre)
print(u3.cumple)


# Agreguemos otra característica más.
# 
# Por ejemplo, extraer nombre y apellido:

# In[ ]:


class Usuario:
    def __init__(self, nombre_completo, cumple):
        self.nombre_c = nombre_completo
        self.cumple = cumple
        
        #Extraer partes
        piezas_nombre=nombre_completo.split(" ")
        self.nombre=piezas_nombre[0]
        self.apellido=piezas_nombre[-1]
        
u = Usuario("Thomas Anderson", '19620311')

print(u.nombre_c)
print(u.nombre)
print(u.apellido)
print(u.cumple)


# In[ ]:


class Usuario:
    def __init__(self, nombre_completo, cumple):
        self.nombre_c = nombre_completo
        self.cumple = cumple
        
        #Extraer partes
        piezas_nombre=nombre_completo.split(" ")
        self.nombre=piezas_nombre[0]
        self.apellido=piezas_nombre[-1]
        
Neo = Usuario("Thomas Anderson", '19620311')

print(Neo.nombre_c)
print(Neo.nombre)
print(Neo.apellido)
print(Neo.cumple)


# ### <span style="color:#4CC9F0">Documentación de una clase</span>

# Podemos documentar la clase de la siguiente manera:

# In[ ]:


class Usuario:
    """Un usuario de nuestra plataforma. Por ahora
    sólo recolectamos nombre y cumpleaños.
    Pero pronto tendremos mucho más que eso."""
    def __init__(self, nombre_completo, cumple):
        self.nombre_c = nombre_completo
        self.cumple = cumple
        
        #Extraer partes
        piezas_nombre=nombre_completo.split(" ")
        self.nombre=piezas_nombre[0]
        self.apellido=piezas_nombre[-1]
        
help(Usuario)


# ### <span style="color:#4CC9F0">Agregando métodos a una clase</span>
# 

# Es posible crear métodos propios a una clase.
# 
# Creemos por ejemplo un método que extraiga la edad de nuestro usuario.

# In[ ]:


import datetime

class Usuario:
    """Un usuario de nuestra plataforma. Por ahora
    sólo recolectamos nombre y cumpleaños.
    Pero pronto tendremos mucho más que eso."""
    def __init__(self, nombre_completo, cumple):
        self.nombre_c = nombre_completo
        self.cumple = cumple
        
        #Extraer partes
        piezas_nombre=nombre_completo.split(" ")
        self.nombre=piezas_nombre[0]
        self.apellido=piezas_nombre[-1]
        
    def edad(self):
        """Regresa la edad de nuestro usuario en años."""
        hoy=datetime.date.today()
        año=int(self.cumple[0:4])
        mes=int(self.cumple[4:6])
        dia=int(self.cumple[6:8])
        fecha_cumple=datetime.date(año,mes,dia)
        edad_dias=(hoy-fecha_cumple).days
        edad_años=edad_dias/365
        return int(edad_años)
    
Neo=Usuario("Thomas Anderson","19620311")

print("Neo tiene",Neo.edad(),"años")


# In[ ]:


help(Usuario)


# ### <span style="color:#4CC9F0">Imprimiendo contenidos de una clase por defecto</span>
# 

# Para establecer una forma de print por defecto en una clase, puede agregar el método reservado ```__str__```. Vamos a redefinir nuestra clase para incluirlo.
# 

# In[ ]:


import datetime

class Usuario:
    """Un usuario de nuestra plataforma. Por ahora
    sólo recolectamos nombre y cumpleaños.
    Pero pronto tendremos mucho más que eso."""
    def __init__(self, nombre_completo, cumple):
        self.nombre_c = nombre_completo
        self.cumple = cumple
        
        #Extraer partes
        piezas_nombre=nombre_completo.split(" ")
        self.nombre=piezas_nombre[0]
        self.apellido=piezas_nombre[-1]
        
    def edad(self):
        """Regresa la edad de nuestro usuario en años."""
        hoy=datetime.date.today()
        año=int(self.cumple[0:4])
        mes=int(self.cumple[4:6])
        dia=int(self.cumple[6:8])
        fecha_cumple=datetime.date(año,mes,dia)
        edad_dias=(hoy-fecha_cumple).days
        edad_años=edad_dias/365
        return int(edad_años)
     
    def __str__(self):
        return self.nombre_c + '  tiene ' + str(self.edad()) + ' años'


# In[ ]:


Neo=Usuario("Thomas Anderson","19620311")
print(Neo)


# ### <span style="color:#4CC9F0">Ejecución de una tarea por defecto en una instancia de clase: call</span>
# 

# Puede usar el método reservado ```__call__``` para ejecutar uan tarea por defecto cuando se llama a un objeto. 
# 
# Por ejemplo supongamos que deseamos ver cuantas veces ha sido llamado un objeto.
# 
# Agrandamos una vez más nuestra clase *Usuario*.

# In[ ]:


import datetime

class Usuario:
    """Un usuario de nuestra plataforma. Por ahora
    sólo recolectamos nombre y cumpleaños.
    Pero pronto tendremos mucho más que eso."""
    def __init__(self, nombre_completo, cumple):
        self.nombre_c = nombre_completo
        self.cumple = cumple
        
        self.llamadas = 0
        
        #Extraer partes
        piezas_nombre=nombre_completo.split(" ")
        self.nombre=piezas_nombre[0]
        self.apellido=piezas_nombre[-1]
        
    def edad(self):
        """Regresa la edad de nuestro usuario en años."""
        hoy=datetime.date.today()
        año=int(self.cumple[0:4])
        mes=int(self.cumple[4:6])
        dia=int(self.cumple[6:8])
        fecha_cumple=datetime.date(año,mes,dia)
        edad_dias=(hoy-fecha_cumple).days
        edad_años=edad_dias/365
        return int(edad_años)
     
    def __str__(self):
        return self.nombre_c + '  tiene ' + str(self.edad()) + ' años'
    
    def __call__(self):
        self.llamadas +=1
        return(self.llamadas)


# In[ ]:


Neo=Usuario("Thomas Anderson","19620311")
print(Neo)
print(Neo())
print(Neo())


# ## <span style="color:#4361EE">Referencias y copia de objetos</span>
Es importante que hagamos la diferencia entre referenciar un objeto y realmente copiarlo.

Vamos a crear un segundo objeto
# In[ ]:


Smith=Usuario("Agente Smith","20100515")
print(Smith)


# ahora una referencia a Neo

# In[ ]:


px = Neo
print(px)
print(Neo)


# Pero ahora observe lo que pasa si modifica *px*

# In[ ]:


px.cumple ='19500319'
print(Neo)
print(px)


# Esto ocurre porque en realidad px es una referencia al objeto Neo. Si desea una copia física puede por ejemplo usar la función *copy* del módulo estándar *copy*.

# In[ ]:


from copy import copy

px = copy(Neo)
Neo.cumple = "19600311"
print(px)
print(Neo)


# ### <span style="color:#4CC9F0">Eliminación de objetos: del</span>

# Se usa para eliminar un objeto. Por ejemplo:

# In[ ]:


del px
print(px)


# ## <span style="color:#4361EE">Atributos Intrínsecos de clases y objetos</span>
# 

# Cada clase y objeto de Python tiene una conjunto de atributos intrínsecos que pueden ser llamados.
# 
# Los atributos intrínsecos de clase son:
# 
# +  ```__name__```: nombre de la clase
# +  ```__module__```: módulo al cual pertenece la clase
# +  ```__bases__```: clases base de ésta clase
# +  ```__dict__```: diccionario conteniendo un conjunto *clave/valor* con todos los atributos de la clase incluidos los métodos.
# 
# Los atributos intrínsecos de los objetos son:
# 
# + ```__class__```: nombre de la clase del objeto 
# + ```__dict__```: diccionario conteniendo un conjunto *clave/valor* con todos los atributos
# 
# 

# In[ ]:


print('Atributos de clase\n')
print('Nombre de la clase: ',Usuario.__name__)
print('\n Módulo: ', Usuario.__module__)
print('\n Documentación:\n',Usuario.__doc__)
print('\nDiccionario de la clase: \n',Usuario.__dict__)
print('\nClases Base: ',Usuario.__bases__)
print('\nAtributos del objeto Neo\n')
print('Clase: ',Neo.__class__)
print('\n Diccionario: ', Neo.__dict__)


# ## <span style="color:#4361EE">Herencia de clases</span>
# 

# Una de las grandes ventajas de usar clases en programación es poder generar clases más especializadas a partir de una o más clases base.
# 
# Esto característica permite re-utilizar código y también permite escribir un código más limpio y legible.
# 
# Supongamos que a la clase Usuario le queremos dar un tipo de publicidad en específico.
# 
# Creemos entonces una clase que hable sobre los gustos del usuario, pero referenciando a la clase ya creada.

# In[ ]:


class Lector(Usuario):
    pass


# In[ ]:


help(Lector)


# In[ ]:


l=Lector("Daniel Montenegro","19901026")
print(l.nombre_c)
print(l.nombre)
print(l.edad())
print(l)
print(l())


# Al intentar colocar un constructor sobre la clase heredada, se perderá la función constructora heredada de Usuario:

# In[ ]:


class Lector(Usuario):
    def __init__(self, nombre_completo, cumple):
        self.nombre_c = nombre_completo
        self.cumple = cumple
        # Agregar cositas


# In[ ]:


l=Lector("Daniel Montenegro","19901026")
print(l.nombre_c)
print(l.edad())


# ### <span style="color:#4CC9F0">Referencia a la clase base: super()</span>
# 

# Dado que al heredar una clase de otra, estamos pensando en conservar la funcionalidad de la clase base, es importante poder usar el constructor de la clase base junto con el constructor extendido en la clase heredada. Para hacer esta característica posible se utiliza  `super()` como se muestra a continuación. *super()* es un enlace o referencia a la clase base. Entonces, si deseamos usar el constructor de la clase base se puede escribir 
# 
# super().\_\_init\_\_(...)
# 
# 
# Veamos el uso de *super()* en nuestra clase Lector, la cual heredamos de la clase Usuario.

# In[ ]:


class Lector(Usuario):
    def __init__(self, nombre_completo, cumple, gustos):
        super().__init__(nombre_completo, cumple)
        self.gustos=gustos
        # Agregar otras cosas


# In[ ]:


l=Lector("Daniel Montenegro","19901026","Jack Kerouac")
print(l.nombre_c)
print(l.edad())
print(l.gustos)
print(l)


# Finalmente, agreguemos un método a la clase Lector para extender su funcionalidad:

# In[ ]:


class Lector(Usuario):
    def __init__(self, nombre_completo, cumple, gustos):
        super().__init__(nombre_completo, cumple)
        self.gustos=gustos
        año=int(self.cumple[0:4])
        mes=int(self.cumple[4:6])
        dia=int(self.cumple[6:8])
        self.fecha_cumple=datetime.date(año,mes,dia)
        
    def info(self):
        print(" El Usuario",self.nombre_c,", nacido en",self.fecha_cumple, ", tiene",self.edad(),"años", "y le gustan las obras de",self.gustos)


# In[ ]:


l=Lector("Daniel Montenegro","19901026","Jack Kerouac")
l.info()


# ## <span style="color:#4361EE">Autores</span>
# 
# 1. Alvaro Mauricio Montenegro Díaz, ammontenegrod@unal.edu.co
# 2. Daniel Mauricio Montenegro Reyes, dextronomo@gmail.com 
# 

# ## <span style="color:#4361EE">Comentarios</span>
