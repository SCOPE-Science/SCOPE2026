#!/usr/bin/env python3
"""Exact integral incidence certificate for degree-two del Pezzo conic pencils.

Run in the same directory as operations.json: python3 verify.py
All arithmetic uses Python's exact integers; no third-party package is needed.
"""
import itertools
import json
from collections import Counter
from pathlib import Path


def intersection(a,b):
    return a[0]*b[0]-sum(x*y for x,y in zip(a[1:],b[1:]))

K=(-3,)+(-1,)*7
curves=[]
for i in range(7):
    x=[0]*8;x[i+1]=-1;curves.append(tuple(x))
for i,j in itertools.combinations(range(7),2):
    x=[1]+[0]*7;x[i+1]=x[j+1]=1;curves.append(tuple(x))
for I in itertools.combinations(range(7),5):
    x=[2]+[int(i in I) for i in range(7)];curves.append(tuple(x))
for i in range(7):
    x=[3]+[1]*7;x[i+1]=2;curves.append(tuple(x))
assert len(curves)==56==len(set(curves))
assert all(intersection(E,E)==-1 and intersection(K,E)==-1 for E in curves)
# Complete exceptional classes, using Cauchy to constrain 0 <= d <= 3.
# Bound |m_i| by sqrt(d*d+1) and search every possible integer tuple.
import math
possible_curves=set()
for d in range(4):
    m_bound=math.isqrt(d*d+1)
    for m in itertools.product(range(-m_bound,m_bound+1),repeat=7):
        if sum(m)==3*d-1 and sum(z*z for z in m)==d*d+1:
            possible_curves.add((d,)+m)
assert possible_curves==set(curves) and len(possible_curves)==56
roots=[]
for i,j in itertools.permutations(range(7),2):
    x=[0]+[0]*7;x[i+1]=-1;x[j+1]=1;roots.append(tuple(x))
for I in itertools.combinations(range(7),3):
    x=[1]+[int(i in I) for i in range(7)];roots.extend([tuple(x),tuple(-y for y in x)])
for i in range(7):
    x=[2]+[int(j!=i) for j in range(7)];roots.extend([tuple(x),tuple(-y for y in x)])
assert len(roots)==126==len(set(roots))
assert all(intersection(r,r)==-2 and intersection(K,r)==0 for r in roots)

# Complete roots: by Cauchy, |d| <= 2, and |m_i| <= 2. This is exhaustive.
root_set=set(roots)
possible=[]
for d in range(-2,3):
    for m in itertools.product(range(-2,3),repeat=7):
        if sum(m)==3*d and sum(z*z for z in m)==d*d+2:
            possible.append((d,)+m)
assert set(possible)==root_set and len(possible)==126

A=[]
curve_set=set(curves)
for r in roots:
    f=tuple(-a+b for a,b in zip(K,r))
    assert intersection(f,f)==0 and intersection(K,f)==-2
    ints=[intersection(f,E) for E in curves]
    assert Counter(ints)=={0:12,1:32,2:12}
    supported=[E for E,val in zip(curves,ints) if val==0]
    # The 12 components make six disjoint intersecting pairs:
    # their disjointness graph is the thin D6 graph K12 minus a perfect matching.
    assert Counter(intersection(E,G) for E,G in itertools.combinations(supported,2))=={0:60,1:6}
    for E,val in zip(curves,ints):
        if val==0:
            F=tuple(a-b for a,b in zip(f,E))
            assert F in curve_set and intersection(E,F)==1 and F in supported
            assert sum(intersection(E,G)==1 for G in supported if G!=E)==1
    A.append([int(z==0) for z in ints])
assert Counter(map(sum,A))=={12:126}
assert Counter(map(sum,zip(*A)))=={27:56}
# Geiser-involute exceptional curves are disjoint in the support coordinates.
assert len({tuple(-k-e for k,e in zip(K,E)) for E in curves})==56
# Independent intersection-pattern check, before integral Smith replay.
col_counts=Counter(sum(A[i][j]*A[i][k] for i in range(126))
                   for j in range(56) for k in range(j+1,56))
assert col_counts=={0:28,1:756,10:756}

ops=json.loads((Path(__file__).parent/'operations.json').read_text('utf-8'))
assert len(ops)==2313
N,M=126,56
for op in ops:
    kind,i,j=op[:3]
    if kind=='rs':
        assert 0<=i<N and 0<=j<N
        A[i],A[j]=A[j],A[i]
    elif kind=='cs':
        assert 0<=i<M and 0<=j<M
        for row in A:row[i],row[j]=row[j],row[i]
    elif kind=='ra':
        q=op[3]
        assert 0<=i<N and 0<=j<N and isinstance(q,int)
        if i==j:
            assert q==-2  # multiplies this row by -1; still unimodular
            A[i]=[-v for v in A[i]]
        else:
            A[i]=[x+q*y for x,y in zip(A[i],A[j])]
    elif kind=='ca':
        q=op[3]
        assert 0<=i<M and 0<=j<M and i!=j and isinstance(q,int)
        for row in A:row[i]+=q*row[j]
    else:raise AssertionError('Unknown operation')

assert all(A[i][j]==0 for i in range(N) for j in range(M) if i!=j)
diag=[A[i][i] for i in range(56)]
assert diag==[1]*28+[2]*6+[6]+[0]*21
assert all(diag[i+1]%diag[i]==0 for i in range(34))
print('CERTIFICATE_OK: 126 pencils; 56 curves; 2313 unimodular operations')
print('SNF=1^28, 2^6, 6^1, 0^21')
print('cokernel = Z^21 + (Z/2)^6 + Z/6; torsion order 384, exponent 6')
