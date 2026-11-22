"""Finite exact diagnostic for parity-conditioned Rademacher first moments.

Supplementary only: the theorem for all dimensions is proved analytically.
"""
from itertools import product
from fractions import Fraction
from math import comb

checks=0
for n in range(2,11):
    signs=list(product((-1,1), repeat=n))
    classes={p:[s for s in signs if __import__('math').prod(s)==p] for p in (-1,1)}
    coeffs=[]
    for k in range(n):
        a=[0]*n; a[k]=1; coeffs.append(a)
    coeffs += [[1]*n,[-1]+[1]*(n-1),[2]+[1]*(n-1)]
    if n<=6:
        coeffs += [list(c) for c in product((-1,0,1),repeat=n) if any(c)]
    elif n<=8:
        coeffs += [list(c) for c in product((0,1),repeat=n) if any(c)]
    for a in coeffs:
        if not any(a): continue
        e={p:sum(abs(sum(x*y for x,y in zip(a,s))) for s in classes[p]) for p in (-1,1)}
        # Each parity class has the same cardinality; use integer sums
        if n&1:
            assert e[-1]==e[1],(n,a,e)
        else:
            assert (n-2)*e[-1]<=n*e[1],(n,a,e)
            assert (n-2)*e[1]<=n*e[-1],(n,a,e)
            if all(abs(x)==1 for x in a):
                assert (n-1)*abs(e[1]-e[-1])==e[1]+e[-1],(n,a,e)
        checks+=1
print(f'PARITY_KHINTCHINE_EXACT_OK {checks}')
