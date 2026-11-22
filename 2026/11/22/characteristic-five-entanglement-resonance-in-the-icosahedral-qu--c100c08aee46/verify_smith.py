#!/usr/bin/env python3
"""Independent integer-minor verification from the exact golden-ratio model.

Uses only the standard library. Smith invariant factors are obtained from
successive gcds of every square minor (determinantal divisors), with a
valid short circuit when the gcd reaches one.
"""
from itertools import product, combinations
from collections import Counter
from math import gcd, comb

ZERO, ONE, PHI = (0, 0), (1, 0), (0, 1)

def neg(pair): return (-pair[0], -pair[1])

def sub(u, v): return u[0] - v[0], u[1] - v[1]

def sq(u):
    a,b=u
    return a*a+b*b, 2*a*b+b*b # phi^2=phi+1

def dist2(u,v):
    x=[sq(sub(a,b)) for a,b in zip(u,v)]
    return sum(c[0] for c in x),sum(c[1] for c in x)

def graph():
    vertices=[]
    for s,t in product((-1,1),repeat=2):
        def sign(v,z): return v if z==1 else neg(v)
        vertices.extend([(ZERO,sign(ONE,s),sign(PHI,t)),
                         (sign(ONE,s),sign(PHI,t),ZERO),
                         (sign(PHI,s),ZERO,sign(ONE,t))])
    assert len(vertices)==12 and len(set(vertices))==12
    rows=[[int(i!=j and dist2(u,v)==(4,0)) for j,v in enumerate(vertices)]
          for i,u in enumerate(vertices)]
    assert all(sum(row)==5 for row in rows)
    assert sum(map(sum,rows))==60
    assert all(rows[i][j]==rows[j][i] for i in range(12) for j in range(12))
    return rows

def det(a):
    """Bareiss exact determinant with row swaps and integer divisions."""
    n=len(a)
    if n==0:return 1
    m=[list(row) for row in a]
    prev=1; sign=1
    for k in range(n-1):
        t=next((r for r in range(k,n) if m[r][k]),None)
        if t is None:return 0
        if t!=k: m[t],m[k]=m[k],m[t];sign=-sign
        pivot=m[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                value=m[i][j]*pivot-m[i][k]*m[k][j]
                assert value%prev==0
                m[i][j]=value//prev
            m[i][k]=0
        prev=pivot
    return sign*m[-1][-1]

def divisors(m,k):
    """Full gcd of k-by-k minors; gcd=1 short circuit is exact."""
    rows=len(m);cols=len(m[0]) if rows else 0
    g=0
    for rs in combinations(range(rows),k):
        for cs in combinations(range(cols),k):
            d=abs(det([[m[i][j] for j in cs] for i in rs]))
            g=gcd(g,d)
            if g==1:return 1
    return g

def smith_diagonal(m):
    k=len(m)
    if k==0:return ()
    delta=[None]*(k+1);delta[0]=1
    for j in range(k,0,-1):
        delta[j]=divisors(m,j)
        if delta[j]==1:
            for i in range(1,j):delta[i]=1
            break
    factors=[]
    for j in range(1,k+1):
        factors.append(0 if delta[j]==0 else delta[j]//delta[j-1])
        if delta[j]:assert delta[j]%delta[j-1]==0
    return tuple(factors)

EXPECTED={
 0:{():1},
 1:{(1,):12},
 2:{(1,1):66},
 3:{(1,1,1):220},
 4:{(1,1,1,0):15,(1,1,1,1):480},
 5:{(1,1,1,1,0):120,(1,1,1,1,1):672},
 6:{(1,1,1,1,0,0):140,(1,1,1,1,1,0):240,
    (1,1,1,1,1,1):500,(1,1,1,1,1,5):12,
    (1,1,1,1,2,0):12,(1,1,1,1,2,2):20}
}

def main():
    G=graph()
    for k in range(7):
        counts=Counter()
        for left in combinations(range(12),k):
            right=[v for v in range(12) if v not in left]
            M=[[G[i][j] for j in right] for i in left]
            counts[smith_diagonal(M)]+=1
        assert dict(counts)==EXPECTED[k],(k,counts)
        assert sum(counts.values())==comb(12,k)
        print('k',k, 'Smith classes:',sorted(counts.items()))
    print('PASS: all 2510 subsets of size <=6 checked by exact integer minors')
    print('PASS: all six balanced-cut Smith types and only prime factors 2,5')

if __name__=='__main__':main()
