#!/usr/bin/env python
# coding: utf-8

# (2:py3)=
# 

# # <span style="color:#F72585">Listas, Tuplas y Diccionarios en Python</span>

# ## <span style="color:#4361EE">Introducción</span>

# Este es un cuaderno introductorio a las colecciones como tuplas, listas y diccionarios en Python. Para una introducción más extensa, ir [aquí](https://www.w3schools.com/python/). Empezamos con el concepto de Iterables e iteradores.

# ## <span style="color:#4361EE">Iterables e iteradores</span>

# Hay dos protocolos que es muy probable tenga que utilizar, o posiblemente necesite
# implementar en algún momento; estos son el protocolo Iterable y el protocolo Iterador. 
# Estos dos protocolos están estrechamente relacionados y son muy utilizados y respaldados por un
# gran cantidad de tipos.
# 
# Una de las razones por las que los iteradores y los iterables son importados es que se pueden usar con
# sentencias *for* en Python; esto hace  que sea muy fácil integrar un iterable en el código
# que necesita procesar una secuencia de valores a su vez

# ### <span style="color:#4CC9F0">Iterables</span>

# El protocolo Iterable es utilizado por tipos donde es posible procesar su contenido.
# uno a la vez.
# 
# Un Iterable es un objeto que proporcionará un Iterador que puede ser
# utilizado para realizar este procesamiento.
# 
# Como tal, el iterable no es el iterador en sí mismo; sino el proveedor del iterador.
# 
# Hay muchos tipos iterables en Python, incluidas listas, conjuntos, diccionarios,
# tuplas, etc. Todos estos son contenedores iterables que proporcionarán un iterador.
# 
# Es posible además construir clases que generen iteradores personalizados. De momento trabajaremos con los tipos que ya lo soportan, mencionados arriba.

# ### <span style="color:#4CC9F0">Iteradores</span> 

# Un iterador es un objeto que devolverá una secuencia de valores. 
# 
# Los iteradores pueden ser finitos de longitud o infinito (aunque la mayoría de  iteradores orientados a contenedores proporcionan un conjunto fijo de valores.
# 

# ### <span style="color:#4CC9F0">Generadores</span>

# Un generador es una función especial que se puede utilizar para generar una secuencia de
# valores que se van a iterar sobre  demanda (es decir, cuando se necesitan los valores) en lugar de
# que producido todo por adelantado.
# 
# Lo único que hace que una función  generadora trabaje como generador es el uso de
# palabra clave *yield*.

# ### <span style="color:#4CC9F0">Ejemplo de una función generadora</span>

# In[1]:


def gen_numbers():
    yield 1
    yield 2
    yield 3


# Esta es una función generadora, ya que tiene al menos una declaración *yield* (de hecho, tiene
# Tres). 
# 
# Cada vez que se llama a la función *gen_numbers ()* dentro de una instrucción *for*
# devolverá uno de los valores asociados con una declaración *yield*; en este caso el
# valor 1, luego el valor 2 y finalmente el valor 3 antes de que regrese (termine). 
# 
# Ahora construimos una ciclo *for* que va llamando los números a la medida que los necesita. Observe que la variable *i* en este ejemplos es un iterador entregado por la función *gen_numbers()*.

# In[2]:


for i in gen_numbers():
    print(i)


# Para enteder un poco mejor como se ejecuta *yield* discuta en clase el siguiente fragmento (snippet) de código.

# In[3]:


def gen_numbers2():
    print('Start')
    yield 1
    print('Continue')
    yield 2
    print('Final')
    yield 3
    print('End')

for i in gen_numbers2():
    print(i)


# ### <span style="color:#4CC9F0">Creación de una clase iterable</span> 

# Más adelante veremos clases a plenitud. Aquí introducimos una clase muy sencilla para mostrar como crear un iterable personalizado.

# In[4]:


class Evens(object):
    def __init__(self, limit):
        self.limit = limit
        self.val = 0
    
    # Hace esta clase iterable
    def __iter__(self):
        return self
    
    # Hace esta clase un iterador
    def __next__(self):
        if self.val > self.limit:
            raise StopIteration
        else:
            return_val = self.val
            self.val += 2
            return return_val


