# -*- coding: utf-8 -*-
"""
Original file is located at
    https://colab.research.google.com/drive/17Dx1yhdjRVXPIbJ-0FxP6GTo0B-tiB3j

## Construye la gráfica de ***$\sum_{k=1}^{10} cos(2 \pi k t)$***
Punto 4 de la Práctca [P01: Señales en Tiempo Continuo](https://carlosfavila.github.io/PracticasASyS/ASySPracP01CarlosJosafathLopezFavila/ASySPracP01CarlosJosafathLopezFavila.html#60)
"""

import  matplotlib.pyplot  as  plt 
import  numpy  as  np 
import  sympy  as  sp 

t = sp.Symbol ( 't' ) #convierte la letra 't' en simbólica
y = [] 
for  k  in range( 1 , 11 ):  
  y.append( sp.cos ( 2 * np. pi * k * t )) 
  x = np.sum( y ) #función x(t) con 't' simbólica


xt = [] #lista que contendrá con valores de la función x(t) en el dominio de -2 a 2
r = np.linspace( -2 , 2, 1000) 

for  i in  r : 
  #sustituye cada valor que toma i en cada 't' de la expresión almacenada en x
  l=x.subs( t, i) 
  xt.append(l) 

def config(row, column):
  # establece la columna x al centro
  axs[row,column].spines[ 'left' ].set_position( 'center' ) 
  # apaga la columna derecha 
  axs[row,column].spines[ 'right' ].set_color( 'none' ) 
  # establece los ejes de la columna y
  axs[row,column].yaxis.tick_left() 
  # quita la linea superior, y la inferior la posiciona en el centro
  axs[row,column].spines['top'].set_color( 'none' )
  axs[row,column].spines[ 'bottom' ].set_position( 'zero' ) 
  # apaga la espina superior / ticks 
  axs[row,column].spines[ 'top' ].set_color( 'none' ) 
  axs[row,column].xaxis.tick_bottom() 
  # Define el estilo de la rejilla 
  axs[row,column].grid ( True ,  linestyle = '-' )


fig,axs = plt.subplots(2,2) 

#______________________________ Subplot 1 ______________________________________ 

axs[0,0].plot( r ,  xt , 'g' ) 
axs[0,0].set( xlabel = '. t',ylabel ='x(t)', 
             title = 't de -2 a 2' , xlim = ( -2 , 2 )) 

config(0,0)

# Define la posición del Subplot
g = axs[0,0].get_position() 
axs[0,0].set_position([ g.x0 ,  g.y0 ,  g.width * 2.5 ,  g.height * 2 ]) 

#______________________________ Subplot 2 ______________________________________ 

axs[0,1].plot( r, xt, 'r' ) 
axs[0,1].set( xlabel ='. t ' ,  ylabel = ' x (t) ' ,  
        title = ' t de -0.2 a 0.2 ' ,  xlim = ( -0.2 , 0.2 )) 

config(0,1)

# Define la posición del Subplot
g = axs[0,1].get_position () 
axs[0,1].set_position([ g.x0+0.5 ,  g.y0 ,  g.width * 2.5 ,  g.height * 2 ])

#______________________________ Subplot 3 ______________________________________ 
 
axs[1,0].plot(r ,  xt , 'k') 
axs[1,0].set( xlabel = '. t' ,  ylabel = 'x (t)' ,  
        title = 't de 0.3 a 0.7' , xlim = ( 0.3 , 0.7 ))   

config(1,0)

# Define la posición del subplot
g=axs[1,0].get_position() 
axs[1,0].set_position([ g.x0 ,  g.y0-0.5 ,  g.width*2.5 ,  g.height*2 ])
                                          
#______________________________ Subplot 4 ______________________________________ 

axs[1,1].plot( r, xt , 'b' )  
axs[1,1].set(xlabel = '. t' ,  ylabel = 'x (t)' ,  
        title = 't de 0 a 1' , xlim = ( 0 , 1 ))  

config(1,1)

# Define la posición del Subplot
g=axs[1,1].get_position() 
axs[1,1].set_position([g.x0+0.5, g.y0-0.5, g.width*2.5, g.height*2])