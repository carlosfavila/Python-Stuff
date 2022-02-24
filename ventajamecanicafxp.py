# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 10:17:50 2022

@author: CarlosFavila
"""


import matplotlib.pyplot as plt
import numpy as np

def fxp(alpha,us):
    alpha=np.deg2rad(alpha)
    fxp=[]
    for i in (us):
        fxp.append((np.cos(alpha)-i*np.sin(alpha))/(2*(i*np.cos(alpha)+np.sin(alpha))))
    return fxp
    
usm=[0.1,0.2,0.3,0.4,0.5]
us=np.linspace(0.1,0.5,100)

#______________________Caso 1 cuando alpha es 3°
alpha = 3
fxp1=fxp(alpha,us)
fxp1m=fxp(alpha,usm)
plt.plot(us,fxp1,'r-',label=r"$alpha=3°$")
plt.plot(usm,fxp1m,'ok')

#______________________Caso 2 cuando alpha es 5°
alpha = 5
fxp2=fxp(alpha,us)
fxp2m=fxp(alpha,usm)
plt.plot(us,fxp2,'b-',label="$alpha=5°$")
plt.plot(usm,fxp2m,'ok')

#______________________Caso 3 cuando alpha es 8°
alpha = 8
fxp3=fxp(alpha,us)
fxp3m=fxp(alpha,usm)
plt.plot(us,fxp3,'g-',label="$alpha=8°$")
plt.plot(usm,fxp3m,'ok')

#______________________Caso 2 cuando alpha es 10°
alpha = 10
fxp4=fxp(alpha,us)
fxp4m=fxp(alpha,usm)
plt.plot(us,fxp4,'m-',label="$alpha=10°$")
plt.plot(usm,fxp4m,'ok')

plt.title(r"Ventaja mecánica para distintos valores de $\alpha$")
plt.xlabel(r"$\mu_{s}$")
plt.ylabel(r"$\frac{F_x}{P}$ (Ventaja Mecánica)")
plt.legend(loc="best")
plt.grid(True)