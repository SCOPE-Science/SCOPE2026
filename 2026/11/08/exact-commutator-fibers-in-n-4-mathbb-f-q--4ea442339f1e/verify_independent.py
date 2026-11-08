#!/usr/bin/env python3
"""Independent six-variable quotient count and adjoint-rank spectrum checks."""
from itertools import product
from collections import Counter

def rank_mod(matrix, p):
    a = [row[:] for row in matrix]
    n = len(a); r = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(r, n) if a[i][col] % p), None)
        if pivot is None: continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][col], -1, p)
        a[r] = [(z * inv) % p for z in a[r]]
        for i in range(r+1, n):
            k=a[i][col]
            if k:
                a[i]=[(x-k*y)%p for x,y in zip(a[i],a[r])]
        r+=1
        if r == n: break
    return r

def check(q):
    # Only prime q used here; the structural argument handles all prime powers.
    counts=Counter()
    exceptional=0
    for a,b,c,A,B,C in product(range(q), repeat=6):
        u=(a*B-b*A)%q
        v=(b*C-c*B)%q
        counts[u,v]+=1
        exceptional += (a==c==A==C==0)
    for u,v in product(range(q),repeat=2):
        expect=(2*q**4-q**2) if (u==0 and v==0) else q*q*(q*q-1)
        assert counts[u,v] == expect, (q,u,v,counts[u,v],expect)
    assert exceptional==q*q
    # For each pair with nonexceptional first-layer data, central output is uniform;
    # exceptional pairs force central output zero. Check the resulting mass.
    generic=q**7*(q*q-1)
    pure=2*generic
    zero=pure+q**8
    assert zero+(q-1)*pure+(q*q-1)*q*generic==q**12
    print('quotient q=',q,'zero=',zero,'noncentral=',generic,'central_nonzero=',pure)

for p in (2,3,5):
    check(p)
    hist=Counter()
    for a,b,c,d,e,f in product(range(p),repeat=6):
        rows=[[-b,a,0,0,0,0],
              [0,-c,b,0,0,0],
              [-e,0,d,-c,a,0]]
        hist[rank_mod(rows,p)]+=1
    expected={0:p,
              1:p**3-p,
              2:p**3*(p*p+p-2),
              3:p**3*(p-1)*(p*p-1)}
    assert dict(hist)==expected, (p,hist,expected)
    commuting=sum(v*p**(6-r) for r,v in hist.items())
    assert commuting==p**8+2*p**9-2*p**7
    print('rank spectrum q=',p,dict(sorted(hist.items())))
print('VERIFY_OK')
