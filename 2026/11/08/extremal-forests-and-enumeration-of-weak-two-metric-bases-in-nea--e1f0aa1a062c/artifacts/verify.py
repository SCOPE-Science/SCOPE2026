"""Exact coefficient arithmetic and independent direct distance checks for labelled rook-graph bases."""
from collections import defaultdict
from fractions import Fraction
from math import factorial, ceil
from itertools import combinations

T3={(1,2):Fraction(1,2),(2,1):Fraction(1,2)}
T4={(3,1):Fraction(1,6),(1,3):Fraction(1,6),(2,2):Fraction(1)}
T5={(4,1):Fraction(1,24),(1,4):Fraction(1,24),(2,3):Fraction(1),(3,2):Fraction(1)}

def mul(P,Q,n,m):
 R=defaultdict(Fraction)
 for (i,j),a in P.items():
  for (k,l),b in Q.items():
   if i+k<=n and j+l<=m:R[(i+k,j+l)]+=a*b
 return dict(R)

def power(P,t,n,m):
 R={(0,0):Fraction(1)}
 for _ in range(t):R=mul(R,P,n,m)
 return R

def count(n,m):
 assert 8<=n<=m<=2*n-5
 q,r=divmod(n+m,3)
 if r==0:v=power(T3,q,n,m).get((n,m),Fraction())/factorial(q)
 elif r==1:v=mul(power(T3,q-1,n,m),T4,n,m).get((n,m),Fraction())/factorial(q-1)
 else:
  v=mul(power(T3,q-1,n,m),T5,n,m).get((n,m),Fraction())/factorial(q-1)
  v+=mul(mul(power(T3,q-2,n,m),T4,n,m),T4,n,m).get((n,m),Fraction())/(2*factorial(q-2))
 answer=v*factorial(n)*factorial(m)
 assert answer.denominator==1
 return int(answer)

def representative(n,m):
 """Build q disjoint small trees with sides exactly n,m."""
 q,r=divmod(n+m,3)
 if r==0:
  a=(2*m-n)//3;b=q-a
  cores=[(1,2)]*a+[(2,1)]*b
 elif r==1:
  a=2*q-n;b=n-q-1
  cores=[(2,2)]+[(1,2)]*a+[(2,1)]*b
 else:
  a=2*q-n;b=n-q-1
  cores=[(2,3)]+[(1,2)]*a+[(2,1)]*b
 assert len(cores)==q and sum(x for x,y in cores)==n and sum(y for x,y in cores)==m
 E=[];i=j=0
 for a,b in cores:
  # tree: row 0 attached to all columns, extra rows attached to col 0
  for jj in range(b):E.append((i,j+jj))
  for ii in range(1,a):E.append((i+ii,j))
  i+=a;j+=b
 assert len(E)==ceil(2*(n+m)/3)
 return E

def direct_weak_two(n,m,edges):
 for (i,j),(ii,jj) in combinations(((a,b) for a in range(n) for b in range(m)),2):
  score=sum(abs(int(i!=a)+int(j!=b)-int(ii!=a)-int(jj!=b)) for a,b in edges)
  if score<2:return False
 return True

expected={(8,8):31046400,(8,9):1079038800,(8,10):47628000,(9,9):57153600,(9,10):4286520000,(9,11):184048880400}
for nm,value in expected.items():
 assert count(*nm)==value,(nm,count(*nm),value)
 print('EGF_COEFFICIENT_OK',*nm,value)
for n in range(8,17):
 for m in range(n,2*n-4):
  edges=representative(n,m)
  assert direct_weak_two(n,m,edges)
  print('SAMPLE_BASIS_OK',n,m,len(edges))
print('VERIFY_OK')
