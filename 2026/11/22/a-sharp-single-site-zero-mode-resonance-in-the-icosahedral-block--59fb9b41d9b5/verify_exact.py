#!/usr/bin/env python3
"""Exact characteristic polynomial and symbolic-minor certificate for the icosahedral blockade Hamiltonian.
Requires Python 3.10+ and sympy. Run: python verify_exact.py
"""
import sympy as S
from collections import Counter

# Two poles 0,11; two pentagons 1..5 and 6..10.
EDGES=set()
def edge(a,b):
    EDGES.add(tuple(sorted((a,b))))
for i in range(5):
    u=1+i; v=6+i
    for a,b in ((0,u),(11,v),(u,1+(i+1)%5),
                (v,6+(i+1)%5),(u,v),(u,6+(i-1)%5)):
        edge(a,b)
assert len(EDGES)==30
# Check local degrees and number of triangular faces.
assert all(sum(v in e for e in EDGES)==5 for v in range(12))
assert sum(all(tuple(sorted((a,b))) in EDGES for a,b in ((u,v),(v,w),(u,w)))
           for u in range(12) for v in range(u+1,12)
           for w in range(v+1,12))==20

IS=[s for s in range(1<<12) if all(not ((s>>a)&1 and (s>>b)&1) for a,b in EDGES)]
EVEN=[s for s in IS if s.bit_count()%2==0]
ODD=[s for s in IS if s.bit_count()%2==1]
assert Counter(s.bit_count() for s in IS)=={0:1,1:12,2:36,3:20}
assert (len(EVEN),len(ODD))==(37,32)

# H=[[0,B(t)],[B(t).T,0]], using increasing integer-bitmask basis order.
t=S.symbols('t')
B=S.Matrix([[(t if (a^b)==1 else 1) if (a^b).bit_count()==1 else 0
              for b in ODD] for a in EVEN])
G=(B.subs(t,1).T*B.subs(t,1))
z=S.symbols('z')
expected=(z**6*(z-3)**4*(z-1)**4*(z*z-30*z+84)
          *(z*z-16*z+44)**3*(z*z-10*z+12)**5)
assert S.expand(G.charpoly(z).as_expr()-expected)==0

# The 32 rows below index EVEN in ascending bitmask order, 0-based.
ROWS=[0,1,3,2,4,5,6,7,8,9,10,11,14,12,18,17,
      16,15,19,20,21,23,22,13,25,26,31,30,29,27,24,32]
assert len(ROWS)==32 and len(set(ROWS))==32
M=B.extract(ROWS,list(range(32)))
det=S.factor(M.det(method='domain-ge'))
assert S.expand(det-2*(t*t-1)**6)==0
print('PASS: 69 configurations, parity dimensions 37/32')
print('PASS: uniform Gram factorization and rank 26; nullity 17')
print('PASS: selected 32x32 minor = 2(t^2-1)^6')
print('PASS: every real t with |t|!=1 has rank 32 and nullity 5')
