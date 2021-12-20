#!/usr/bin/env python
# coding: utf-8

# (2:py8)=

# # <span style="color:#F72585">Introducción a tensores</span> 

# ## <span style="color:#4361EE">Introducción</span>
# 

# En este cuaderno se introducen los conceptos de vectores, matrices y tensores.
# 
# Los tensores son la estructura de datos más utilizada en el aprendizaje profundo. Desde el punto de vista matemático, un tensor generaliza los conceptos de escalares, vectores y matrices. 
# 
# Solamente haremos la introducción al concepto de tensores desde el punto de vista de las estructuras de datos requeridas en el aprendizaje profundo.

# ## <span style="color:#4361EE">Vectores (Tensores unidimensionales)</span>
# 

# En esta sección revisamos el concepto de vector. Desde el punto de vista del aprendizaje profundo. Entendemos un vector como un contenedor de  *n* datos, cada uno de los cuales se identifica genéricamente mediante un índice. Por ejemplo supongamos que $w$ es un vector de tamaño tres. Este vector se representa genéricamente como 
# 
# $$
# \begin{equation}
# w = (w_1,w_2, w_3).
# \end{equation}
# $$
# 
# En estadística es usual escribir los vectores el columna. En este caso $w$ se escribe como
# 
# 
# $$
# \begin{equation}
# w = \begin{pmatrix} w_1\\ w_2 \\ w_3\end{pmatrix}.
# \end{equation}
# $$
# 
# 
# El tipo de valores que puede contener un vector debe ser de la misma clase por convención. Por ejemplo, si $w$ es un vector de números reales, entonces *z=(3.2, 1.5, -7.2,0.0)* es un vector real de tamaño cuatro. Matemáticamente se dice el vector *z* tiene dimensión cuatro. En otras palabras, la dimension matemática de un vector es su tamaño.
# 
# El contenido y tipo de datos de un vector depende del contexto en que se está utilizando. Supongamos que se trata de construir una máquina de aprendizaje profundo que identifique digitos escritos a mano. Lo que se acostumbra a hacer es digitalizar las imágenes correspondientes. 

# ### <span style="color:#4CC9F0">Ejemplo en Numpy</span> 

# En [NumPy](https://numpy.org/) el vector $w =(1,2,3)$ se puede crear así:

# In[1]:


get_ipython().system('pip install numpy matplotlib')


# In[2]:


import numpy as np
# crea el vector (array)
w = np.array([1,2,3]) 
# lo imprime
print(w)
# Muestra el tamaño (shape) del vector
print(w.shape)


# ### <span style="color:#4CC9F0">Discusión:¿Vector o Tensor?</span> 

# En matemáticas la dimensión por lo general hace referencia al número de componentes con el que se representa un objeto en un espacio. Por lo general el espacio Euclideano, digamos $\mathbf{R}^2$ o $\mathbf{R}^3$.
# 
# El siguiente código dibuja algunos vectores en $\mathbf{R}^2$. Los  matemáticos dicen que estos objetos geométricos tienen dimensión geométrica 2. Por favor revisa cada línea del código para estar seguro que lo entiende.

# In[3]:


import numpy as np
import matplotlib.pyplot as plt

soa = np.array([[0, 0, 4, 1], [0, 0, 1, 5], [0, 0, 3, 2]])
X, Y, U, V = zip(*soa)
plt.figure()
plt.title('Vectores en el espacio Euclideano $R^2$ ')
ax = plt.gca()
ax.quiver(X, Y, U, V, angles='xy', scale_units='xy', scale=1)
ax.set_xlim([-1, 6])
ax.set_ylim([-1, 6])
plt.draw()
plt.show()


# :::{admonition} Ayuda
# :class: tip
# Por ejemplo busque en Google [ax.quiver](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.axes.Axes.quiver.html).
# :::
# 

