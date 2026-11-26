"""Exact arithmetic combinatorial checks of shadow counts for truncations of tetrahedra."""
from fractions import Fraction as F
from itertools import combinations, product
from random import Random
from math import acos, pi

def cross3(a,b):
 return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def minus(a,b): return tuple(x-y for x,y in zip(a,b))
def face_normals(vertices):
 out=[]
 for i in range(4):
  inds=[j for j in range(4) if j!=i]
  a,b,c=[vertices[j] for j in inds]
  n=cross3(minus(b,a),minus(c,a))
  if dot(n,minus(vertices[i],a))>0: n=tuple(-x for x in n)
  out.append(n)
 return out

def clipped_points(v,S,t):
 out=[]
 for i in range(4):
  if i in S:
   for j in range(4):
    if j!=i: out.append(tuple((1-t[i])*v[i][k]+t[i]*v[j][k] for k in range(3)))
  else:out.append(v[i])
 return out

def plane_hull_count(vertices,u):
 a,b,c=u
 p=(-b,a,0) if a or b else (1,0,0)
 q=cross3(u,p)
 pts=set((dot(v,p),dot(v,q)) for v in vertices)
 pts=sorted(pts)
 if len(pts)<3: return len(pts)
 def det(o,a,b): return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0])
 lo=[]; hi=[]
 for x in pts:
  while len(lo)>=2 and det(lo[-2],lo[-1],x)<=0:lo.pop()
  lo.append(x)
 for x in pts[::-1]:
  while len(hi)>=2 and det(hi[-2],hi[-1],x)<=0:hi.pop()
  hi.append(x)
 return len(lo)+len(hi)-2

def run():
 rng=Random(925172)
 examples=[[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)],
           [(0,0,0),(5,0,0),(1,7,0),(1,2,9)],
           [(1,2,3),(7,-1,3),(-2,9,2),(2,1,12)],
           [(1,1,0),(-4,-2,3),(0,9,1),(1,-1,11)]]
 count=0; cells=set()
 for ex in examples:
  v=[tuple(F(q) for q in x) for x in ex]
  normals=face_normals(v)
  for iteration in range(400):
   u=tuple(rng.randint(-19,19) for _ in range(3))
   if u==(0,0,0) or any(dot(n,u)==0 for n in normals):continue
   plus={i for i in range(4) if dot(normals[i],u)>0}
   k=len(plus)
   if k not in (1,2,3): raise AssertionError((u,k))
   cells.add(tuple(sorted(plus)))
   t={i:F(rng.randint(1,7),20) for i in range(4)}
   actual=[]
   for mask in range(16):
    S={i for i in range(4) if mask>>i&1}
    verts=clipped_points(v,S,t)
    n=plane_hull_count(verts,u)
    r=len(S)
    if k==2: expected=4+r
    else:
     i=next(iter(plus)) if k==1 else next(i for i in range(4) if i not in plus)
     expected=3+2*(r-(i in S))
    if n!=expected: raise AssertionError((ex,u,mask,k,n,expected))
    actual.append(n);count+=1
   for mask in range(16):
    assert actual[mask]+actual[15-mask]==12
 print('PARTIAL_TETRA_SHADOW_OK',f'exact_hull_comparisons={count}',f'sign_cells={len(cells)}/14')
 assert len(cells)==14
if __name__=='__main__':run()

# Optional stochastic check: labels isolated by one-vertex truncation.
def monte_carlo():
 import numpy as np
 from math import atan2, sqrt
 v=np.array([[0,0,0],[4,0,0],[1,3,0],[1,1,5]],float)
 ns=np.array(face_normals(v.tolist()),float)
 def omega(i):
  rays=[v[j]-v[i] for j in range(4) if j!=i]
  rays=[r/np.linalg.norm(r) for r in rays]
  a,b,c=rays
  return 2*atan2(abs(np.linalg.det(np.stack(rays))),1+np.dot(a,b)+np.dot(b,c)+np.dot(c,a))
 predicted=np.array([omega(i)/(2*pi) for i in range(4)])
 rng=np.random.default_rng(3912)
 U=rng.normal(size=(200000,3)); U/=np.linalg.norm(U,axis=1)[:,None]
 D=U@ns.T
 p=[]
 for i in range(4):
  only_plus=(D[:,i]>0)&np.all(D[:,np.arange(4)!=i]<0,axis=1)
  only_minus=(D[:,i]<0)&np.all(D[:,np.arange(4)!=i]>0,axis=1)
  p.append(np.mean(only_plus|only_minus))
 error=np.max(np.abs(predicted-np.array(p)))
 assert error<.0035,(predicted,p,error)
 print('ANGLE_MASS_MONTE_CARLO_OK',f'max_abs_error={error:.8f}',f'samples={len(U)}')
if __name__=='__main__':monte_carlo()
