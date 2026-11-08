#!/usr/bin/env python3
"""Reproduce finite rank-two game and ordered-partition identities."""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb, factorial, log


def compositions(n):
    if n == 0:
        yield ()
    else:
        for mask in range(1 << (n - 1)):
            out = []
            k = 1
            for j in range(n - 1):
                if mask & (1 << j):
                    out.append(k)
                    k = 1
                else:
                    k += 1
            out.append(k)
            yield tuple(out)


def labels(comp):
    return tuple(j for j,k in enumerate(comp) for _ in range(k))


def atomic(a,b,la):
    return (a == b, la[a] <= la[b], la[b] <= la[a])


def qr2_game(la,lb):
    def forth(aa,bb):
        for x in range(len(aa)):
            if not any(all(any(atomic(x,y,aa)==atomic(u,v,bb) for v in range(len(bb))) for y in range(len(aa)))
                       and all(any(atomic(u,v,bb)==atomic(x,y,aa) for y in range(len(aa))) for v in range(len(bb)))
                       for u in range(len(bb))):
                return False
        return True
    return forth(la,lb) and forth(lb,la)


def profile(comp):
    return frozenset((j>0,j<len(comp)-1,k>1) for j,k in enumerate(comp))


def weight(comp):
    n=sum(comp)
    w=factorial(n)
    denom=1
    for k in comp: denom*=factorial(k)
    return w//denom

# Exact 2-round games vs realized-point profiles for every pair across sizes 1..5.
C=[c for n in range(1,6) for c in compositions(n)]
L=[labels(c) for c in C]
for i in range(len(C)):
    for j in range(len(C)):
        assert qr2_game(L[i],L[j]) == (profile(C[i]) == profile(C[j])), (C[i],C[j])

c=[1]
for n in range(1,20):
    c.append(sum(comb(n,k)*c[n-k] for k in range(1,n+1)))
for n in range(1,15):
    allcomp=list(compositions(n))
    assert sum(weight(q) for q in allcomp) == c[n]
    singleton_l=sum(weight(q) for q in allcomp if q[0]==1)
    singleton_both=sum(weight(q) for q in allcomp if len(q)>=2 and q[0]==q[-1]==1)
    assert singleton_l==n*c[n-1]
    assert singleton_both==n*(n-1)*c[n-2] if n>=2 else singleton_both==0
    if n>=3:
        typical=[q for q in allcomp if len(q)>=3 and any(k==1 for k in q[1:-1]) and any(k>=2 for k in q[1:-1])]
        for q in typical:
            expected=frozenset({(False,True,q[0]>1),(True,False,q[-1]>1),(True,True,False),(True,True,True)})
            assert profile(q)==expected

# 16 unions of 4 endpoint atoms: equal-mass middle atoms cause exactly 12 distinct polynomials in t=log 2.
# Expand t^2, t(1-t), t(1-t), (1-t)^2 in polynomial coefficient basis (1,t,t^2).
atom_polys=[(0,0,1),(0,1,-1),(0,1,-1),(1,-2,1)]
polyset=set()
for mask in range(16):
    coeff=tuple(sum(atom_polys[i][d] for i in range(4) if (mask>>i)&1) for d in range(3))
    polyset.add(coeff)
assert len(polyset)==12

# Derive sharp rare-event count by exactly summing compositions.
for n in (8,12,16):
    bad=sum(weight(q) for q in compositions(n) if not (len(q)>=3 and any(k>=2 for k in q[1:-1])))
    # Coefficient of 1+A+A^2/(1-z), multiplied by n!, through power-series arithmetic
    gf_coeff=sum((Fraction(2**k-2, factorial(k)) for k in range(2,n+1)), Fraction(0)) + Fraction(1,factorial(n))
    assert bad==gf_coeff*factorial(n)
    pr=bad/c[n]
    asym=2*log(2)*(2.718281828459045-1)**2*log(2)**n
    print('n=',n,'p(rank-two no interior nonsingleton)=',float(pr),'asym=',asym,'ratio=',float(pr)/asym)
print('RANK_TWO_RANDOM_PREORDER_CHECKS_OK', 'EF_pairs=',len(C)**2,'composition_counts=',sum(2**(n-1) for n in range(1,15)),'distinct_limits=',len(polyset))
