import pylab as pl
import numpy as np
import math

x=[]
y=[]
z=[]
t=[0]
dt=0.0001
x_0=float(raw_input('enter the initial x:'))
y_0=float(raw_input('enter the initial y:'))
z_0=float(raw_input('enter the initial z:'))
r=float(raw_input('enter the initial r:'))
a=10
b=8./3
t_final=50
l=9.8
q=0.5
x.append(x_0)
y.append(y_0)
z.append(z_0)

i_final=int(t_final/dt)
for i in range(i_final):
 x_1=x[i]+a*(y[i]-x[i])*dt
 y_1=y[i]+(-x[i]*z[i]+r*x[i]-y[i])*dt
 z_1=z[i]+(x[i]*y[i]-b*z[i])*dt
 x.append(x_1)
 y.append(y_1)
 z.append(z_1)
 t.append(dt*(1+i))

pl.plot(x,z,'r')
pl.title('phase space plot: z versus x')
pl.xlabel('x')
pl.ylabel('z')
pl.show()
