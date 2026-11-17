#!/usr/bin/env python3
"""Exact integral orbit chains of the proper-part NC(D_5) under Coxeter conjugation.
Run with Python 3.10+ and sympy (tested on sympy 1.13+).
"""
from collections import Counter
from functools import lru_cache, reduce
from itertools import permutations, product
from math import prod, factorial
import json
import sympy as sp
from sympy.polys.domains import ZZ
from sympy.matrices.normalforms import smith_normal_form

n = 5
identity = tuple(range(1, n+1))

def multiply(a, b):
    return tuple((1 if x > 0 else -1) * a[abs(x)-1] for x in b)

def inverse(a):
    b = [0] * n
    for i, x in enumerate(a):
        b[abs(x)-1] = (1 if x > 0 else -1) * (i+1)
    return tuple(b)

def reflection(i,j,flipped=False):
    a=list(identity)
    a[i-1],a[j-1] = ((-j,-i) if flipped else (j,i))
    return tuple(a)

simples = [reflection(i,i+1) for i in range(1,n)] + [reflection(n-1,n,True)]
coxeter = reduce(multiply, simples, identity)
assert coxeter == (2,3,4,-1,-5)

# Signed-permutation reflection length: codimension of fixed space,
# equal to n minus the number of positive signed cycles.
@lru_cache(None)
def length(a):
    seen = set()
    positive = 0
    for start in range(n):
        if start in seen:
            continue
        x=start
        sign=1
        while x not in seen:
            seen.add(x)
            z=a[x]
            sign *= (1 if z>0 else -1)
            x=abs(z)-1
        positive += (sign == 1)
    return n-positive

group=[]
for p in permutations(range(1,n+1)):
    for ss in product((-1,1), repeat=n-1):
        signs = ss + (prod(ss),)
        group.append(tuple(x*s for x,s in zip(p,signs)))
assert len(group)==1920
assert length(coxeter)==n
assert all(multiply(a,inverse(a)) == identity for a in group)

# Independent length check: exact nullity calculation on a fixed sample
# from every possible reflection length, with independent matrix code.
for k in range(n+1):
    sample=next(a for a in group if length(a)==k)
    A=sp.zeros(n)
    for j,v in enumerate(sample):
        A[abs(v)-1,j] = 1 if v>0 else -1
    assert (A-sp.eye(n)).rank() == k

@lru_cache(None)
def below(a,b):
    return length(a)+length(multiply(inverse(a),b))==length(b)

nc = [w for w in group if below(w,coxeter)]
nc.sort(key=lambda w:(length(w),w))
rank_counts=Counter(length(w) for w in nc)
assert len(nc)==182 and rank_counts == {0:1,1:20,2:70,3:70,4:20,5:1}
proper = nc[1:-1]

higher={a:[b for b in proper if length(b)>length(a) and below(a,b)] for a in proper}
chains={0:[(a,) for a in proper]}
for dimension in range(1,n-1):
    chains[dimension]=[chain+(b,) for chain in chains[dimension-1] for b in higher[chain[-1]]]
assert [len(chains[i]) for i in range(4)] == [180,1536,3328,2048]
assert len(chains[3]) == factorial(n)*(2*(n-1))**n // len(group)

ci=inverse(coxeter)
def rotation(a):
    return multiply(multiply(coxeter,a),ci)
rot={a:rotation(a) for a in proper}
assert set(rot.values())==set(proper)
assert all(rot[rot[rot[rot[rot[rot[rot[rot[w]]]]]]]] == w for w in proper)

representatives={}; orbit_lookup={}; orbit_sizes={}
for dimension,faces in chains.items():
    remaining=set(faces)
    representatives[dimension]=[]
    orbit_lookup[dimension]={}
    orbit_sizes[dimension]=[]
    while remaining:
        ch=min(remaining)
        orbit=[]
        y=ch
        while y not in orbit:
            orbit.append(y)
            y=tuple(rot[x] for x in y)
        assert y==ch
        index=len(representatives[dimension])
        for y in orbit:
            assert y in remaining
            remaining.remove(y)
            orbit_lookup[dimension][y]=index
        representatives[dimension].append(ch)
        orbit_sizes[dimension].append(len(orbit))
assert [len(representatives[i]) for i in range(4)] == [32,228,448,256]
assert [Counter(orbit_sizes[i]) for i in range(4)] == [
    {2:2,4:16,8:14}, {4:72,8:156}, {4:64,8:384}, {8:256}
]

B={}
for d in (1,2,3):
    mat=sp.zeros(len(representatives[d-1]), len(representatives[d]))
    for j,ch in enumerate(representatives[d]):
        for k in range(d+1):
            face=ch[:k]+ch[k+1:]
            mat[orbit_lookup[d-1][face],j]+=(-1)**k
    B[d]=mat
assert B[1]*B[2]==sp.zeros(32,448)
assert B[2]*B[3]==sp.zeros(228,256)

smith={}
for d in (1,2,3):
    D=smith_normal_form(B[d], domain=ZZ)
    smith[d]=Counter(abs(int(D[j,j])) for j in range(min(D.shape)) if D[j,j]!=0)
assert smith=={1:{1:31},2:{1:196,2:1},3:{1:250,2:1}}

r={d:sum(smith[d].values()) for d in (1,2,3)}
free_h1=228-r[1]-r[2]
free_h2=448-r[2]-r[3]
free_h3=256-r[3]
assert (free_h1,free_h2,free_h3)==(0,0,5)
assert 32-228+448-256 == 1-free_h1+free_h2-free_h3 == -4
assert 180-1536+3328-2048 == -76  # cover has 77 third spheres

# Rank drops at the prime 2 reproduce the UCT mod-two Betti vector.
mod2r={d:r[d]-smith[d].get(2,0) for d in (1,2,3)}
mod2betti=[32-mod2r[1],228-mod2r[1]-mod2r[2],448-mod2r[2]-mod2r[3],256-mod2r[3]]
assert mod2betti==[1,1,2,6]

report={
 'object':'proper-part order complex of NC(D5) modulo conjugation by a Coxeter element',
 'coxeter_signed_images':coxeter,'group_order':len(group),'noncrossing_rank_counts':[rank_counts[i] for i in range(6)],
 'cover_cell_counts':[len(chains[i]) for i in range(4)],
 'quotient_cell_counts':[len(representatives[i]) for i in range(4)],
 'quotient_orbit_sizes':[{str(k):v for k,v in sorted(Counter(orbit_sizes[i]).items())} for i in range(4)],
 'boundary_shapes':{str(i):list(B[i].shape) for i in (1,2,3)},
 'boundary_smith_nonzero':{str(i):{str(k):v for k,v in sorted(smith[i].items())} for i in (1,2,3)},
 'mod2_betti':mod2betti,
 'integral_homology':['Z','Z/2','Z/2','Z^5'],
 'boundary_compositions_zero':True,
 'status':'PASS'
}
print(json.dumps(report,sort_keys=True,indent=2))
