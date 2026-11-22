"""Finite diagnostic checks for a uniform local semigroup theorem.
The mathematical proof does not depend on a finite verification range.
"""
from collections import defaultdict

PRIME = 101

def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i+j] = (out[i+j] + u*v) % PRIME
    return out

def polynomial_degree_pivots(n):
    phi = [1, 1, 1]
    phipowers = [[1]]
    for _ in range(n):
        phipowers.append(poly_mul(phipowers[-1], phi))
    vectors = []
    for r in range(n+1):
        for i in range(r+1):
            v = [0]*i + phipowers[r]
            v += [0]*(3*n + 1 - len(v))
            vectors.append(v)
    pivots = {}
    for v in vectors:
        v = v[:]
        while any(v):
            d = max(j for j,c in enumerate(v) if c % PRIME)
            if d not in pivots:
                inverse = pow(v[d], -1, PRIME)
                pivots[d] = [(c*inverse)%PRIME for c in v]
                break
            mul = v[d]
            v = [(c-mul*w)%PRIME for c,w in zip(v,pivots[d])]
    return set(pivots)

def basic_semigroup(m, bound):
    have = {0}
    for n in range(bound+1):
        if n in have:
            for a in [m,m+2,m+6]:
                if n+a<=bound: have.add(n+a)
    return have

for n in range(1,18):
    assert polynomial_degree_pivots(n) == ({0} | set(range(2,3*n+1)))
for g in range(4,101):
    m=2*g-5
    q,r=divmod(m,3)
    ap=[m*(t//3+t%3)+2*t for t in range(m)]
    assert len({a%m for a in ap})==m
    conductor=max(ap)-m+1
    expect_conductor=(q+2)*m-(3 if r==1 else 1)
    expect_delta=3*q*(q+1)//2+r*q+r*(r-1)//2+(m-1)//2
    assert conductor==expect_conductor
    assert conductor < (m//3+(1 if m%3 else 0)+2)*m
    vals=basic_semigroup(m,conductor+m+6)
    assert all(x in vals for x in range(conductor,conductor+m+6))
    assert sum(t not in vals for t in range(conductor))==expect_delta
    assert all(a in vals for a in ap)
    for k in range(conductor):
        if k==0 or k not in vals:continue
        # E_n contains each possible valuation below the conductor;
        # no two distinct homogeneous degrees may share one below it.
        n_support=[]
        for n in range(1,k//m+1):
            possible={n*(m+6)-2*d for d in [0]+list(range(2,3*n+1))}
            if k in possible:n_support.append(n)
        assert len(n_support)==1,(g,k,n_support)
print('FINITE_CHECKS_PASSED: polynomial spans n=1..17; Apéry, gaps, nonoverlap g=4..100')
for g in (4,5,6,7,8,9,10,13):
    m=2*g-5;q,r=divmod(m,3)
    ap=[m*(t//3+t%3)+2*t for t in range(m)]
    print(f'g={g}: m={m}, conductor={max(ap)-m+1}, delta={3*q*(q+1)//2+r*q+r*(r-1)//2+(m-1)//2}')
