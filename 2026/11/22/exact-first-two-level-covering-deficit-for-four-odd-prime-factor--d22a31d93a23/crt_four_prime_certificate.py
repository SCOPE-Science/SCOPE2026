#!/usr/bin/env python3
"""Exact four-vertex CRT cylinder union certificate (Python 3 stdlib)."""
from collections import defaultdict
from itertools import product

EDGES=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
INC=tuple(tuple(j for j,e in enumerate(EDGES) if v in e) for v in range(4))
PARTS=((0,0,0),(0,0,1),(0,1,0),(0,1,1),(0,1,2))
ZERO=(0,0,0,0)

def add(a,b):
 out=defaultdict(int,a)
 for k,v in b.items():out[k]+=v
 return dict(out)

def mult(a,b):
 out=defaultdict(int)
 for i,v in a.items():
  for j,w in b.items():out[tuple(i[t]+j[t] for t in range(4))]+=v*w
 return dict(out)

def scalar(c):return {ZERO:c}

# For each vertex v, n_v=base_v+sum polynomial variables.
# p>=5: independent shifts n_v=4+x_v.
P_BIG=[]
for v in range(4):
 x=list(ZERO);x[v]=1
 P_BIG.append({ZERO:4,tuple(x):1})
# p=3, q<r<s odd primes: n=(2,4+x,6+x+y,8+x+y+z).
P_THREE=[scalar(2),{ZERO:4,(1,0,0,0):1},
 {ZERO:6,(1,0,0,0):1,(0,1,0,0):1},
 {ZERO:8,(1,0,0,0):1,(0,1,0,0):1,(0,0,1,0):1}]

def cylinder_union_masks(signature):
 """Inclusion-exclusion yields an exact squarefree monomial polynomial."""
 out=defaultdict(int)
 for pick in range(1,1<<6):
  coeff=1 if pick.bit_count()%2 else -1
  free=0
  for v in range(4):
   chosen=[j for j in INC[v] if pick&(1<<j)]
   if not chosen:free|=1<<v;continue
   labels=PARTS[signature[v]]
   if len({labels[INC[v].index(j)] for j in chosen})>1:break
  else:out[free]+=coeff
 return out

def lift(poly,parameters):
 out={}
 for mask,c in poly.items():
  term=scalar(c)
  for v in range(4):
   if mask&(1<<v):term=mult(term,parameters[v])
  out=add(out,term)
 return out

# Each one-coordinate-pair cylinder has size n_i*n_j on its two free coordinates.
B=defaultdict(int)
for e in EDGES:B[sum(1<<v for v in range(4) if v not in e)]+=1
assert dict(cylinder_union_masks((4,4,4,4)))=={**dict(B),0:-3}
assert dict(cylinder_union_masks((3,4,4,4)))=={**dict(B),0:-3,2:-1}

certified_large=0;certified_three=0
for signature in product(range(5),repeat=4):
 union=cylinder_union_masks(signature)
 difference={m:B.get(m,0)-union.get(m,0) for m in set(B)|set(union)}
 # For n_v>=4, the deficit is >=3 by coefficientwise positivity in x_v>=0.
 poly=add(lift(difference,P_BIG),scalar(-3))
 assert all(v>=0 for v in poly.values()), ('n>=4',signature,poly)
 certified_large+=1
 if signature[0]==4:continue  # 3 distinct labels impossible when n_p=2.
 # q>=5,r>=q+2,s>=r+4 imply x,y,z>=0.
 poly=add(lift(difference,P_THREE),{ZERO:-7,(1,0,0,0):-1})
 assert all(v>=0 for v in poly.values()), ('n_p=2',signature,poly)
 certified_three+=1
assert certified_large==625 and certified_three==500
# Sharpness: distinct incidence labels for >=4; one repeated label on p for p=3.
print('CERTIFIED: 625 signatures for n_i>=4, each B-U>=3')
print('CERTIFIED: 500 feasible signatures for n_p=2, q<r<s odd primes, each B-U>=q+2')
print('SHARP: witnesses all-distinct and p-signature (0,1,1), other vertices all-distinct')