# 
# Solamente vamos a resaltar unas pocas cosas de esta clase *Events*
# 
# + El método  \_\_iter__()  retorna *self*; este es un patrón muy común y asume que la clase también implementa el protocolo iterador.
# + El método  \_\_next__() retorna el siguiente valor en la secuencia o dispara una excepción con *StopIteration* para indicar que no hay más valores disponibles.
# 
# 
# El protocolo implica que cuando Python encuentra la definición de la función \_\_iter__() construye la maquinaria para que la clase sea un iterable. De la misma forma, cuando encuentra la función \_\_next__() construye la maquinaria para que la clase entregue un iterador.
# 
# 
# Veamos en acción *Evens*. Discuta en la clase.

# In[5]:


print('¡Empezamos')
for i in Evens(6):
    print(i,end=', ')
print('\nHecho!')


# # <span style="color:#F72585">Colecciones</span>

# Una colección es un contenedor de objetos del mismo tipo. Por defecto en Python existen cuatro tipos de contenedores:
# 
# - **Tuplas (tuple).** Esta es una colección de objetos que están ordenados y son inmutables (no pueden modificarse). Las tuplas admiten elementos repetidos y sus miembros son indexados.
# 
# - **Listas (list).** Son colecciones de objetos que están ordenado y son mutables, es decir, sus contenidos pueden ser modificados. Los elementos son indexados y permite duplicados.
# 
# - **Conjuntos (set).** Son contenedores de datos que no son ordenados ni indexados. Son mutables, pero no admiten duplicados.
# 
# - **Diccionarios (dictionary)** Son contenedores no ordenados, que son indexados mediante una clave, la cual referencia a un valor. El valor es retornado cuando se le solicita con la clave. No se admiten claves repetidas, pero si valores repetidos.
# 
# Recuerde que todo en Python es realmente un tipo de objeto.

# # <span style="color:#F72585">Tuplas</span>
# 

# Las tuplas se crean y se reconocen porque los elementos se escriben entre paréntesis circulares: '()'. Por ejemplo tupla1 en la siguiente línea define una tupla.

# In[6]:


tupla1 = (1,3,5,7)


# Cada elemento de la tupla está indexado. Por ejemplo, discuta el siguiente snippet de código.

# In[7]:


print ('Acceso a la tupla con iterator')
for i in tupla1:
    print(i)

print('Acceso al tupla con índices')
for i in range(len(tupla1)):
    print(i, tupla1[i] )


# ## <span style="color:#4361EE">Constructor de tuplas: tuple(iterable)</span>

# Una tupla puede crearse a partir de cualquier objeto iterable. Por ejemplo:

# In[8]:


lista1 = [1,2,3]
tupla2 = tuple(lista1)
print(tupla2)


# Observe como los valores de la lista pueden modificarse pero no los de la tupla:

# In[9]:


lista1[0] = 5
print(lista1)


# In[10]:


tupla2[0] = 5
print(tupla2)


# ## <span style="color:#4361EE">Uso de índices con tuplas</span>

# Observe las siguientes salidas:

# In[ ]:


print('tupla1:\t',tupla1)
print('tupla1[:3]:\t', tupla1[:3])
print('tupla1[1:]:\t', tupla1[1:])
print('tupla1[0:1]:\t', tupla1[0:1])
print('tupla1[1:-1]:\t', tupla1[1:-1])
print('tupla1[:-1]:\t', tupla1[:-1])
print('tupla1[:]:\t', tupla1[:])
print('tupla1[::2]:\t', tupla1[::2])


# De especial atención son las tres últimas líneas. El valor -1 se usa para indicar el final del objeto.
# 
# La ausencia de valores indica se toma desde el extremo (izquierdo o derecho) del objeto indexable. 
# 
# El tercer índice, introducido en Python, se utiliza como valor de salto al recuperar los elementos de la tupla. La última línea del ejemplo indica tomar cada dos posiciones. Como inicia en cero (0) tomas la posiciones 0 y 2.

# ```{admonition} Nota
# Las tuplas pueden contener **diferentes tipos de dato**.
# ```

# Por ejemplo en el siguiente fragmento *tup2* es una tupla que contiene un entero, un string, un tupla y un float.

# In[ ]:


tup2 = (1,"John", tupla1, True, -23.1)

for i in tup2:
    print(i)


# # <span style="color:#F72585">Listas</span>

# Las listas son contenedores mutables y ordenados de objetos. Las listas se distinguen porque sus elementos están encerrados entre paréntesis cuadrados. Por ejemplo:

# In[ ]:


