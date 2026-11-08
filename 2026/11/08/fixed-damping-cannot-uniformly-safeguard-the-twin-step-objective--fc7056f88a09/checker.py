"""Exact-rational check of the paired-gradient ray-intersection identities.
All asserted results are finite certificates supplementary to the analytic proof.
Run: python3 checker.py
"""
from fractions import Fraction as F
from math import sqrt

def phi(v,k):
    return (v[0]**2 + k*v[1]**2)/2

def vec_add(a,b): return tuple(a[i]+b[i] for i in range(2))
def vec_sub(a,b): return tuple(a[i]-b[i] for i in range(2))
def vec_mul(t,a): return tuple(t*v for v in a)
def grad(a,k): return (a[0],k*a[1])

def trial(k,e,eta):
    x=(F(2),F(2)); z=(F(1),F(1)+e)
    t=(e*k+e+k-1)/(2*e*k)
    s=(e+k-1)/(e*k)
    w=vec_sub(x,vec_mul(t,grad(x,k)))
    assert t>0 and s>0
    assert w==vec_sub(z,vec_mul(s,grad(z,k)))
    want=((k-1)*(e-1)/(e*k), -(k-1)*(e+1)/e)
    assert w==want
    assert grad(x,k)[0]*grad(z,k)[1] - grad(x,k)[1]*grad(z,k)[0] == 2*k*e
    xd=vec_add(vec_mul(1-eta,x),vec_mul(eta,w))
    zd=vec_add(vec_mul(1-eta,z),vec_mul(eta,w))
    assert vec_sub(xd,zd)==vec_mul(1-eta,vec_sub(x,z))
    return phi(xd,k),phi(zd,k),phi(x,k),phi(z,k)

n=0
for k in (F(5,4),F(3,2),F(2),F(3),F(10)):
 for e in (F(1,10),F(1,50),F(1,100),F(1,1000)):
  for eta in (F(1),F(1,2),F(1,10),F(1,100),e*F(1,2),e*F(3,2),e*F(4)):
   if eta>1: continue
   trial(k,e,eta);n+=1
# Symbolic-scaled limit verified using exact rational expressions at k=2.
# With eta=c*e and e->0, x_eta -> (2-c/2,2-c), z_eta -> (1-c/2,1-c).
for c in (F(1,2),F(1),F(3,2),F(2),F(3),F(4)):
 for e in (F(1,100),F(1,1000),F(1,10000)):
  if c*e>1: continue
  xx,zz,_,_=trial(F(2),e,c*e)
  X=F(6)-5*c+F(9,8)*c*c
  Z=F(3,2)-F(5,2)*c+F(9,8)*c*c
  assert abs(float(xx-X))<100*float(e)
  assert abs(float(zz-Z))<100*float(e)
  n+=1
# Necessary and sufficient limiting threshold: L(c)=min(X,Z).
cs=(20+2*sqrt(19))/9
for c in (0.01,0.5,1,1.8,2,2.5,3,3.19,3.20,4,20):
 X=6-5*c+9*c*c/8
 Z=1.5-2.5*c+9*c*c/8
 if c<cs: assert min(X,Z)<1.5
 if c>cs: assert min(X,Z)>1.5
 n+=1
# Fixed damping fails at a prescribed curvature ratio 2 and bounded starts.
for eta in (F(1,100),F(1,10),F(1,2),F(1)):
 for D in (100000,1000000,10000000):
  xx,zz,fx,fz=trial(F(2),F(1,D),eta)
  assert min(xx,zz)>max(fx,fz)
  n+=1
print('PASS',n,'exact-rational and threshold checks')
