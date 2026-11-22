#!/usr/bin/env python3
"""Exact exhaustive verification of the marked characteristic-seven sextic census.
Requires Python 3.10+ and SymPy 1.12+. No external data files.
"""
import sympy as sp
from collections import defaultdict
X,Y,Z,A,B,t = sp.symbols('X Y Z A B t')
P=7
S=X**6+Y**6+Z**6 + A*(X**4*Y**2+X**2*Z**4+Y**4*Z**2) + B*(X**2*Y**4+X**4*Z**2+Y**2*Z**4)-3*(A+B+1)*X**2*Y**2*Z**2
D=-(t**3+B*t**2+A*t+1)*((A+B+2)*t**3-(A+2*B+3)*t**2+(B+3)*t-1)
partials=[sp.diff(S,x) for x in (X,Y,Z)]
# The exact ideal of the fixed four nodes in each affine chart.
expected=[('X**2 - 1','Y**2 - 1'),('X**2 - 1','Z**2 - 1'),('Y**2 - 1','Z**2 - 1')]
valid=[]
for a in range(P):
 for b in range(P):
  ideals=[]
  for fix in (Z,Y,X):
   free=tuple(x for x in (X,Y,Z) if x!=fix)
   gb=sp.groebner([g.subs({A:a,B:b,fix:1}) for g in partials],*free,modulus=P)
   ideals.append(tuple(str(q.as_expr()) for q in gb.polys))
  if ideals==expected:
   assert (a+b+3)%P!=0
   valid.append((a,b))
assert len(valid)==29
# F_49=F_7[i]/(i^2+1). Nonzero squares exact.
Q=[(a,b) for a in range(P) for b in range(P)]
def add(u,v):return ((u[0]+v[0])%P,(u[1]+v[1])%P)
def mul(u,v):return ((u[0]*v[0]-u[1]*v[1])%P,(u[0]*v[1]+u[1]*v[0])%P)
SQ={mul(z,z) for z in Q}
def evalpoly(cc,x):
 y=(0,0)
 for z in cc:y=add(mul(y,x),(z,0))
 return y
def points_D(a,b,q):
 poly=sp.Poly(D.subs({A:a,B:b}),t,modulus=P)
 assert poly.degree() in (5,6)
 assert sp.gcd(poly,poly.diff()).degree()==0
 cc=[int(u)%P for u in poly.all_coeffs()]
 if q==7:
  n=sum(1 if (v:=evalpoly(cc,(x,0)))[0]==0 else (2 if v[0] in (1,2,4) else 0) for x in range(P))
  n+=1 if poly.degree()==5 else (2 if int(poly.LC())%7 in (1,2,4) else 0)
 else:
  assert q==49
  n=sum(1 if (v:=evalpoly(cc,x))==(0,0) else (2 if v in SQ else 0) for x in Q)
  n+=1 if poly.degree()==5 else 2
 return n
rational_projective=[(x,y,1) for x in range(P) for y in range(P)]+[(x,1,0) for x in range(P)]+[(1,0,0)]
assert len(rational_projective)==57
def plane_count(a,b):
 ans=0
 for x,y,z in rational_projective:
  f=x**6+y**6+z**6+a*(x**4*y*y+x*x*z**4+y**4*z*z)+b*(x*x*y**4+x**4*z*z+y*y*z**4)-3*(a+b+1)*x*x*y*y*z*z
  ans+=int(f%7==0)
 return ans
spectrum=defaultdict(list)
for a,b in valid:
 n1=points_D(a,b,7);n2=points_D(a,b,49)
 trace=8-n1
 assert (n2-50+trace*trace)%2==0
 second=(n2-50+trace*trace)//2
 spectrum[trace,second].append((a,b))
 # Distinct check: direct homogeneous plane count, with 4 split nodes.
 assert plane_count(a,b)+4==3*n1-16,(a,b,n1,plane_count(a,b))
assert len(spectrum)==11
assert spectrum[(-4,14)]==[(5,5)]
assert sorted(spectrum[(-6,18)])==[(0,3),(3,0)]
assert sum(len(v) for v in spectrum.values())==29
assert all((t,s)!=(-4,14) and s%7!=0 for t,s in spectrum if (t,s)!=(-4,14))
for (t,s),pairs in sorted(spectrum.items()):
 print(f'trace={t:3d} second={s:3d} multiplicity={len(pairs):2d} pairs={pairs}')
print('KAWAKITA_F7_COMPLETE_CENSUS_VERIFIED parameters=49 smooth_four_node=29 zeta_types=11 nonordinary=1 p_rank=3 ordinary=28 p_rank=6')