lista1 = ['Alvaro', 'Daniel', 'Pilar', 'Beatriz']

for i in lista1:
    print(i, end=' ')
print('')


# Una lista puede contener objetos muy complejos. Por ejemplo observe detenidamente la siguiente construcción y discútala en la clase.

# In[ ]:


t1 = (1, 'Oleg', 24.5)
l1 = ['Maria', 'Bonita']
l2 = [t1, l1]
t2 = (l2,'manzana')

print('t1=', t1)
print('l1=', l1)
print('l2=', l2)
print('t2=', t2)


# ## <span style="color:#4361EE">Acceso a los elementos de una lista</span>

# Vamos a acceder a los elementos individuales de las listas y tuplas creadas arriba.

# In[ ]:


for i in t1:
    print(i)
print('\n')

for i in l1:
    print(i) 
print('\n')

for i in l2:
    print(i)
print('\n')

for i in t2:
    print(i)


# Ahora accedamos al interior de las estructuras complejas.

# In[ ]:


print(t2[0])
print(t2[1])
print('\n')

print(t2[0][0])
print(t2[0][1])
print('\n')

print(t2[0][0][0])
print(t2[0][0][1])
print(t2[0][0][2])
print('\n')

print(t2[0][1][0])
print(t2[0][1][1])
print(t2[0][0][2])
print('\n')


# Por favor asegúrese de entender completamente la lógica del anterior ejemplo.

# ### <span style="color:#4CC9F0">Constructor de lista</span>

# #### list(iterable)
# 
# Por ejemplo

# In[ ]:


vocalTupla = ('a', 'e','i','o','u')
vocalLista = list(vocalTupla )

print(vocalTupla)
print(vocalLista)


# ### <span style="color:#4CC9F0">Adicionar elementos a una lista</span>

# #### lista.append(objeto)
# 
# Veamos el siguiente ejemplo

# In[ ]:


alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
print( 'alfabeto es un objeto string: ',type(alfabeto))


# Vamos a crear una lista vacía y la vamos a llenar con cada uno de los elementos de *alpfabeto*

# In[ ]:


alfaL = []

for i in alfabeto:
    alfaL.append(i)

print(alfaL)


# ### <span style="color:#4CC9F0">Concatenar dos listas</span>

# In[ ]:


N = len(alfaL)

numL = []

for i in range(N):
    numL.append(i)

print('alfaL = ',alfaL) 
print('\n')
print('numL = ',numL)
print('\n')

alfanumL = alfaL + numL
alfanumLL = [alfaL, numL]

print('alfanumL = ',alfanumL) 
print('\n')
print('alfanumLL = ',alfanumLL)


# In[ ]:


# Acceso a los elementos de la lista alfanumLL

for i in range(N):
    print(alfanumLL[0][i],alfanumLL[1][i] )


# ### <span style="color:#4CC9F0">Eliminar elementos de una lista</span>
# 

# #### lista.remove(objeto)

# In[ ]:


alfaL.remove('c')
print(alfaL)


# ## <span style="color:#4361EE">Métodos para manipulación de listas</span>

# |Method| Description|
# |---|---|
# |append()| Agrega un elemento al final de la lista|
# |clear()| Remueve todo los elementos de la lista|
# |copy()| Regresa una copia de la lista|
# |count()| Regresa el número de elementos con el valor especificado|
# |extend()| Agrega elementos de una lista (o cualquier iterable) al final de esta lista|
# |index()|Regresa el índice del primer elemento con el valor especificado|
# |insert()|  Addiciona un elemento en la posición especificada|
# |pop()| Remueve un elemento en la posición especificada y puede retornarlo si se hce una asignación|
# |remove()| Remueve el item con este valor específico|
# |reverse()| Invierte el orden de la lista|
# |sort() | Ordena la lista|
# 
# 
# Por favor pruebe cada uno de estos métodos. Veamos unos pocos ejemplos.

# In[ ]:


print(alfaL.index('d'))

alfaL.insert(2,'c')
print(alfaL)


# In[ ]:


alfanumLL.reverse()
print(alfanumLL)


# # <span style="color:#F72585">Diccionarios</span>

# Los diccionarios se distinguen por dos conceptos claves: están encapsulado en {} y poseen el concepto de llave e ítem.
# 
# :::{admonition} Consideraciones importantes:
# :class: warning
# En **contraste con las listas**, los elementos del diccionario no se acceden vía índices, sino vía llaves (**keys**) que se definen.
# :::
# 
# 
# Miremos el siguiente ejemplo:

