#!/usr/bin/env python
# coding: utf-8

# (1:prob1)=
# # <span style="color:#F72585">Conceptos básicos de probabilidad</span>

# ## <span style="color:#4361EE">Introducción</span>
# 
# 

# En esta sección se introducen los conceptos básicos de probabilidad requeridos para entender la inteligencia artificial. 
# 
# El propósito es presentar el lenguaje utilizado. No se hará ningún desarrollo matemático formal. Solamente se presentarán los cálculos que se consideran necesarios para entender el concepto.

# ## <span style="color:#4361EE">Espacio muestral</span>
# 
# 
# 

# La siguiente gráfica representa un ejemplo de un `espacio muestral`, el cual denotaremos como $\mathcal{M}$. Cada objeto dentro de la bolsa es un elemento del espacio muestral. Esto significa que este espacio muestral tiene $N=20$ elementos. Se supone que cada individuo puede identificarse de manera única. En este ejemplo hemos usado  un identificador $1,2,\ldots,20$, para cada uno de los elementos del espacio muestral. 
# 
# Adicionalmente,  cada individuo tiene un atributo de color. Hay tres colores diferentes: rojo, azul y gris.

# ```{admonition} Nota
# Se observa que el espacio muestral es un conjunto.
# ```

# ```{figure} https://raw.githubusercontent.com/AprendizajeProfundo/Diplomado/master/Temas/Módulo%201-%20Matemáticas%20y%20Estad%C3%ADstica/2.%20Estad%C3%ADsica%2C%20Teor%C3%ADa%20de%20la%20Decisión%20y%20Teor%C3%ADa%20de%20la%20información/Imagenes/prob_bolsa_bolas.png
# :height: 250px
# :name: espacio-muestral
# 
# Ejemplo de Espacio Muestral $\mathcal{M}$
# ```

# ## <span style="color:#4361EE">Evento</span>
# 
# 

# Un evento es cualquier subconjunto del espacio muestral. El lector interesado puede verificar, si lo desea, que el espacio muestral $\mathcal{M}$ tiene exactamente $2^{20}$ subconjuntos. 
# 
# Consideremos ahora seis eventos (subconjuntos) especiales de $\mathcal{M}$: 
# 
# 1. *azul*: el subconjunto de bolas azules;
# 2. *rojo*: el subconjunto de bolas rojas;
# 3. *gris*: el subconjunto de bolas grises.
# 4. *pares*: el subconjunto de bolas pares.
# 5. *impares*: el subconjunto de bolas impares.
# 6. *pares azules*: el subconjunto de bolas pares azules.
# 
# La gráfica muestra los 6 eventos (subconjuntos) del espacio muestral.

# :::{figure-md} markdown-fig
# <img src="https://raw.githubusercontent.com/AprendizajeProfundo/Diplomado/master/Temas/Módulo%201-%20Matemáticas%20y%20Estad%C3%ADstica/2.%20Estad%C3%ADsica%2C%20Teor%C3%ADa%20de%20la%20Decisión%20y%20Teor%C3%ADa%20de%20la%20información/Imagenes/prob_bolas_subconjuntos.png" alt="evento" class="bg-primary mb-1" width="600px">
# 
# Ejemplos de **eventos** del Espacio Muestral
# :::

# (prob1:ej1)=
# ## <span style="color:#4361EE">Probabilidad</span>
# 
# 

# ## <span style="color:#4361EE">Regla aditiva de la probabilidad</span>

