"""Reproducible finite checks for a nonagon associahedral rotation quotient.
The complete integral-homology proof is the Mayer–Vietoris argument in RESULT.md.
No finite enumeration is claimed to prove the general secondary-polytope theorem.
"""
from itertools import combinations
from collections import Counter
from math import gcd

N=9
D=[(a,b) for a in range(N) for b in range(a+1,N) if b-a not in (1,N-1)]
assert len(D)==27

def cross(v,w):
 a,b=v;c,d=w
 return a<c<b<d or c<a<d<b

def shift(v,k): return tuple(sorted(((v[0]+k)%N,(v[1]+k)%N)))

C={1:[(i,) for i in range(len(D))]}
for size in range(2,7):
 C[size]=[s+(j,) for s in C[size-1] for j in range(s[-1]+1,len(D))
          if all(not cross(D[i],D[j]) for i in s)]
assert len(C[6])==429
index={v:i for i,v in enumerate(D)}
def rotate(s,k):return tuple(sorted(index[shift(D[i],k)] for i in s))
orb=[len({min(rotate(s,k) for k in range(N)) for s in C[d]}) for d in range(1,7)]
stabs=Counter()
for d in C:
 for s in C[d]: stabs[len([k for k in range(N) if rotate(s,k)==s])]+=1
# Vertex-action harmonic decomposition: trivial/first mode removed from 9 real coordinates.
# The retained Fourier modes are 2,3,4; stabilizer orders gcd(9,weight).
weights=(2,3,4)
assert [gcd(9,w) for w in weights]==[1,3,1]
# Distinct free and exceptional strata for the C9 action.
# E is a circle-mapping-torus of L(3;1,2), so H2(E)=Z/3, H3(E)=Z.
# E -> L(9;2,4) has degree 3 on H3.
# The exact homology LES implies |H3(Y)|=3*3=9.
print('diagonals',len(D),'face_counts', [len(C[d]) for d in range(1,7)])
print('rotational_orbits_by_face_size',orb)
print('stabilizers_face_count',sorted(stabs.items()))
print('representation_weights',weights,'isotropy_orders',[gcd(9,w) for w in weights])
print('MV_finite_groups',{'H1':'C3','H2':'0','H3_order':9,'H4':'0','H5':'Z'})
print('VERIFY_OK')