# In[ ]:


Rios = {
    'Leticia' : 'Amazonas',
    'Montería': 'Sinu',
    'Bogotá'  : 'Bogotá',
    'San Gil': 'Fonce',
    'Honda'  : 'Magladena'
}

print(Rios)


# Note lo que ocurre cuando intentamos acceder por medio de índices (posiciones):

# In[ ]:


print(Rios[0])


# In[ ]:


print(Rios['Montería'])


# También es posible crear un diccionario usando la función por defecto (built-in) `dict()`, usando una lista de tuplas:

# In[ ]:


my_dic=dict([
             ('Colores', ['Negro','Rojo','Azul']),
             ('Animales', 'Gato'),
             ('Calzado', ['Botas','Botines','Deportivos','Sanadalias'])
            ])

print(my_dic)


# Veamos el tipo de dato que es un diccionario.

# In[ ]:


print(type(my_dic))


# Veamos por ejemplo, los ítems que pertenecen a la llave **Colores**

# In[ ]:


print(my_dic['Colores'])


# Una vez ingresado a los ítem del diccionario, en caso de ser listas, podemos acceder a sus elementos tal cual lo hacemos con las listas (por sus índices)

# In[ ]:


print(my_dic['Colores'][1])


# In[ ]:


print('Ví pasar un',my_dic['Animales'],'con',my_dic['Calzado'][0],'de color',my_dic['Colores'][0])


# ```{admonition} Nota
# Si las llaves son strings sencillas (sin espacios), también es posible definir un diccionario de la siguiente manera:
# ```

# In[ ]:


my_dic=dict(
             Colores = ['Negro','Rojo','Azul'],
             Animales= 'Gato',
             Calzado =['Botas','Botines','Deportivos','Sanadalias']
            )

print(my_dic)


# Claro está, si se intenta acceder a una llave incorrecta, obtendremos el siguiente error:

# In[ ]:


print(my_dic['Valor'])


# ## <span style="color:#4361EE">Manejo de diccionarios:</span>
# 

# Podemos agregar, modificar y eliminar valores de un diccionario:

# ### <span style="color:#4CC9F0">Agregar valores:</span> 
# 

# In[ ]:


my_dic['Valor']=['20','50','12']
print(my_dic)


# ### <span style="color:#4CC9F0">Modificar valores:</span> 
# 

# In[ ]:


my_dic['Colores']='Negro'
print(my_dic)


# ### <span style="color:#4CC9F0">Eliminar valores:</span> 
# 

# In[ ]:


del my_dic['Valor']
print(my_dic)


# La razón por la cuál no es permitido acceder a los ítems de los diccionarios con índices, es que ellos mismos pueden ser las llaves:

# In[ ]:


d = {0: 'Coco', 1: 'Urban_Sound8k', 2: 'Mnist', 3: 'CheXpert'}
print(d)


# In[ ]:


d[0]


# Puede ser confuso al principio, confundir estas llaves con índices. Incluso se podría pensar en tomar rebanadas de él sin éxito o agregar valores como se hace en las listas:

# In[ ]:


d[0:2]


# ###Ejercicio:
# 
# Investigue que significa unhashable. Busque la función `hash()` y úsela en este contexto.

# In[ ]:


d.append('Yolo')


# ## <span style="color:#4361EE">Propiedades de los diccionarios </span>
# 

# ### <span style="color:#4CC9F0">Dinámicos:</span> 
#   

# Este concepto es muy importante, pues resalta la capacidad de un diccionario en incrementar su tamaño sin generar error:

# In[ ]:


#Generar diccionario vacío
persona = {}
print(type(persona))

# Agregar llaves y sus definiciones (items)
persona['Nombre'] = 'Gengis'
persona['Apellido'] = 'Khan'
persona['Edad'] = 23
persona['Esposa'] = ['Börte Qatun','Yesugen','Qulan Qatun','Möge Qatun','Juerbiesu','Ibaqa Beki']
persona['Hijos'] = 'En estudio'
persona['Mascotas'] = {'Perro': 'Wahadi', 'Gato': 'Gotze','Leon':'Pichirilo'}

print(persona)
print('Hijos de',persona['Nombre'],':',persona['Hijos'])


# ```{admonition} Nota
# Del ejemplo anterior se puede observar que los diccionarios pueden contener diccionarios en su interior:
# ```

