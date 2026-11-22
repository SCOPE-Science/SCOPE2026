"""Standalone exact-arithmetic finite diagnostics for a sharp ℓ1 median hull theorem.
These checks are not substitutes for the mathematical proof.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

def norm(v): return sum(map(abs,v),F(0))
def median(x,y): return [sorted((F(0),a,b))[1] for a,b in zip(x,y)]
def intersection(L,M):
 a,b,c=L;d,e,f=M;det=a*e-b*d
 if not det:return None
 return ((c*e-b*f)/det,(a*f-c*d)/det)
def distance(x,y):
 m=median(x,y); lines=[(F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(1),F(1),F(1))]+[(a,b,z) for a,b,z in zip(x,y,m)]
 vertices=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1))]
 for i,l in enumerate(lines):
  for z in lines[:i]:
   t=intersection(l,z)
   if t is not None and t[0]>=0 and t[1]>=0 and sum(t)<=1:vertices.append(t)
 return min(sum((abs(z-a*p-b*q) for z,a,b in zip(m,x,y)),F(0)) for p,q in vertices)
def classification(x,y):
 m=median(x,y)
 if norm(x)!=1 or norm(y)!=1:return False
 S=[i for i,v in enumerate(m) if v]
 if norm(m)!=F(1,2):return False
 if any(x[i]!=y[i] for i in S):return False
 if any(x[i] and y[i] for i in range(len(x)) if i not in S):return False
 return norm([x[i] for i in range(len(x)) if i not in S])==F(1,2)==norm([y[i] for i in range(len(y)) if i not in S])

if __name__=='__main__':
 rng=Random(271828);assertions=0
 V=[]
 for v in product(range(-2,3),repeat=3):
  if any(v):
   a=norm(v);V.append([F(z,a) for z in v])
 for _ in range(1500):
  x,y=rng.choice(V),rng.choice(V)
  d=distance(x,y); m=median(x,y)
  assert d<=F(1,2);assertions+=1
  assert (d==F(1,2))==classification(x,y);assertions+=1
  a=sum((min(abs(s),abs(t)) for s,t in zip(x,y)),F(0))
  assert d<=min(a,1-a);assertions+=1
 for d in range(3,8):
  x=[F(1,2),F(1,2),F(0)]+[F(0)]*(d-3)
  y=[F(1,2),F(0),F(1,2)]+[F(0)]*(d-3)
  assert distance(x,y)==F(1,2);assertions+=1
  assert classification(x,y);assertions+=1
 print('TORRICELLI_L1_RIGIDITY_EXACT_CHECK_OK',assertions)
