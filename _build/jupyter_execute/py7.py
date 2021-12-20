#!/usr/bin/env python
# coding: utf-8

# (2:py7)=

# # <span style="color:#F72585">Taller de manejo de Datos en Pandas</span> 
# 

# ## <span style="color:#4361EE">¿Qué es?</span>
# 

# Pandas es una librería de python destinada al análisis y manipulación de datos. Para obtener más información de ella, pueden revisar este [link](https://pandas.pydata.org/).

# In[1]:


get_ipython().system('pip install pandas openpyxl')


# In[2]:


import pandas as pd


# ## <span style="color:#4361EE">¿Cómo importar datos?</span>

# Para leer los datos la estructura básica es *pd.read_tipo-archivo*. Si estamos en colab y queremos utilizar algunos datos que están en nuestro google drive podemos utilizar:
# 
# 
# ```
#       from google.colab import drive
#       drive.mount('/content/gdrive')
# ```

# In[3]:


#from google.colab import ##drive correr solo en colab
#drive.mount('/content/gdrive')
counties= pd.read_excel("https://github.com/Yesenia-AriasC/book_pruebas/blob/Venus/counties.xlsx?raw=true")#cambiar dirección


# Para tener una idea de qué variables y datos tengo en lo base de datos, sólo debemos llamarla.

# In[4]:


counties


# En lo anterior veiamos todas las variables con las 5 primeras y 5 últimas filas. Pero, podemos ver una cantidad  determinada de registros tanto del inicio de la tabla como del final. Utilizando *.head()* y *.tail()* respectivamente.

# In[5]:


counties.head(3) #por defecto salen 5 primeros


# In[6]:


counties.tail(2)


# Si aparte de ver solamente la tabla, queremos más información de la base de datos, por ejemplo sus dimensiones y tipo de variables podemos  utilizar lo siguiente:

# In[7]:


counties.info()
print("\n")
print("La forma de la base de datos es:",counties.shape)  #shape:forma de un array


# In[8]:


print(counties.dtypes) #tipo de objeto en cada columna
print("\n")
print(counties.describe())
print("\n")
print(counties.describe(include="all")) #summary, si no se pone el include solo aparece de las variables numéricas


# ## <span style="color:#4361EE">Seleccionar subconjuntos de una base de datos</span>

# ### <span style="color:#4CC9F0">Escoger columnas </span>

# Para ver el nombre de las columnas que existen, podemos utilizar *.columns*.

# In[9]:


counties.columns


# Escoger una columna específica o un conjunto de ellas

# In[10]:


condado = counties["county"]


# In[11]:


print(condado.shape) #array unidimensional con 3234 elementos
print(counties["county"].shape)
print(type(condado))


# In[12]:


codi_condado=counties[["codecounty","county"]]
print(codi_condado)
print(type(codi_condado))


# ### <span style="color:#4CC9F0">Escoger filas </span>

# Podemos escoger ciertas filas a través de su posición. utilizando *.iloc*

# In[13]:


get_ipython().system('pip install seaborn')


# In[14]:


from seaborn import load_dataset


# In[15]:


print(counties.iloc[0:1,])
print(type(counties.iloc[0:1,]))


# In[16]:


print(counties.iloc[8:12,1:3])


# O también escoger filas con base a alguna condicion o característica específica.

# In[17]:


counties.tail()


# In[18]:


counties["codestate"] > 72 #Verdadero o falso si cumple la condición


# In[19]:


codsat72 = counties[counties["codestate"] > 72] # Llama aquellos cuyo valor es verdadero
codsat72.info()


# Filas que no tengan valores faltantes en determinada columna

# In[20]:


no_na = counties[counties["population"].notna()]
print(no_na.shape)
print(counties.shape)


# ### <span style="color:#4CC9F0">Filas con valores específicos </span>

# Existen varias maneras de realizar estas búsquedas, algunas de ellas son utilizando *isin*, *loc* de la librería seaborn y *or*.