# Los tensores son objetos de tipo algebraico. La dimensión de un tensor se define como el número de índices requerido para representar todos a los elementos del tensor.
# 
# Entonces:
# 
# 1. El vector $w = (w_1,w_2, w_3)$ tiene dimensión 3.
# 2. El tensor $w = (w_1,w_2, w_3)$ tiene dimensión 1 y tamaño (shape = 3).
# 
# En aprendizaje profundo usaremos con más frecuencia el concepto de tensor. **Asegúrese de comprender la diferencia**.

# ## <span style="color:#4361EE">Aritmética básica de tensores unidimensionales</span>
# 

# Mientras no se diga lo contrario, asumiremos que los tensores que usaremos tienen el mismo tamaño. Por facilidad, en las definiciones usaremos tensores unidimensionales de tamaño $n=3$. En realidad el tamaño de los tensores unidimensionales puede ser cualquier número entero $n$ y las definiciones se generalizan de forma obvia.

# Supongamos que $a= (a_1,a_2,a_3)$ y $b=(b_1,b_2,b_3)$ son dos vectores. La suma entre $a$ Y $b$ es un vector $c$ definido por
# 
# $$
# c = a+b = (a_1+b_1, a_2+b_2,a_3+b_3)
# $$
# 
# En Python escribimos

# In[4]:


a = np.array([1,2,3])
b = np.array([7,8,9])
c = a + b
print(c)


# Similarmente la diferencia  de vectores $a-b$ es definida por
# 
# $$
# c = a-b = (a_1-b_1, a_2-b_2,a_3-b_3)
# $$

# In[5]:


a = np.array([1,2,3])
b = np.array([7,8,9])
c = a - b
print(c)


# El producto de Hadamard, o producto elemento by elemento entre dos vectores se denota $a \odot b$ y se define como
# 
# $$
# c = a\odot b = (a_1*b_1, a_2*b_2,a_3*b_3).
# $$
# 
# En Python el producto de Hadamard se implementa simplemente usando el operador de multiplicación (*). Veamos
# 

# In[6]:


a = np.array([1,2,3])
b = np.array([7,8,9])
c = a * b
print(c)


# La división entre vectores no es una operación formalmente definida. En ocasiones sin embargo se requiere dividir los elementos de un vector entre los elementos de otro, elemento a elemento. Esta operación se implementa en Python simplemente usando el operador división (/)

# In[7]:


a = np.array([1,2,3])
b = np.array([7,8,9])
c = a / b
print(c)


# ## <span style="color:#4361EE">Matrices (Tensores bidimensionales)</span>
# 

# Una matriz es una organización (tensor) bidimensional. Por ejemplo la matriz  $M$ de tamaño $2\times 3$ puede ser
# 
# $$
# \begin{pmatrix} 1 & 2 & 3\\
# 4 &5 & 6
# \end{pmatrix}
# $$
# 
# Las matrices son muy utilizadas en prácticamente todas las área de la ciencia y la tecnología. 
# 
# En el caso del aprendizaje profundo, y más generalmente en Estadística las matrices se usan para representar conjuntos de datos. En los casos de regresión, las filas usualmente representan individuos y las columnas variables.
# 
# En adelante llamaremos a las matrices tensores bidimensionales (o de dos dimensiones). Entonces Una matriz que tiene $m$filas y $n$ columnas, es un tensor bidimensional de tamaño (shape) $=(m,n)$.
# 
# El tensor $M$ se representa en NumPy de la siguiente forma:

# In[8]:


import numpy as np

# Crea el tensor
M = np.array([[1,2,3],
              [4,5,6]])
# Imprime el Tensor
print(M)
# Muestra la forma (shape)
M.shape


# 
# ## <span style="color:#4361EE">Creación de algunos tensores bidimensionales</span>
# 

# ### <span style="color:#4CC9F0">Tensor vacío</span>

# La función *empty()* crea un arreglo de la forma especificada. 

# In[9]:


v = np.empty([2,3])
print(v)
print(v.shape)


