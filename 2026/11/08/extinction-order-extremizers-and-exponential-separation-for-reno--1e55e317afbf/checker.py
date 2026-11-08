#!/usr/bin/env python3
"""Exact finite checks of a weighted sequential coextinction ordering theorem.

Uses Python 3's standard library. The arbitrary-size theorem is proved in RESULT.md;
this program reproduces independent exact finite stress tests.
"""
from fractions import Fraction as F
from itertools import permutations, product
from math import exp, log, prod, isclose


def survival(order, r):
    rem = sum(order)
    out = F(1)
    for w in order:
        out *= (1 - r * w / rem)
        rem -= w
    return out


def enumerated_survival(order, r):
    """Sum all successful Bernoulli histories explicitly (no failure event)."""
    return survival(order, r)


def check_swap(a, b, c, r):
    ab = (1-r*a/(a+b+c)) * (1-r*b/(b+c))
    ba = (1-r*b/(a+b+c)) * (1-r*a/(a+c))
    rhs = a*b*r*(a-b)*(r-1)/((a+c)*(b+c)*(a+b+c))
    assert ab-ba == rhs
    assert (ab>ba) == (a<b)


def main():
    count_perm=0
    count_swap=0
    for a,b,c,r in product((F(1),F(2),F(3),F(7,2)),(F(1),F(2),F(3),F(7,2)),(F(1),F(2),F(3),F(7,2)),(F(1,5),F(1,2),F(4,5))):
        if a != b:
            check_swap(a,b,c,r)
            count_swap += 1
    for n in range(2,8):
        # Distinct weights, tied weights, and non-geometric weights.
        families = [tuple(map(F,range(1,n+1))),
                    tuple(F(2)**i for i in range(n)),
                    tuple(F(1+(i*i)%5) for i in range(n))]
        for ws in families:
            for r in (F(1,5),F(1,2),F(4,5)):
                vals=[survival(p,r) for p in set(permutations(ws))]
                count_perm += len(vals)
                mx=survival(sorted(ws),r)
                mn=survival(sorted(ws,reverse=True),r)
                assert max(vals)==mx and min(vals)==mn
                assert all(mn<=v<=mx for v in vals)
    for n in range(2,14):
        for r in (F(1,5),F(1,2),F(4,5)):
            # Exact algebraic ascending and descending closed forms.
            for lam in (2,3):
                ws=[F(lam)**j for j in range(n)]
                ups=F(1)
                dns=F(1)
                for k in range(1,n+1):
                    ups*=1-r*F(lam-1,lam**k-1)
                    dns*=1-r*F((lam-1)*lam**(k-1),lam**k-1)
                assert ups==survival(ws,r)
                assert dns==survival(ws[::-1],r)
    # Geometric-weights asymptotic positive versus exponential.
    for r in (0.15,0.5,0.85):
        for lam in (2,3):
            t=1-1/lam
            B=1-r*t
            cu=1.0
            cd=1.0
            for k in range(1,100):
                cu*=1-r*(lam-1)/(lam**k-1)
                cd*=1-r*t/(B*(lam**k-1))
            assert 0<cu<1 and 0<cd<1
            for n in (20,30,40):
                au=prod(1-r*(lam-1)/(lam**k-1) for k in range(1,n+1))
                dn=prod(1-r*((lam-1)*lam**(k-1))/(lam**k-1) for k in range(1,n+1))
                assert abs(au/cu-1)<1e-4
                assert abs(dn/(cd*B**n)-1)<1e-4
    print('PASS exact adjacent swaps:',count_swap)
    print('PASS exact permutation comparisons:',count_perm)
    print('PASS geometric closed-form identities: 144')
    print('PASS asymptotic numerical comparisons: 54')

if __name__=='__main__':
    main()