# In[21]:


codcou1 = counties[counties["codecounty"].isin([78010, 72151])]
codcou1


# In[22]:


codcou2 = counties.loc[:, 'codecounty'] == 78010
codcou2_ = counties.loc[codcou2]
codcou2_


# In[23]:


counties[(counties["codecounty"] == 78010) | (counties["codecounty"] == 72151)]


# Filas con más de una característica específica.

# In[24]:



counties[(counties["codestate"] == 72) & (counties["area"] >= 60)].info()


# ### <span style="color:#4CC9F0">Eliminar valores omitidos </span>

# In[25]:


#Eliminar valores omitidos: dropna
# axis= 0 -> Eliminar fila completa
# axis=1 -> Eliminar columna completa
counties.dropna(subset=["population"], axis=0, inplace=False) #inplace:modifique directamente la BD


# ## <span style="color:#4CC9F0">Manipulación datos textuales</span>

# Para realizarle limpieza a columna *county* de la base de datos counties, podemos utilizar lo siguiente:
# 
# * **lower:**Poner en minúscula todo el texto.
# * **replace:**Remplazar ciertos valores por otros.
# * **strip:**Eliminar los espacios al principio y al final de la cadena.
# * **title:**Poner primera letra de cada palabra en mayúscula.

# In[26]:


counties["county"] = (counties["county"]
                            .str.lower()
                            .str.replace("[^a-záéíóúüñ ]","")
                            .str.replace(" +"," ")
                            .str.strip()
                            .str.title()
                           ) 


# In[27]:


print(counties)


# ## <span style="color:#4361EE">Creación de columnas a partir de otras</span>

# In[28]:


counties["densidad"]= counties["population"]/counties["area"]
print(counties[["densidad","population","area"]])


# ### <span style="color:#4CC9F0">Renombrar columnas</span>

# In[29]:


print(counties.columns)
counties.rename(columns={"densidad":"densidad_pob"},inplace=True) #renombrar columna
print(counties.columns) #Verificación


# ### <span style="color:#4CC9F0">Modificar tipo de dato de una columna</span>

# In[30]:


print(counties.info())
print("\n")
counties["codestate"]=counties["codestate"].astype("float")
print(counties.info())


# ### <span style="color:#4CC9F0">Eliminar filas y columnas</span>

# Eliminación filas, puede ser por posición o que cumpla una característica.

# In[31]:


print(counties.shape)
counties = counties.drop(counties.iloc[0:3,].index)
counties = counties.drop(counties[counties['codecounty']==70].index)
print(counties.shape)


# In[32]:


counties.drop(['densidad_pob'], axis=1,inplace=True) #inplace=True, para que me modifique la BD
counties.columns


# ### <span style="color:#4CC9F0">Conteos</span>

# In[33]:


counties.groupby("codestate")["codecounty"].count().head(10)


# ## <span style="color:#4361EE">Modificar tablas</span>
# 
# es posible hacer cambios de orden y estructura en las tablas de pandas.

# In[34]:


elections=pd.read_excel("https://github.com/AprendizajeProfundo/Diplomado/blob/master/Temas/M%C3%B3dulo%2013-%20Talleres/Datos/elections.xlsx?raw=true")
elections.head(5)


# organicemos los datos descendentemente depende de la cantidad de votos democratas

# In[35]:


elections.sort_values(["democrat"], ascending=False)


# usando `groupby()` podemos juntar los datos por año y sumarlos para tener el total de votos por año

# In[36]:


elections.groupby('year')[['democrat', 'republic']].sum()


# Podemos aplicar ambos métodos en un mismo código

# In[37]:


elections_sort=(elections.groupby('year')[['democrat', 'republic']]
                .sum()
                .sort_values('democrat', ascending=False))
display(elections_sort)


# Para reestructurar los datos usamos la función `pivot()`.