# In[ ]:


print(persona['Mascotas'])


# In[ ]:


print(persona['Mascotas']['Perro'])


# ### <span style="color:#4CC9F0">Llaves:</span> 

# No hay restricciones en la forma de definir las llaves:

# In[ ]:


foo = {42: 'aaa', 2.78: 'bbb', False: 'cc'}


# In[ ]:


foo[False]


# In[ ]:


d = {int: 1, float: 2, bool: 3}

d[int]


# Sin embargo, las llaves son únicas y no se pueden repetir (com un diccionario clásico al que estamos acostumbrados):

# In[ ]:


foo = {42: 'aaa', 2.78: 'bbb', False: 'cc',False:'dodo'}
foo


# #### Ejercicio

# Defina un diccionario de al menos 4 llaves de tal manera que esas llaves sean tuplas. Acceda a cada elemento. ¿Puede hacer lo mismo para una llave que sea definida como lista o diccionario?

# ## <span style="color:#4361EE">Operadores </span>

# Es posible utilizar algunos operadores sobre los diccionarios para verificar su estado (por ejemplo, si están o no están disponibles sin generar errores):

# In[ ]:


'Animales' in my_dic


# In[ ]:


'Colores' not in my_dic


# También podemos usar lógica aristotélica (tablas de verdad) para chequear cosas sin tener errores:

# In[ ]:


my_dic['Valor']


# In[ ]:


'Valor' in my_dic and my_dic['Valor']


# ### <span style="color:#4CC9F0">len() sobre diccionarios</span> 
# 

# In[ ]:


print(my_dic)

print("\nEl diccionario tiene",len(my_dic),'llaves')


# ## <span style="color:#4361EE">Métodos</span>
# 

# ### <span style="color:#4CC9F0">d.clear()</span>

# In[ ]:


print(d)
d.clear()
print(d)


# Una vez ingresado a los ítem del diccionario, en caso de ser listas, podemos acceder a sus elementos tal cual lo hacemos con las listas (por sus índices)

# ### <span style="color:#4CC9F0">d.get(\<key>[, \<default>])</span>

# In[ ]:


print(my_dic.get('Colores'))


# In[ ]:


print(persona.get('Esposa'))


# #### Ejercicio

# ¿Qué significa default?

# ### <span style="color:#4CC9F0">d.items()</span>
# 

# In[ ]:


print(my_dic.items())


# In[ ]:


print(list(my_dic.items()))


# In[ ]:


list(my_dic.items())[0][1]


# También existen otros métodos útiles. ¡Averigua para que sirve cada uno!
# 
# - **d.keys()**
# - **d.values()**
# - **d.pop(\<key>[, \<default>])**
# - **d.popitem()**
# - **d.update(\<obj>)**

# #### Ejercicio

# A partir de las siguientes líneas de código, entienda lo que hace cada uno de los métodos y cree sus propio ejemplo de mayor complejidad.

# In[ ]:


print(my_dic)


# In[ ]:


print(my_dic.keys())
print(my_dic.values())
print(my_dic.pop('Colores'))
print(my_dic)
print(my_dic.popitem())
print(my_dic)
print(my_dic.update(persona))


# ## <span style="color:#4361EE">Char2int</span>

# Como último ejemplo construimos un diccionario para el alfabeto, de tal manera que dado un caracter retorne un código asociado.

# In[ ]:


alfabeto = 'abcdefghijklmnñopqrstuvwxyz'
alfaL = []
for j in alfabeto:
    alfaL.append(j)


char2int = {}
num = list(range(len(alfabeto)))

for car,val in zip(alfaL, num):
    char2int[car] = num[val]

print(char2int)
print('\n')
print('char2int[\'c\']=',char2int['c'])


# ### Conclusión

# Las listas y los diccionarios son los tipos de objetos más usados en Python.
# 
# Debido a su diferencia en la forma de accesar los datos, tienen diferentes usos, dependiendo de la situación.

# ## <span style="color:#4361EE">Métodos de los diccionarios</span>
# 

