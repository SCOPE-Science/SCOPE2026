#!/usr/bin/env python3
"""Exact finite certificate for quadratic harmonic sampling on a 14-vertex spherical grid.
Run: python3 rhombic_erasure_certificate.py . No external packages or inputs required.
The two modular maps are homomorphisms from Z[1/3,sqrt(3)] to F_p.
"""
from itertools import combinations, permutations, product
from fractions import Fraction
from collections import Counter

# Indices 0..5: -e1,+e1,-e2,+e2,-e3,+e3; 6..13: lexicographic corners.
V=[]
for i in range(3):
    for sign in (-1,1):
        t=[0,0,0];t[i]=sign;V.append((tuple(t),False))
for signs in product((-1,1),repeat=3):
    V.append((signs,True))
assert len(V)==14

# A+b*sqrt(3), with rational A,B, represented exactly by pairs.
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def mul(a,b):return (a[0]*b[0]+3*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def const(q):return (Fraction(q),Fraction(0))

def eval_row(vertex):
    u,corner=vertex
    x,y,z=[(Fraction(0),Fraction(v,3)) if corner else const(v) for v in u]
    x2,y2,z2=mul(x,x),mul(y,y),mul(z,z)
    return [const(1),x,y,z,mul(x,y),mul(x,z),mul(y,z),
            add(x2,(-y2[0],-y2[1])),
            add(add(x2,y2),(-2*z2[0],-2*z2[1]))]
R=[eval_row(v) for v in V]

# These four explicit degree-at-most-two harmonic-coordinate annihilators
# are tested directly over Q(sqrt(3)); zero rows remain zero on rotations.
W={
  0x0f3f:[0,0,0,0,0,1,1,0,0],
  0x1bdb:[0,0,-2,-2,(0,-2),(0,-2),0,-1,1],
  0x1f8f:[-1,0,0,0,-3,-3,-3,0,1],
  0x3fc3:[0,0,0,0,0,0,0,-1,1],
}
for mask,coefficients in W.items():
    coeff=[(const(t) if isinstance(t,int) else (Fraction(t[0]),Fraction(t[1]))) for t in coefficients]
    assert any(a!=(0,0) for a in coeff)
    for i in range(14):
        if (mask>>i)&1:
            v=(Fraction(0),Fraction(0))
            for q,c in zip(R[i],coeff):v=add(v,mul(q,c))
            assert v==(0,0),(hex(mask),i,v)

# Full octahedral group: signed coordinate permutations; actual set symmetry.
actions=[]
for perm in permutations(range(3)):
    for signs in product((-1,1),repeat=3):
        a=[]
        for v,c in V:
            dst=(tuple(signs[i]*v[perm[i]] for i in range(3)),c)
            a.append(V.index(dst))
        actions.append(a)
assert len({tuple(a) for a in actions})==48

def act(mask,a):return sum(1<<a[i] for i in range(14) if mask&(1<<i))
orbits={m:{act(m,a) for a in actions} for m in W}
assert [len(orbits[k]) for k in W]==[6,24,12,3]
assert len(set.union(*orbits.values()))==45

def mod_pair(a,p,root):
    def convert(q):return (q.numerator%p)*pow(q.denominator,-1,p)%p
    return (convert(a[0])+root*convert(a[1]))%p

def rank(rows,p):
    pivots={}
    for row in rows:
        v=list(row)
        for j,base in sorted(pivots.items()):
            if v[j]:
                f=v[j]
                v=[(c-f*b)%p for c,b in zip(v,base)]
        first=next((j for j,t in enumerate(v) if t),None)
        if first is not None:
            inv=pow(v[first],-1,p)
            pivots[first]=[(t*inv)%p for t in v]
    return len(pivots)

for p,root in ((97,10),(109,49)):
    assert root*root%p==3
    M=[[mod_pair(a,p,root) for a in row] for row in R]
    defect=[];count_full={}
    for k in (10,11):
        full=0
        for inds in combinations(range(14),k):
            mask=sum(1<<i for i in inds)
            r=rank([M[i] for i in inds],p)
            if r==9:full+=1
            else:
                assert k==10 and r==8
                defect.append(mask)
        count_full[k]=full
    assert count_full=={10:956,11:364},(p,count_full)
    assert set(defect)==set.union(*orbits.values())
    assert all(rank([M[i] for i in range(14) if m>>i&1],p)==8 for m in W)
    print('CERTIFIED_MODULUS',p,'sqrt3',root,'10_recoverable',956,'10_defective',45,'11_recoverable',364)
print('QUADRATIC_RHOMBIC_ERASURE_CERTIFICATE_OK; four orbit sizes 6,24,12,3')
