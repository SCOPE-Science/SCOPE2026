"""Independent algebraic and convex-section checks for octahedral intersection-body theorem.
Requires SymPy and NumPy. Tests support, not a substitute for the analytic proof.
"""
import itertools
import math
import random
import sympy as sp
import numpy as np

x,y,z,t=sp.symbols('x y z t')
V=[x,y,z]
D=(x+y)*(x+z)*(y+z)
S=x*y+x*z+y*z
F=sp.expand(D-2*t*S)
checks=0

def require(test):
 global checks
 assert test
 checks+=1

q=[t-(x+y+z)/2,x/2,y/2,z/2]
cayley=-8*sum(sp.prod(q[j] for j in range(4) if j!=k) for k in range(4))
require(sp.expand(F-cayley)==0)
# Rational Laplace-density identity for pairwise distinct positive magnitudes.
laplace_sum=sum(V[i]**3/sp.prod(V[i]**2-V[j]**2 for j in range(3) if j!=i) for i in range(3))
require(sp.factor(laplace_sum-S/D)==0)

sign_polys={}
for signs in itertools.product((-1,1),repeat=3):
 subs={V[i]:signs[i]*V[i] for i in range(3)}
 f=sp.expand(F.subs(subs))
 sign_polys[signs]=f
 require(len(sp.factor_list(f)[1])==1)
 require(sp.Poly(f,x,y,z,t).total_degree()==3)
 for axis in range(3):
  p={x:0,y:0,z:0,t:1}
  p[V[axis]]=2*signs[axis]
  require(f.subs(p)==0)
require(len(set(map(str,sign_polys.values())))==8)
# Four ordinary nodes (one origin and three axis endpoints) for each affine octant cubic.
for signs,f in sign_polys.items():
 f=f.subs(t,1)
 for point in [(0,0,0)]+[tuple(2*signs[i] if i==j else 0 for i in range(3)) for j in range(3)]:
  p=dict(zip(V,point))
  require(f.subs(p)==0)
  require(all(sp.diff(f,v).subs(p)==0 for v in V))
  require(sp.hessian(f,V).det().subs(p)!=0)

def section_area(u):
 u=np.asarray(u,dtype=float)
 vertices=[]
 for i in range(3):
  for j in range(i+1,3):
   for si in (-1,1):
    for sj in (-1,1):
     v=np.eye(3)[i]*si
     w=np.eye(3)[j]*sj
     p=float(np.dot(u,v)); q=float(np.dot(u,w))
     if p*q < 0:
      vertices.append((q*v-p*w)/(q-p))
 for i in range(3):
  for si in (-1,1):
   v=np.eye(3)[i]*si
   if abs(np.dot(u,v))<1e-12:
    vertices.append(v)
 uniq=[]
 for p in vertices:
  if not any(np.linalg.norm(p-v)<1e-10 for v in uniq):uniq.append(p)
 n=u/np.linalg.norm(u)
 basis=np.eye(3)[int(np.argmin(abs(n)))]
 a=np.cross(n,basis); a=a/np.linalg.norm(a)
 b=np.cross(n,a)
 points=[(float(np.dot(v,a)),float(np.dot(v,b))) for v in uniq]
 points.sort(key=lambda p:math.atan2(p[1],p[0]))
 return abs(sum(p[0]*q[1]-q[0]*p[1] for p,q in zip(points,points[1:]+points[:1])))/2

def claimed(u):
 a,b,c=map(abs,u)
 return 2*np.linalg.norm(u)*(a*b+a*c+b*c)/((a+b)*(a+c)*(b+c))

rng=random.Random(801)
for i in range(160):
 u=[rng.uniform(-3,3) for _ in range(3)]
 actual=section_area(u)
 require(abs(actual-claimed(u)) < 1e-10*max(1,actual))
for u in [(1,0,0),(0,1,1),(1,1,1),(1,2,0),(-3,2,1)]:
 a,b,c=map(abs,u)
 actual=section_area(u)
 if (a+b)*(a+c)*(b+c):require(abs(actual-claimed(u))<1e-11)
 else:require(abs(actual-2.)<1e-11)
# Each orthant contains a real smooth 2D boundary patch.
for signs,f in sign_polys.items():
 p={V[i]:sp.Rational(3,4)*signs[i] for i in range(3)}
 p[t]=1
 require(f.subs(p)==0)
 require(any(sp.diff(f,v).subs(p)!=0 for v in V))
print('PASS',checks,'checks: eight distinct irreducible Cayley cubics, node tests, rational Laplace identity, polygon-section independent geometry')
