import pylab as pl
import numpy as np
import math

y_e=[-5]
x_e=[0]
r_e=[5]
x_j=[5]
y_j=[0]
r_j=[5]
v_ey=[0]
v_ex=[1]
v_jx=[0]
v_jy=[-1]
t=[0]
dt=0.001
m_j=6*10**31
m_e=3*10**31
m_s=5.7*10**26
m_sun=2*10**30

t_final=5

i_final=int(t_final/dt)
for i in range(i_final):
 r_ej=((x_e[i]-x_j[i])**2+(y_e[i]-y_j[i])**2)**(1/2)
 
 v_ex1=v_ex[i]-((4*(math.pi)**2)*(m_j/m_sun)*(x_e[i]-x_j[i])*dt)/(r_ej)**3
 v_ey1=v_ey[i]-((4*(math.pi)**2)*(m_j/m_sun)*(y_e[i]-y_j[i])*dt)/(r_ej)**3
 v_jx1=v_jx[i]-((4*(math.pi)**2)*(m_e/m_sun)*(x_j[i]-x_e[i])*dt)/(r_ej)**3
 v_jy1=v_jy[i]-((4*(math.pi)**2)*(m_e/m_sun)*(y_j[i]-y_e[i])*dt)/(r_ej)**3
 
 
 v_ex.append(v_ex1)
 v_ey.append(v_ey1)
 v_jx.append(v_jx1)
 v_jy.append(v_jy1)

 x_e1=x_e[i]+v_ex[i+1]*dt
 y_e1=y_e[i]+v_ey[i+1]*dt
 x_j1=x_j[i]+v_jx[i+1]*dt
 y_j1=y_j[i]+v_jy[i+1]*dt

 r_e1=((x_e1)**2+(y_e1)**2)**(1/2)
 r_j1=((x_j1)**2+(y_j1)**2)**(1/2)
 
 x_e.append(x_e1)
 y_e.append(y_e1)
 x_j.append(x_j1)
 y_j.append(y_j1)
 r_e.append(r_e1)
 r_j.append(r_j1)
 t.append(dt*(1+i))

plot1=pl.plot(x_e,y_e,color='red',linewidth=0.5,linestyle='-',label='earth')
plot2=pl.plot(x_j,y_j,color='green',linewidth=0.5,linestyle='-',label='sun')
pl.title('the motion of earth and sun')
pl.xlabel('x')
pl.ylabel('y')
pl.legend(loc='upper right')

pl.show()

