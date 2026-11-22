#!/usr/bin/env python3
"""Exact, dependency-free checks for the icosahedral-facet Walsh theorem."""
from collections import Counter
from itertools import combinations
from fractions import Fraction

N = 12
SIZE = 1 << N
u = lambda j: 2 + (j % 5)
v = lambda j: 7 + (j % 5)

# First construction: four explicit families of five triangular facets.
explicit = set()
for j in range(5):
    for tri in ((0,u(j),u(j+1)), (1,v(j),v(j+1)),
                (u(j),u(j+1),v(j)), (u(j),v(j),v(j-1))):
        explicit.add(sum(1 << a for a in tri))
assert len(explicit) == 20

# Second construction: determine all graph triangles from the edge rule.
E = set()
def edge(a, b):
    E.add(tuple(sorted((a,b))))
for j in range(5):
    for pair in ((0,u(j)),(1,v(j)),(u(j),u(j+1)),
                 (v(j),v(j+1)),(u(j),v(j)),(u(j),v(j-1))):
        edge(*pair)
assert len(E) == 30
F = {sum(1<<a for a in tri) for tri in combinations(range(N),3)
     if all(tuple(sorted(pair)) in E for pair in combinations(tri,2))}
assert F == explicit
assert all(sum(a in pair for pair in E) == 5 for a in range(N))
assert all(sum(bool((mask & (1<<a)) and (mask & (1<<b))) for mask in F) == 2
           for (a,b) in E)

def hadamard_inplace(a):
    n = len(a)
    step = 1
    while step < n:
        for base in range(0,n,2*step):
            for j in range(base,base+step):
                x,y=a[j],a[j+step]
                a[j],a[j+step]=x+y,x-y
        step*=2

def face_sum(mask):
    return sum(1 if ((mask & face).bit_count() & 1) == 0 else -1
               for face in F)

by_weight=Counter()
hist=Counter()
zero_six=Counter()
zeros=[]
L=[]
for mask in range(SIZE):
    k = mask.bit_count()
    e = sum(((mask>>a)&1) * ((mask>>b)&1) for a,b in E)
    t = sum((mask & face) == face for face in F)
    value = 20-10*k+8*(e-t)
    assert value == face_sum(mask)
    assert value % 8 == (4-2*k) % 8
    assert value == -face_sum(mask ^ (SIZE-1))
    if value == 0:
        zeros.append(mask)
        if k == 6:
            assert e-t == 5
            zero_six[(e,t)]+=1
    by_weight[(k,value)]+=1
    hist[value]+=1
    L.append(value)

expected_hist={-20:1,-12:30,-10:44,-8:130,-6:380,-4:465,
               -2:600,0:796,2:600,4:465,6:380,8:130,
               10:44,12:30,20:1}
assert dict(hist) == expected_hist
assert Counter(x.bit_count() for x in zeros)=={2:36,6:724,10:36}
assert dict(zero_six)=={(5,0):72,(6,1):260,(7,2):180,
                        (8,3):120,(9,4):80,(10,5):12}
assert len(zeros)==796
assert min(abs(a) for a in L if a)!=0
assert min(abs(a) for a in L if a)==2
assert max(abs(a) for a in L)==20

# Independent Fourier calculation from delta masses of the faces.
counting_kernel=[int(s in F) for s in range(SIZE)]
hadamard_inplace(counting_kernel)
assert counting_kernel == L

# Recoverable-space projection: Walsh multiplier is 1 at nonzeros, 0 elsewhere.
P=[int(x!=0) for x in L]
hadamard_inplace(P)
expected_projection={-796:1,-60:60,-44:240,-28:294,-12:240,
                      0:2048,4:420,20:420,36:280,52:32,
                      84:60,3300:1}
assert Counter(P)==expected_projection
assert sum(abs(x) for x in P)==56232
assert Fraction(sum(abs(x) for x in P),SIZE)==Fraction(7029,512)
assert P[0]==3300 and P[SIZE-1]==-796
# Orthogonal projection identity, including normalization.
verify_mask=P.copy()
hadamard_inplace(verify_mask)
assert verify_mask==[SIZE*int(x!=0) for x in L]
assert sum(1 for x in L if x!=0)==3300

# Explicitly verify nonedges give exactly the 36 two-coordinate zeros.
nonedges={ (a,b) for a,b in combinations(range(N),2) if (a,b) not in E}
assert len(nonedges)==36
assert {s for s in zeros if s.bit_count()==2}=={
    (1<<a)|(1<<b) for a,b in nonedges}

print('PASS: 12 vertices, 30 edges, 20 triangular faces')
print('PASS: 4096 direct signed sums = 4096 edge/triangle formulas = exact Walsh transform')
print('PASS: complete signed histogram',sorted(hist.items()))
print('PASS: nullity 796; six-subset count 724; rank 3300; gap 2; condition 10')
print('PASS: normalized minimal endpoint projection constant 7029/512')
print('PASS: independent projection multiplier reconstruction')
