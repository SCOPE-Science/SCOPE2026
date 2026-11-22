import sympy as s
from math import sqrt
import numpy as np
r=s.sqrt(3)
u=[s.Matrix([1,0]),s.Matrix([s.Rational(1,2),r/2]),s.Matrix([-s.Rational(1,2),r/2])]
Q=[x*x.T for x in u]
q=[s.Matrix([x[0,0],x[1,1],s.sqrt(2)*x[0,1]]) for x in Q]
assert sum(Q,s.zeros(2))==s.Rational(3,2)*s.eye(2)
G=s.Matrix.hstack(*q).T*s.Matrix.hstack(*q)
assert G==s.Rational(3,4)*s.eye(3)+s.Rational(1,4)*s.ones(3)
assert sorted((s.Matrix.hstack(*q)*s.Matrix.hstack(*q).T/3).eigenvals().keys())==[s.Rational(1,4),s.Rational(1,2)]
h=s.Matrix([1/s.sqrt(2),1/s.sqrt(2),0])
P=[x*x.T for x in q]
for n in range(2,10):
 k=n//2
 if n%2==0:
  D=[s.eye(3)]*k+[s.zeros(3)]*k
 else:
  D=[s.eye(3)]*(k-1)+[s.zeros(3)]*(k-1)+P
 e=s.Matrix.vstack(*[h/s.sqrt(n) for _ in range(n)])
 De=s.Matrix.vstack(*[D[i]*h/s.sqrt(n) for i in range(n)])
 z=2*De-e
 assert s.simplify(e.dot(z))==0
 assert s.simplify(z.dot(z))==1
 assert all(s.simplify(sum(z[3*i+j] for i in range(n)))==0 for j in range(3))
 kap=n+1
 delta=e/kap+z
 Ddelta=s.Matrix.vstack(*[D[i]*delta[3*i:3*i+3,0] for i in range(n)])
 mass=s.kronecker_product(s.eye(n)+s.ones(n),s.eye(3))
 gain2=s.simplify((Ddelta.T*mass*Ddelta)[0]/(delta.T*mass*delta)[0]); expected=s.Rational((n+2)**2,4*(n+1))
 assert gain2==expected, (n,gain2,expected)
 print(f'spatial_dim={n-1} sharp_gain_squared={gain2} sharp_gain={s.sqrt(gain2)}')
# Real finite 2x2 spectral clip finite-difference ratio for triangle n=3
u0=[np.array([1.,0.]),np.array([.5,np.sqrt(3)/2]),np.array([-.5,np.sqrt(3)/2])]
h=np.eye(2)/np.sqrt(2)
proj=[]
for ui in u0:proj.append(np.outer(ui,ui))
e=np.array([h]*3)
De=np.array([np.trace(h@pi)*pi for pi in proj])/np.sqrt(3)
e=e/np.sqrt(3)
z=2*De-e
delta=e/4+z
M=np.eye(3)+np.ones((3,3))
def massnorm(v):return np.sqrt(np.einsum('ij,iab,jab->',M,v,v))
def clip(v):
 lam,U=np.linalg.eigh(v)
 return (U*np.clip(lam,0,1))@U.T
for L in [10,100,1000]:
 centers=np.array([.5*pi-L*(np.eye(2)-pi) for pi in proj])
 eps=1e-5
 v=np.array([clip(a+eps*b)-clip(a) for a,b in zip(centers,delta)])/eps
 print('finite_L',L,'gain',massnorm(v)/massnorm(delta))
assert abs(massnorm(v)/massnorm(delta)-1.25)<1e-4
print('all exact and finite sensitivity tests passed')
