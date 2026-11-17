"""Independent direct geometric check of the strict-obtuse small-perimeter law."""
import numpy as np
from scipy.integrate import quad
from scipy.stats import qmc
import math
A=2*math.pi/3
b=c=1.
a=math.sqrt(2-2*math.cos(A))
h=math.sin(A)/a
p=h/c;q=h/b
kappa=lambda k:math.sqrt(1+k*k-2*k*math.cos(A))-p-q*k
I,err=quad(lambda k:kappa(k)**-2,0,math.inf,epsabs=1.e-12,epsrel=1.e-12)
C=8*math.sqrt(h)*I/(15*a*b*c)
print('angle_deg',120,'altitude',h,'integral',I,'asymptotic_coefficient',C)
for t in (0.025,0.010,0.004,0.0016):
 Umax=2.5*t; Wmax=2*math.sqrt(h*t)
 pts=qmc.Sobol(d=3,scramble=True,seed=12345).random_base2(20)
 u=Umax*pts[:,0];v=Umax*pts[:,1];w=Wmax*(2*pts[:,2]-1)
 xB=-math.sqrt(1-p*p);xC=-xB
 L=np.sqrt((h-p*u)**2+(w-xB*u)**2)+np.sqrt((h-q*v)**2+(w-xC*v)**2)+np.sqrt(u*u+v*v-2*u*v*math.cos(A))
 prob=(u.size and (L<2*h+t).mean())*(Umax**2*2*Wmax)/(a*b*c)
 print('t=',t,'direct_prob=',prob,'prob/t^2.5=',prob/t**2.5,'relative=',(prob/t**2.5)/C)