# In[38]:


pivot_elections=elections.pivot(index='codecounty',
                columns='year',
                values=['democrat','republic'])
pivot_elections.head()


# ### <span style="color:#4CC9F0">Múltiples Índices</span>
# 
# Se pueden elegir múltiples variables como índice del dataframe. Esto es util para facilitar la extracción de información en ciertos casos

# In[39]:


counties_multi=pd.read_excel("https://github.com/Yesenia-AriasC/book_pruebas/blob/Venus/counties.xlsx?raw=true", index_col=[0, 1])
display(counties_multi)


# Podemos obtener la suma de población de cada estado

# In[40]:


counties_multi["population"].sum(level='codestate').head(5)


# ### <span style="color:#4CC9F0">Concatenar y Unir</span>
# 
# Es posible unir varias tablas tanto vertical como horizontalmente.
# 
# 
# En ambos casos, podemos usar `concat()`, y se juntarán las bases con bases a los nombres de columnas o los indices de las filas

# In[41]:


elections_2000=elections[elections['year']==2000]
display(elections_2000) #display:ejecuta el método dunder apropiado para obtener los datos apropiados para mostrar


# In[42]:


elections_2004=elections[elections['year']==2004]
elections_2004['dummy']=0
display(elections_2004)


# Si se hace la concatenación sin más, se tomarán todas las columnas y se agregarán NaN

# In[43]:


elections_00_04=pd.concat([elections_2000, elections_2004])
display(elections_00_04)


# Ahora, usando `merge()`, podemos hacer uniones  de las tablas de forma horizontal que compartan una columna/indice en común

# :::{figure-md} markdown-fig
# <img src="https://raw.githubusercontent.com/AprendizajeProfundo/Diplomado/master/Temas/M%C3%B3dulo%2013-%20Talleres/Imagenes/Joins.png" alt="evento" class="bg-primary mb-1" width="600px">
# 
# Tipos de Join
# :::

# In[44]:


display(counties)


# In[45]:


inner_joined=pd.merge(elections, counties)
inner_joined.head(10)


# In[46]:


outer_joined=pd.merge(elections, counties, how='outer')
outer_joined.head(10)


# In[47]:


left_joined=pd.merge(elections, counties, how='left')
left_joined.head(10)


# In[48]:


right_joined=pd.merge(elections, counties, how='right')
right_joined.head(10)


# 
# ## <span style="color:#4361EE">Series de tiempo y time stamps</span>

# Existe un tipo de datos llamado "timestamp" que se usa para medir registros de tiempo. Es posible pasar strings a este tipo de dato en diferentes formatos y trabajar con este usándolo como indice

# In[49]:


airrpm=pd.read_csv("https://raw.githubusercontent.com/Yesenia-AriasC/book_pruebas/Venus/airrpm.txt", header=None, delimiter= '\s+', decimal=",")
airrpm.columns=["Time", "R1", "R2", "R3"]
airrpm.head()


# La variable "Time" en este momento es un string. Pero podemos transformarlo usando `to_datetime()`. Para obtener más información de qué se podría poner en `format`, pueden revisar este [link](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)

# In[50]:


airrpm['Time']=pd.to_datetime(airrpm['Time'], format='%b-%y')
airrpm.index=airrpm['Time']
airrpm=airrpm.drop(['Time'], axis=1)
airrpm.head()


# Definiendo la fecha como índice, podemos extraer información con respecto al año y respecto al mes

# In[51]:


airrpm.groupby([airrpm.index.month])['R1'].describe()


# In[52]:


airrpm.groupby([airrpm.index.year]).sum().head(10)


# ## <span style="color:#4361EE">Autores</span>
# 1. Oleg Jarma, ojarmam@unal.edu.co 
# 2. Laura Lizarazo, ljlizarazore@unal.edu.co 
# 

# ##   <span style="color:#4361EE">Comentarios</span>
# 
