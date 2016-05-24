import pylab as pl
import numpy as np
import math

angular_velocity=[0]
angular_velocity_t=[0]
angle=[]
angle_t=[]
t=[0]
dt=0.01*math.pi
angle_0=float(raw_input('enter the initial angle:'))
t_final=20000
l=9.8
q=0.5
force=float(raw_input('enter the amplitude of the driving force:'))
frequency=2./3
angle.append(angle_0)
angle_t.append(angle_0)
g=9.8

i_final=int(t_final/dt)
for i in range(i_final):
 angular_velocity_1=angular_velocity[i]-9.8*(math.sin(angle[i]))*dt/l-q*angular_velocity[i]*dt+force*(math.sin(frequency*t[i]))*dt
 angular_velocity.append(angular_velocity_1)
 angle_1=angle[i]+angular_velocity[i+1]*dt
 if angle_1<-math.pi:
  angle_2=angle_1+2*math.pi
 elif angle_1>math.pi:
  angle_2=angle_1-2*math.pi
 else:
  angle_2=angle_1
 angle.append(angle_2)
 if i%300==0:
  angle_t.append(angle_2)
  angular_velocity_t.append(angular_velocity_1)
 t.append(dt*(1+i))

pl.plot(angle_t,angular_velocity_t,'o')
pl.title('the angle of the pendulum depending on time')
pl.xlabel('radians')
pl.ylabel('angular velocity')
pl.show()
