"""Algebra and numerical checks for eventual conditional-edge sorting."""
import sympy as s
w,x,r=s.symbols('w x r', real=True)
p0,p1,p2,q0,q1,q2=s.symbols('p0 p1 p2 q0 q1 q2',positive=True)
c1,c2,c3=s.symbols('c1 c2 c3',real=True)
D=1-w;m=D*x*(1-r);n=D*(1-x)*r
v1=2*w*(q0-(p0+q0)*c1)+2*n*(c2-c1)
v2=2*w*(q1-(p1+q1)*c2)+m*(c1-c2)+n*(c3-c2)
v3=2*w*(q2-(p2+q2)*c3)+2*m*(c2-c3)
expr1=2*w*((q1-q0)*(1-c1)+(p0-p1)*c1)-(2*w*(p1+q1)+m+2*n)*(c2-c1)+n*(c3-c2)
expr2=2*w*((q2-q1)*(1-c2)+(p1-p2)*c2)-(2*w*(p2+q2)+2*m+n)*(c3-c2)+m*(c2-c1)
assert s.simplify(v2-v1-expr1)==0
assert s.simplify(v3-v2-expr2)==0
print('PASS symbolic difference equations')
# Adversarial time varying strategy fractions and imitation probabilities; auxiliary, not proof.
try:
 from scipy.integrate import solve_ivp
 import numpy as np
 wp=.2;p=(.85,.5,.1);q=(.1,.4,.85)
 delta=min(q[1]-q[0],p[0]-p[1],q[2]-q[1],p[1]-p[2]);
 mu=2*wp*min(p[1]+q[1],p[2]+q[2]); L=2*wp*max(p[1]+q[1],p[2]+q[2])+(1-wp)
 T=max(np.log(2)/L,np.log(2*L/(wp*delta))/mu)
 def fun(t,z):
  xx=.5+.48*np.sin(1.13*t); rr=.5+.48*np.sin(3.1*t+.6)
  m=(1-wp)*xx*(1-rr);n=(1-wp)*(1-xx)*rr
  c1,c2,c3=z
  return [2*wp*(q[0]-(p[0]+q[0])*c1)+2*n*(c2-c1), 2*wp*(q[1]-(p[1]+q[1])*c2)+m*(c1-c2)+n*(c3-c2), 2*wp*(q[2]-(p[2]+q[2])*c3)+2*m*(c2-c3)]
 bound=wp*delta/(2*L)
 for initial in ([1,0,0],[1,1,0],[0,1,0],[.97,.02,.01]):
  sol=solve_ivp(fun,(0,T+12),initial,rtol=1e-10,atol=1e-12,dense_output=True)
  for t in np.linspace(T,T+12,100):
   cc=sol.sol(t)
   assert min(cc[1]-cc[0],cc[2]-cc[1])>=bound-1e-8
 print('PASS numerical stress check',T,bound)
except ImportError:pass