# Observe que *v* es un tensor que tiene forma (shape) *2x2*. En NumPy un tensor está compuesto por uno más tensores. La dimensión del tensor *v* es 2. Se requiere un objeto de doble entrada para representar un tensor bidimensional. Los rangos de este tensor son $(2,3)$. Observe que el arreglo es representado como una lista con dos elementos, cada uno de los cuales es un arreglo de rango 3.

# ### <span style="color:#4CC9F0">Tensor de ceros</span>
# 

# La función *zeros()* crea un arreglo de la forma especificada relleno de ceros.

# In[10]:


w = np.zeros([3,2])
print(w)


# ### <span style="color:#4CC9F0">Arreglo de unos</span>

# La función *ones()* crea un arreglo de la forma especificada relleno de unos.

# In[11]:


w = np.ones([2,2])
print(w)


# ### <span style="color:#4CC9F0">Combinación de arreglos</span>

# **Vertical**. Con la función *vstack()*

# In[12]:


v = np.ones([2,3])
w = np.array([2,2,2])
z = np.vstack((v,w))
print(z)
print(z.shape)


# **horizontal**. Con la función *hstack()*

# In[13]:


v = np.ones([2,3])
w = np.array([[5],[5]])
z = np.hstack((v,w))
print(z)
print(z.shape)


# ## <span style="color:#4361EE">Creación de tensores multidimensionales</span>

# En Pyhton una lista de listas puede crearse como se muestra en el siguiente fragmento de código. En el código se observa como acceder a la primera lista y como acceder al segundo elemento de la segunda lista. Asegúrese de entender la lógica involucrada.

# ### <span style="color:#4CC9F0">Ejemplo con arreglos tridimensionales</span>
# 
# Para completar de entender la indexación y rebanado de arreglos, observe el siguiente ejemplo. Asegúrese de entender completamente la lógica.

# In[14]:


a = np.array([[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]],[[13,14],[15,16],[17,18]],
              [[19,20],[21,22],[23,24]]])
print('a.shape=', a.shape)
print('a =',a)


# ## <span style="color:#4361EE">Tarea</span>
# 

# Investigue sobre los siguiebtes temas
# 
# 1. Indexación de tensores Numpy.
# 2. Rabanado (slicing) de tensores
# 3. Reorganización (Reshape) de tensores

# ## <span style="color:#4361EE">Algebra Tensorial</span>
# 

# Numpy esta preparado para trabajar las operaciones ordinarias del álgebra lineal y más extendidamente del álgebra tensorial directamente. Los siguientes ejemplos muestran como sumar,....

# In[15]:


# Tensor-operations
# We use 3*2*3 arrays (tensors)
a = np.array([[[1,2,3],[4,5,6]],[[10,20,30],[40,50,60]],[[100,200,300],[400,500,600]]])
print(a.shape)
print(a)
# Observe that has 3 layers of shape 2*3


# In[16]:


# multiply a by -1
b = -a
print(b.shape)
print(b)


# In[17]:


# sum
c = a + b
print("c=",c)
print(c.shape)


# In[18]:


# difference
c = a - b
print("c=",c)
print(c.shape)


# In[19]:


# Hadamard product
c = a * b
print("c=",c)
print(c.shape)


# In[20]:


# component-wise division
c = a / b
print("c=",c)
print(c.shape)


# ### <span style="color:#4CC9F0">Producto escalar (dot product)</span>
# 
# 

# Si $a=(a_1,a_2,a_3)$ y $b=(b_1,b_2, b_3)$ el producto escalar entre $a$ y $b$ está definido por
# 
# $$
# <a,b> = a_1b_1 + a_2b_2+a_3b_3
# $$
# 
# Este producto es base de mucho métodos estadísticos, como la comparación misma de vectores.
# 
# Con Numpy escribimos

# In[21]:


# dot product (vectors): c = sum(a_i*b_i)
a = np.array([1,2,3])
b = np.array([4,5,6])
c = np.dot(a,b)
print("c=",c)
print(c.shape)


