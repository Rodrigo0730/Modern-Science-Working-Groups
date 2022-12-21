import numpy as np 
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math
s,r,b=10,31,8/3 #parameters

def dLorenz(XYZo,t): #ODE system
  x,y,z=XYZo
  return [s*y-s*x,r*x-x*z-y,x*y-b*z]

XYZo=[10,7,10] #initial condition
XYZo2 = [10.01, 7.01, 10.01]

t = np.linspace(0, 40, 10000) #tspace

sol = odeint(dLorenz, XYZo, t) #solver
sol1 = odeint(dLorenz, XYZo2, t) #solver
fig=plt.figure() #plot

ax1 = fig.add_subplot(1 , 1 , 1)
ax1.axis('on')
ax1.plot(t, sol[:, 0], 'r',)
ax1.plot(t, sol1[:, 0], 'g',)
ax1.legend(loc='best')
ax1.grid()
"""
ax2 = fig.add_subplot(2,2,2)
ax2.plot(t, sol[:, 1], 'g', label='y(t)')
ax2.legend(loc='best')
ax2.grid()

ax3 = fig.add_subplot(2,2,3)
ax3.plot(t, sol[:, 2], 'b', label='z(t)')
ax3.legend(loc='best')
ax3.grid()

ax = fig.add_subplot(2,2,4,projection="3d")
ax.plot(*sol.T, lw = 0.5)
ax.grid()
"""
plt.show()

pene = plt.figure()

ax = pene.add_subplot(1,1,1,projection="3d")
ax.plot(*sol.T, lw = 0.5, label="\u03C3 = 10, b=8/3, r=31")
ax.legend(loc="best")
ax.grid()

plt.show()


