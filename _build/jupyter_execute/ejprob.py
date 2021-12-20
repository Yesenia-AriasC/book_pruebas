#!/usr/bin/env python
# coding: utf-8

# # <span style="color:#F72585">Ejercicios</span>

# (prob:ej1)=
# ## <span style="color:#4361EE">[Conceptos Básicos de Probabilidad](1:prob1)</span>

# 
# Considere el siguiente experimento. Se lanzan dos dados no cargados de seis caras cada uno. El resultado del experimento es una pareja de números. Por ejemplo $(5,6)$.

# ```{figure} https://raw.githubusercontent.com/Yesenia-AriasC/PRT/master/dos_dados.png
# :height: 150px
# :name: dos-dados
# 
# Fuente ...
# ```

# 1. Haga una tabla, usando Markdown con todo el espacio muestral $\mathcal{M}$. Ayuda: son 36 elementos.
# 2. ¿Cuántos eventos son posibles? Use Python para hacer el cálculo 2^36
# 2. Calcule la probabilidad de obtener 2,3,... 12.
# 3. Calcule la probabilidad de obtener un número par.
# 4. Compruebe que la probabilidad de obtener 5 en el dado azul es 1/5 y que este evento es independiente del valor obtenido en el dado rojo.
# 4. Escriba un programa Python que construya un tensor de dimensión 2 y que contenga los 36 posibles resultados. Consulte  sobre como se hace un ciclo for en Python.

# <span style="color:green">Escriba aquí su respuesta. Discuta con sus compañeros.</span>

# ### <span style="color:#4CC9F0">[Probabilidad de la Intersección](prob1:ej1)</span>

# ¿Qué piensa de la siguiente afirmación?. ¿Verdadero o falso? Justifique su respuesta.
# 
# Si $A$ y $B$ son conjuntos disyuntos, entonces $\text{Prob}[A\cap B] = 0$.
# 

# <span style="color:green">Escriba aquí su respuesta. Discuta con sus compañeros.</span>

# ### <span style="color:#4CC9F0">[Probabilidad condicional](prob1:ej2)</span>

# Imagínese como se podría verificar la siguiente ecuación según el ejemplo dado en {ref}`prob1:ej2` $\text{Prob}(\text{par}|\text{azul}) = \frac{\text{Prob}[\text{par}\cap \text{azul}]}{\text{Prob}[\text{azul}]}$
# 
# Usando dicha ecuación calcule:
# $\text{Prob}(\text{par}|\text{azul})$
#  

# <span style="color:green">Escriba aquí su respuesta. Discuta con sus compañeros.</span>

# ### <span style="color:#4CC9F0">[Independencia](prob1:ej3)</span>

# Verifique que la siguiente afirmación es verdadera:
# 
# Dos eventos $A$ y $B$ del espacio muestral $\mathcal{M}$ se dicen independientes si
# 
# $$
# \text{Prob}[A| B] = \text{Prob}[A].
# $$

# <span style="color:green">Escriba aquí su respuesta. Discuta con sus compañeros.</span>

# ## <span style="color:#4361EE">[Variables Aleatorias](1:prob2)</span>

# Considere el ejemplo del espacio muestral de los dos dados de seis caras, no cargados. 
# 
# 1. Construya la tabla completa de los posibles resultados de de las funcioens $f$ y $g$.
# 2. Proponga otra variable aleatoria definida sobre el espacio muestral $\mathcal{M}$.
# 
# 

# ::: {admonition} Ayuda
# :class: tip
# Use Python. Construya primero la tabla que representa el espacio muestral, en un tensor $36\times 2$. En otro tensor construya los respectivos valores de la función.
# :::

# <span style="color:green">Escriba aquí su respuesta. Discuta con sus compañeros.</span>

# ### <span style="color:#4CC9F0">[Variable Poisson (Distribución Poisson)](prob2:ej2)</span>

# 1. Revise en cualquier libro de probabilidad y estadística ejemplos de aplicación de la distribución de Poisson. 
# 2. Investigue como calcular probabilidades de la distribución de Poisson con scipy de Python. Suponga que para algún caso $\lambda = 5.3$. Calcule las probabilidades para $ k=0,1,\ldots, 20$. Haga un gráfico de la función de probabilidad con esos datos (obviamente es una aproximación de la función completa).
# 3. Haga sus comentarios.

# <span style="color:green">Escriba aquí su respuesta. Discuta con sus compañeros.</span>

# ### <span style="color:#4CC9F0">[Esperanza de la distribución Poisson](prob2:ej3)</span>

# Verifique que:
# Una variable aleatoria con distribución $\text{Pois}(\lambda)$ tiene esperanza matemática $\lambda$. 

# <span style="color:green">Escriba aquí su respuesta. Discuta con sus compañeros.</span>

# ## <span style="color:#4361EE">[Probabilidad Conjunta y Entropía Cruzada](1:prob3)</span>

# Por favor verifique que si $X\sim \text{Binom}(N,\pi)$, entonces 
# 
# 1. $\mathbb{E}[X]=N\pi$ 
# 2. $\text{Var}[X]=N\pi(1-\pi)$.

# <span style="color:green">Escriba aquí su respuesta. Discuta con sus compañeros.</span>

# ## <span style="color:#4361EE">[Distribuciones de probabilidad continuas](1:prob4)</span>

# ### <span style="color:#4CC9F0">[Variables aleatorias continuas](prob4:ej1)</span>
# 

# Considere los ejemplos dados en la sección {ref}`prob4:ej1`. ¿Puede indicar otros ejemplos?

# <span style="color:green">Escriba aquí su respuesta. Discuta con sus compañeros.</span>

# ### <span style="color:#4CC9F0">[Distribución Normal](prob4:ej3)</span>

# Consulte como calcular usando Python la medida de probabilidad de los siguientes intervalos, si se asume una distribución normal con media 10 y varianza 1.
# 1. $[5,15]$.
# 2. $[0,\infty]$
# 3. $[8,11]$ 

# ::: {admonition} Ayuda
# :class: tip
# $\text{Prob}[a,b] = \text{Prob}[-\infty,b] - \text{Prob}[-\infty,a]$.
# :::

# <span style="color:green">Escriba aquí su respuesta. Discuta con sus compañeros.</span>

# ### <span style="color:#4CC9F0">[Información de distribuciones continuas](prob4:ej4)</span>

# Revise las distribuciones de Laplace y $t$-student utilizadas en la sección {ref}`prob4:ej4`.

# <span style="color:green">Escriba aquí su respuesta. Discuta con sus compañeros.</span>