# La probabilidad de la unión de dos eventos (subconjuntos) disyuntos (que no tiene intersección) es la suma de la probabilidad (medida) de cada uno de ellos. En símbolos, si $A$ y $B$ son eventos disyuntos de $\mathcal{M}$, entonces
# 
# $$
# \text{Prob}[A\cup B] = \text{Prob}[A] + \text{Prob}[B].
# $$ (mylabel)
# 
# 
# Por ejemplo, observe que $\text{Prob}[\text{azul}\cup\text{rojo}] = 5/20+7/20 = 12/20$. ¿Porque decimos que *azul* y  *rojo* son eventos disyuntos.
# 
# 
# Sin embargo 
# 
# $$
# \text{Prob}[\text{azul}\cup\text{pares}] \ne 5/20 + 9/20.
# $$
# 
# Esto se debe a que los eventos *azul* y *pares*, no son disyuntos. Como se muestra en la parte inferior derecha de la gráfica arriba, se tiene que $\text{Prob}[\text{azul}\cap \text{pares}] = 3/20$. ¿Cómo afecta esta situación el resultado el cálculo de la probabilidad de la unión de dos evento?
# 
# Lo anterior conduce a la regla aditiva general la cual dice que
# 
# 

# 
# 
# ```{math}
# :label: eq-label
# 
# \text{Prob}[A\cup B] = \text{Prob}[A] + \text{Prob}[B]-\text{Prob}[A\cap B] .
# ```
# 
# En el ejemplo se tiene entonces que
# 
# $$
# \text{Prob}[\text{azul}\cup\text{pares}] = 5/20 + 10/20 - 3/20 = 12/20
# $$

# ### <span style="color:#4CC9F0">Medida de todo el espacio muestral</span>

# Vamos a denotar por $\emptyset$ al conjunto vacío, es decir un conjunto que no tiene elementos.
# 
# En nuestro ejemplo tenemos que 
# 
# $$\mathcal{M}= \text{azul}\cup \text{rojo}\cup \text{gris}$$ 

# 
# 
# Además se tiene que
# 
# $$
# \begin{align}
# \text{azul}\cap \text{rojo} &= \emptyset\\
# \text{azul}\cap \text{gris} &= \emptyset\\
# \text{gris}\cap \text{rojo} &= \emptyset\\
# \end{align}
# $$
# 
# Se dice en esta situación que los conjuntos son {ref}`prob:mutuamente_excluyentes`.  De acuerdo con la regla aditiva tenemos que
# 
# $$
# \text{Prob}[\mathcal{M}] = \text{Prob}[\text{azul}] +  \text{Prob}[\text{rojo}]+  \text{Prob}[\text{gris}] = 5/20 + 7/20 + 8/20 = 1.
# $$
# 
# Esta es una propiedad general de la probabilidad. El espacio muestral siempre tiene medida de probabilidad 1. 
# 
# Además observe que si se tienen eventos disyuntos entre sí (mutuamente excluyentes), cuya unión es el espacio muestral, entonces la probabilidad de la unión de todos esos eventos tiene probabilidad 1.

# ### <span style="color:#4CC9F0">Probabilidad del complemento de un evento </span>

# El complemento de un evento $A$ se denotará por $A^{c}$. Este simplemente el conjunto de elementos del espacio muestral que están por fuera de $A$. Entonces, es inmediato que $\mathcal{M} = A\cup A^c$. Por lo que 
# 
# $$
# Prob[A^c] = 1 - Prob[A].
# $$
# 
# Una consecuencia inmediata de esta propiedad es que como $\mathcal{M}^c= \emptyset$, porque el espacio muestral contiene a todos los elementos, entonces $Prob[\emptyset]=0$.
# 
# 
# En nuestro ejemplo $impares^c= pares$. Entonces $Prob[\text{impares} ] = 1- 9/20 = 11/20$. Por favor verifica este resultado.

# (prob1:ej2)=
# ## <span style="color:#4361EE">Probabilidad condicional</span>

