import pylab as pl
import numpy as np
import math

x_e=[1]
y_e=[0]
r_e=[1]
x_j=[5.2]
y_j=[0]
r_j=[5.2]
x_s=[9.54]
y_s=[0]
r_s=[9.54]
v_ex=[0]
v_ey=[2*math.pi]
v_jx=[0]
v_jy=[(2*math.pi)/((5.2)**1/2)]
v_sx=[1]
v_sy=[0]
t=[0]
dt=0.001
m_j=1.9*10**28
m_e=6*10**24
m_s=2*10**30
m_sun=2*10**30

t_final=20

i_final=int(t_final/dt)
for i in range(i_final):
 r_ej=((x_e[i]-x_j[i])**2+(y_e[i]-y_j[i])**2)**(1/2)
 r_es=((x_e[i]-x_s[i])**2+(y_e[i]-y_s[i])**2)**(1/2)
 r_js=((x_s[i]-x_j[i])**2+(y_s[i]-y_j[i])**2)**(1/2)
 
 v_ex1=v_ex[i]-((4*(math.pi)**2)*(m_j/m_sun)*(x_e[i]-x_j[i])*dt)/(r_ej)**3-((4*(math.pi)**2)*(m_s/m_sun)*(x_e[i]-x_s[i])*dt)/(r_es)**3
 v_ey1=v_ey[i]-((4*(math.pi)**2)*(m_j/m_sun)*(y_e[i]-y_j[i])*dt)/(r_ej)**3-((4*(math.pi)**2)*(m_s/m_sun)*(y_e[i]-y_s[i])*dt)/(r_es)**3
 v_jx1=v_jx[i]-((4*(math.pi)**2)*(m_e/m_sun)*(x_j[i]-x_e[i])*dt)/(r_ej)**3-((4*(math.pi)**2)*(m_s/m_sun)*(x_j[i]-x_s[i])*dt)/(r_js)**3
 v_jy1=v_jy[i]-((4*(math.pi)**2)*(m_e/m_sun)*(y_j[i]-y_e[i])*dt)/(r_ej)**3-((4*(math.pi)**2)*(m_s/m_sun)*(y_j[i]-y_s[i])*dt)/(r_js)**3
 v_sx1=v_sx[i]-((4*(math.pi)**2)*(m_e/m_sun)*(x_s[i]-x_e[i])*dt)/(r_es)**3-((4*(math.pi)**2)*(m_j/m_sun)*(x_s[i]-x_j[i])*dt)/(r_js)**3
 v_sy1=v_sy[i]-((4*(math.pi)**2)*(m_e/m_sun)*(y_s[i]-y_e[i])*dt)/(r_es)**3-((4*(math.pi)**2)*(m_j/m_sun)*(y_s[i]-y_j[i])*dt)/(r_js)**3
 
 v_ex.append(v_ex1)
 v_ey.append(v_ey1)
 v_jx.append(v_jx1)
 v_jy.append(v_jy1)
 v_sx.append(v_sx1)
 v_sy.append(v_sy1)
 
 x_e1=x_e[i]+v_ex[i+1]*dt
 y_e1=y_e[i]+v_ey[i+1]*dt
 x_j1=x_j[i]+v_jx[i+1]*dt
 y_j1=y_j[i]+v_jy[i+1]*dt
 x_s1=x_s[i]+v_sx[i+1]*dt
 y_s1=y_s[i]+v_sy[i+1]*dt
 
 r_e1=((x_e1)**2+(y_e1)**2)**(1/2)
 r_j1=((x_j1)**2+(y_j1)**2)**(1/2)
 r_s1=((x_s1)**2+(y_s1)**2)**(1/2)
 
 x_e.append(x_e1)
 y_e.append(y_e1)
 x_j.append(x_j1)
 y_j.append(y_j1)
 x_s.append(x_s1)
 y_s.append(y_s1)
 r_e.append(r_e1)
 r_j.append(r_j1)
 r_s.append(r_s1)
 t.append(dt*(1+i))

plot1=pl.plot(x_e,y_e,color='red',linewidth=1,linestyle='-',label='earth')
plot2=pl.plot(x_j,y_j,color='green',linewidth=1,linestyle='-',label='jupiter')
plot3=pl.plot(x_s,y_s,color='blue',linewidth=1,linestyle='-',label='sun')
pl.title('earth,jupiter and saturn orbiting around the sun')
pl.xlabel('x')
pl.ylabel('y')
pl.legend(loc='upper right')

pl.show()