# ### <span style="color:#4CC9F0">Producto de matrices (2D-Tensores)</span>
# 
# 
# Supongamos que $A=[a_{ij}]_{N\times P}$ y  $B=[b_{jk}]_{P\times Q}$ son matrices de tamaños (shape) $N\times P$ y $P\times Q$ respectivamente. Entonces $C = A\times B$ es una matriz $C=[c_{ik}]_{N\times Q}$ de tamaño $P\times Q$, en donde 
# 
# $$
# \begin{equation}
# c_{ik} = \sum_{j=1}^{P} a_{ij}b_{jk}
# \end{equation}
# $$

# In[22]:


# dot product (tensors ): c = sum(a_i*b_i)
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120]])          
print("A=",A)
print("A.shape =",A.shape)
print("B=",B)
print("B.shape =",B.shape)
# Matrix product ( equivalent results)
# prefer C or D computation
C = A @ B
D = np.matmul(A,B)
E = np.dot(A,B)
print("C=",C)
print("C.shape =",C.shape)
print("D=",D)
print("E=",E)


# In[23]:


# a.dot puede ser encadenado con arreglos 2D
a = np.eye(2) #identity matrix 2x2
b = np.ones((2,2))*2# matrix 2x2, full of ith 2's 
a.dot(b).dot(b)


# ### <span style="color:#4CC9F0">Trabajando con arreglos de diferente tamaño(broadcasting)</span>
# 
# 
# Si *a* es escalar (0-D array) y *b* es N-D array) se multiplican todos los elementos de *b* por *a*. Revise el ejemplo anterior.
# 
# Si *a* en un arreglo N-dimensional (N-D) y b es un arreglo 1D (uno-dimensional)

# In[24]:


a = np.array([[1,2],[3,4],[5,6]])
b = np.array([[10],[100]])
c = a.dot(b)   
d = a@b


# In[25]:


print('a=', a)
print('b=', b)
print('c=', c)
print('d=', d)


# ### <span style="color:#4CC9F0">Producto tensorial</span>

# Trabajando con un arreglo *A*  3-D y arreglo *B* 1D de tal forma que el tamaño de la última dimension de *A* coincide con el tamaño de *B*, el producto se puede ver como el resultado del producto de matrices  entre la matriz en cada capa por el vector *B*.
# 
# En el siguiente ejemplo *A* tiene tamaño 4x3x2 y *b* tiene tamaño 2 (en realidad 2x1). Entonces el producto tensorial *C=A@B* da como resultado un arreglo de tamaño 4x3x1. Cada una de las 4 matrices de tamaño 3x2 del arreglo *A* se multiplican por el vector *B*, lo que da como resultado 4 matrices de tamaño 3x1. Veamos los cálculos con Numpy.

# In[26]:


a = np.array([[[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]],[[13,14],[15,16],[17,18]],
              [[19,20],[21,22],[23,24]]])
b = np.array([[10],[100]])
c = a.dot(b)   
d = a@b
# revisamos este subcálculo. a_0 es la primera matrix 3x2 del arreglo A.
a_0 = a[0,:,:]
# e es la primera matriz de tamaño 3*1 del producto. Compare los resultados.
e = a_0@b


# In[27]:


print('a=', a)
print('a.shape=',a.shape)
print('b=', b)
print('b.shape=',b.shape)
print('c=', c)
print('d=', d)
print('d.shape=',d.shape)
print('e=', e)
print('a_1.shape',a_0.shape)
print('e.shape=',e.shape)


# ## <span style="color:#4361EE">Autores</span>
# 
# 1. Alvaro Mauricio Montenegro Díaz, ammontenegrod@unal.edu.co
# 2. Daniel Mauricio Montenegro Reyes, dextronomo@gmail.com 
# 3. Oleg Jarma, ojarmam@unal.edu.co 

# 
# ## <span style="color:#4361EE">Comentarios</span>