# El concepto de probabilidad condicional es de vital importancia en el estudio del aprendizaje profundo y la inteligencia artificial.
# 
# Como el nombre parece indicar, es trata de calcular la probabilidad de un evento sujeto a una restricción. En realidad es así y la restricción normalmente está asociada con otro evento.
# 
# Para ilustrar el asunto, supongamos que se pregunta por la probabilidad que una bola extraída sea par, dado que la bola es azul.
# 
# Se observa entonces, que se da una información antes de calcular la probabilidad de ser par. Esta información corresponde al evento *azul*. Escribiremos
# 
# $$
# \text{Prob}(\text{par}|\text{azul})
# $$
# 
# 
# Para hacer el cálculo correcto, se procede de la siguiente manera: Primero se reduce el espacio muestra a *azul*. En el ejemplo se tiene que  
# 
# $$
# \text{azul} = \{5,7,8,10,16 \}.
# $$
# 
# Ahora que se ha restringido el espacio muestral a *azul*, se calcula la probabilidad de interés. En este caso *par*. Observe entonces que 
# 
# $$
# \text{Prob}(\text{par}|\text{azul}) = \tfrac{3}{5},
# $$
# 
# porque en el evento *azul* que tiene 5 elementos hay 3 *pares*.
# 
# 
# Puede verificarse que 
# 
# $$
# \text{Prob}(\text{par}|\text{azul}) = \frac{\text{Prob}[\text{par}\cap \text{azul}]}{\text{Prob}[\text{azul}]}
# $$

# :::{admonition} Importante
# :class: tip
# Esta es una regla general, que se enuncia así: 
# Si $A$ y $B$ son eventos del espacio muestral $\mathcal{M}$, entonces se define $\text{Prob}[A|B]$ como
# 
# $$
# \text{Prob}[A|B] = \frac{\text{Prob}[A\cap B]}{\text{Prob}[B]}
# $$
# :::

# ## <span style="color:#4361EE">Regla multiplicativa de la probabilidad</span>

# De la definición de la probabilidad condicional $\text{Prob}[A|B]$ se desprende que 
# 
# $$
# \text{Prob}[A\cap B] = \text{Prob}[B]\times \text{Prob}[A|B]
# $$

# ### <span style="color:#4CC9F0">Ejemplo</span>

# Con nuestro ejemplo supongamos que se pregunta por la probabilidad de obtener una bola par azul en un experimento.
# 
# La solución es sencilla, por que ya hemos obtenido que $\text{Prob}(\text{par}|\text{azul}) = \tfrac{3}{5}$,
# y $\text{Prob}[\text{azul}] = 5/20$. por lo tanto
# 
# $$
# \text{Prob}[\text{par}\cap\text{azul}] = \text{Prob}[\text{azul}]\times\text{Prob}[\text{par}|\text{azul}] = \tfrac{5}{20}\times \tfrac{3}{5} =  \tfrac{3}{20}
# $$
# 
# Esto está de acuerdo con la ilustración de los evento del espacio muestral exhibidos arriba.

# (prob1:ej3)=
# ## <span style="color:#4361EE">Independencia</span>

# Dos eventos $A$ y $B$ del espacio muestral $\mathcal{M}$ se dicen independientes si
# 
# 
# $$
# \text{Prob}[A\cap B] = \text{Prob}[A] \times\text{Prob}[B].
# $$
# 
# 
# Esta definición es bastante técnica, pero intuitivamente puede entenderse como que la ocurrencia de un evento no afecta la ocurrencia del otro. Observe que en este caso se tiene que
# 
# $$
# \text{Prob}[A| B] = \text{Prob}[A].
# $$

# ## <span style="color:#4361EE">Autores</span>

# 1. Alvaro Mauricio Montenegro Díaz, ammontenegrod@unal.edu.co
# 1. Daniel Mauricio Montenegro Reyes, dextronomo@gmail.com 

# ## <span style="color:#4361EE">Comentarios</span>
# ```{raw} html
# <script src="https://utteranc.es/client.js"
#         repo="Yesenia-AriasC / book_pruebas"
#         issue-term="nombre de ruta"
#         label="proba_basic"
#         theme="boxy-light"
#         crossorigin="anónimo"
#         asíncrono>
# </script>
# ```
# 
# 