# |Método|Descripción                  |
# |---|---|
# |clear()|Elimina todos los elementos del diccionario.|
# |copy()|Devuelve una copia poco profunda del diccionario.|
# |get(clave[,valor])|Devuelve el valor de la clave. Si no existe, devuelve el valor valor si se indica y si no, None.|
# |items()|Devuelve una vista de los pares clave: valor del diccionario.|
# |keys()|Devuelve una vista de las claves del diccionario.|
# |pop(clave[,valor])|Devuelve el valor del elemento cuya clave es clave y elimina el elemento del diccionario. Si la clave no se encuentra, devuelve valor si se proporciona. Si la clave no se encuentra y no se indica valor, lanza la excepción KeyError.|
# |popitem()|Devuelve un par (clave, valor) aleatorio del diccionario. Si el diccionario está vacío, lanza la excepción KeyError.|
# |setdefault(clave[,valor])|Si la clave está en el diccionario, devuelve su valor. Si no lo está, inserta la clave con el valor valor y lo devuelve (si no se especifica valor, por defecto es None).|
# |update(iterable)|Actualiza el diccionario con los pares clave: valor del iterable.|
# |values()|Devuelve una vista de los valores del diccionario.|

# # <span style="color:#F72585">Conjuntos</span>

# Un conjunto es una colección de objetos inmutables no ordenada. Se crea con corchetes '{}'. Veamos el ejemplo.

# In[ ]:


frutas = {'banano','naranja', 'tomate'}

print(type(frutas))


# ## <span style="color:#4361EE">Operaciones con conjuntos</span>

# In[ ]:


print('banano' in frutas)
print('fresa' in frutas)


# In[ ]:


frutas.add('fresa')
print(frutas)


# ### <span style="color:#4CC9F0"> No puede haber elementos repetidos</span>

# In[ ]:


frutas.add('banano')
print(frutas)


# ### <span style="color:#4CC9F0">Operaciones usuales</span>

# In[ ]:


verduras = {'cebolla', 'tomate'}
print( verduras)


# In[ ]:


# intersección
print( frutas & verduras)


# In[ ]:


# unión
print( frutas | verduras)


# In[ ]:


# diferencia 
print( frutas - verduras)


# In[ ]:


# diferencia simétrica
print( frutas ^ verduras)


# ## <span style="color:#4361EE">Métodos de los conjuntos</span>

# |Método|Descripción|
# |---|---|
# |add(e)|Añade un elemento al conjunto.|
# |clear()|Elimina todos los elementos del conjunto.|
# |copy()|Devuelve una copia superficial del conjunto.|
# |difference(iterable)|Devuelve la diferencia del conjunto con el iterable como un conjunto nuevo.|
# |difference_update(iterable)|Actualiza el conjunto tras realizar la diferencia con el iterable.|
# |discard(e)|Elimina, si existe, el elemento del conjunto.|
# |intersection(iterable)|Devuelve la intersección del conjunto con el iterable como un conjunto nuevo.|
# |intersection_update(iterable)|Actualiza el conjunto tras realizar la intersección con el iterable.|
# |isdisjoint(iterable)|Devuelve True si dos conjuntos son disjuntos.|
# |issubset(iterable)|Devuelve True si el conjunto es subconjunto del iterable.|
# |issuperset(iterable)|Devuelve True si el conjunto es superconjunto del iterable.|
# |pop()|Obtiene y elimina un elemento de forma aleatoria del conjunto.|
# |remove(e)|Elimina el elemento del conjunto. Si no existe lanza un error.|
# |symmetric_difference(iterable)|Devuelve la diferencia simétrica del conjunto con el iterable como un conjunto nuevo.|
# |symmetric_difference_update(iterable)|Actualiza el conjunto tras realizar la diferencia simétrica con el iterable.|
# |union(iterable)|Devuelve la unión del conjunto con el iterable como un conjunto nuevo.|
# |update(iterable)|Actualiza el conjunto tras realizar la unión con el iterable.|

# ## <span style="color:#4361EE">Frozen sets</span>
# 

# Es posible crear conjuntos en donde los elementos no son intercambiables. Esto funciona como conjunto, pero ahora no es posible modificar los elementos del conjunto.
# 
# Veamos el ejemplo 
# 
# *frozenset(iterable)*

# In[ ]:


fruta_congelada = frozenset(frutas)


# In[ ]:


fruta_congelada.add('pera')


# ## <span style="color:#4361EE">Autores</span>

# 1. Alvaro Mauricio Montenegro Díaz, ammontenegrod@unal.edu.co
# 1. Daniel Mauricio Montenegro Reyes, dextronomo@gmail.com 

# ## <span style="color:#4361EE">Comentarios</span>
# 
