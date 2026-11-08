#!/usr/bin/env python3
"""Independent exact-state enumeration and asymptotic checks for a two-species exclusion gas."""
from fractions import Fraction
from itertools import product
from math import exp, log1p, sqrt, floor, cosh, tanh


def partition_formula(a, b, z):
    left = (1 + 2*z)**a - 1
    right = (1 + 2*z)**b - 1
    both = 2*((1 + z)**a - 1)*((1 + z)**b - 1)
    return (Fraction(1), left, right, both)


def brute(a, b, z):
    weights = [Fraction(0) for _ in range(4)]
    for states in product((0, 1, 2), repeat=a+b):
        l, r = states[:a], states[a:]
        if any(x in (1,2) and y in (1,2) and x != y for x in l for y in r):
            continue
        if not any(l) and not any(r):
            kind = 0
        elif any(l) and not any(r):
            kind = 1
        elif not any(l) and any(r):
            kind = 2
        else:
            kind = 3
        weights[kind] += z**sum(bool(v) for v in states)
    return tuple(weights)


def probs(a, b, z):
    # Log-sum-exp for three disjoint positive-weight classes and the empty state.
    import math
    def lexp(x):
        return math.log(math.expm1(x)) if x < 700 else x + math.log1p(-math.exp(-x))
    la = lexp(a*log1p(2*z))
    lb = lexp(b*log1p(2*z))
    lc = log1p(1) + lexp(a*log1p(z)) + lexp(b*log1p(z))
    L = max(0,la,lb,lc)
    w = [exp(-L),exp(la-L),exp(lb-L),exp(lc-L)]
    S=sum(w)
    return [u/S for u in w]


def limiting_probs(k, c):
    w=[exp(-2*c*c),exp(-2*c*c-2*k*c),2*exp(-c*c-k*c)]
    s=sum(w)
    return [x/s for x in w]


def main():
    exact = 0
    for a in range(1,5):
        for b in range(1,5):
            for z in [Fraction(1,4),Fraction(1,2),Fraction(1),Fraction(2)]:
                f=partition_formula(a,b,z)
                q=brute(a,b,z)
                assert f==q, (a,b,z,f,q)
                exact+=1
    print('Exact enumeration passes:',exact)
    asymp=0
    for k in (0,0.5,1,2,3):
        for c in (0.3,0.8,1.5,3):
            target=limiting_probs(k,c)
            for n in (1000,10000,100000):
                b=n-int(floor(k*sqrt(n)))
                observed=probs(n,b,c/sqrt(n))
                if n==100000:
                    err=max(abs(observed[j+1]-target[j]) for j in range(3))
                    assert err < .03, (k,c,err)
                asymp+=1
    print('Numerical asymptotic checks:',asymp)
    for k in (0,0.5,1,1.4142135623730951,1.5,2.5,4):
        c_grid=[j*.005 for j in range(1,2001)]
        p=[limiting_probs(k,c)[2] for c in c_grid]
        # Using position 2 for BOTH (w: left,right,both)
        diffs=[p[i+1]-p[i] for i in range(len(p)-1)]
        if k<=sqrt(2):
            assert min(diffs)>-1e-12, (k,min(diffs))
        else:
            assert min(diffs)<-1e-8 and max(diffs)>1e-8, k
    print('Reentrance threshold checks: 7')
    print('All verification tests passed')

if __name__=='__main__':
    main()
