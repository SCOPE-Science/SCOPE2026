#!/usr/bin/env python3
"""Reproducible checks for bicyclic commutation centralizers and finite balls."""
from fractions import Fraction

def prod(u,v):
    a,b=u;c,d=v;t=min(b,c)
    return a+c-t,b+d-t

def ball(n):
    return [(a,b) for a in range(n+1) for b in range(n-a+1)]

def expected_central(x,y):
    a,b=x;c,d=y
    if a==b: return (c>=a and d>=a) or (c==d and c<a)
    if a>b: return (c>=b and d==b) or (c==d and c<b)
    return (c==a and d>=a) or (c==d and c<a)

def predicted(N):
    return ((N+2)**2*(2*N+1)//4 if N%2==0 else (N+1)**2*(2*N+5)//4)

for M in range(8):
    B=ball(M)
    for u in B:
        for v in B:
            assert (prod(u,v)==prod(v,u))==expected_central(u,v)
    k=sum(prod(u,v)==prod(v,u) for u in B for v in B)
    assert k==predicted(M), (M,k,predicted(M))
    print(f'N={M}, ball={len(B)}, commuting_ordered_pairs={k}, exact=PASS')
# Check individual bivariate generating-function coefficients, independent of ball sums.
for m in range(7):
    for n in range(7):
        X=[(a,m-a) for a in range(m+1)]
        Y=[(c,n-c) for c in range(n+1)]
        actual=sum(prod(u,v)==prod(v,u) for u in X for v in Y)
        # (1-xy)/(1+xy) = 1+2*sum_{j>=1} (-1)^j (xy)^j.
        expected=(m+1)*(n+1)+2*sum((-1)**j*(m-j+1)*(n-j+1) for j in range(1,min(m,n)+1))
        assert actual==expected,(m,n,actual,expected)
print('BIVARIATE_COEFFICIENTS_PASS: 49 coefficients')
print('ALL_CHECKS_PASS')
