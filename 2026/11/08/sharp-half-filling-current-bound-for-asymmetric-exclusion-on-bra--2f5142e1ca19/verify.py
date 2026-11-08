#!/usr/bin/env python3
"""Reproducible exact checks for a half-filled exclusion-network current bound."""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
from random import Random

def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0

def elementary(weights):
    a = [Q(1)]
    for w in weights:
        w=Q(w)
        a = [a[0]]+[a[j]+w*a[j-1] for j in range(1,len(a))]+[w*a[-1]]
    return a

def certificate(m, t):
    """Both sides of the exact positive elementary-symmetric expansion."""
    z=elementary([1+x for x in t])
    e=elementary(t)
    lhs=(m+1)*(z[m-1]+z[m+1])-2*m*z[m]
    rhs=sum(Q(j*(j-1),m+1-j)*choose(2*m-j,m-j)*e[j]
            for j in range(2,m+1)) + (m+1)*e[m+1]
    return lhs, rhs

def current(L, weights):
    total=L+len(weights)
    assert total%2==0 and L>=3
    N=total//2
    c=elementary(weights)
    z=sum(x*choose(L,N-i) for i,x in enumerate(c))
    numerator=sum(x*choose(L-2,N-1-i) for i,x in enumerate(c))
    return numerator/z

def generator_check(L, edges, weights, N, hf, hb):
    """Exact stationarity for tree edges (tail,head,forward,backward)."""
    S=L+len(weights)
    states=[sum(1<<v for v in sites) for sites in combinations(range(S),N)]
    rates={}
    for a in range(L):
        b=(a+1)%L
        rates[(a,b)]=Q(hf)
        rates[(b,a)]=Q(hb)
    for a,b,f,r in edges:
        rates[(a,b)]=Q(f)
        rates[(b,a)]=Q(r)
    w={s:__import__('functools').reduce(lambda x,y:x*y,
              (weights[v-L] for v in range(L,S) if s>>v&1),Q(1)) for s in states}
    residual={s:Q(0) for s in states}
    for state in states:
        for (a,b),rate in rates.items():
            if state>>a&1 and not state>>b&1 and rate:
                other=state^(1<<a)^(1<<b)
                residual[state]-=w[state]*rate
                residual[other]+=w[state]*rate
    assert all(value==0 for value in residual.values()),residual

def main():
    rng=Random(402026)
    tests=0
    for m in range(1,8):
        for _ in range(30):
            t=[Q(rng.randint(0,8),rng.randint(1,7))
               for i in range(2*m)]
            left,right=certificate(m,t)
            assert left==right and right>=0
            tests+=1
    for L in range(3,11):
        for M in range(1,7):
            if (L+M)%2: continue
            n=(L+M)//2
            for q in (Q(1,7),Q(1,2),Q(1),Q(7,3),Q(5)):
                # A rooted path is a legitimate tree on M off-backbone vertices.
                weights=[q**d for d in range(1,M+1)]
                j=current(L,weights)
                j0=Q(n,2*(2*n-1))
                assert j<=j0
                assert (j==j0)==(M==1 or q==1)
                tests+=1
    # Independent weighted microcanonical enumeration and stationarity:
    # L=4 backbone, one attached two-vertex path.
    generator_check(4,[(0,4,Q(3),Q(2)),(4,5,Q(3),Q(2))],
                    [Q(3,2),Q(9,4)],3,Q(2),Q(1))
    tests+=1
    # Same-site count, two attached leaves with opposing tree biases.
    generator_check(4,[(0,4,Q(2),Q(1)),(2,5,Q(1),Q(2))],
                    [Q(2),Q(1,2)],3,Q(2),Q(1))
    assert current(4,[Q(2),Q(1,2)])==Q(7,23)
    assert current(4,[Q(1),Q(1)])==Q(3,10)
    tests+=3
    print("PASS: %d exact certificate, current, and generator checks"%tests)

if __name__=="__main__":
    main()
